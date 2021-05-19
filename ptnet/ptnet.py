#!/usr/bin/env python3

"""
Petri Net Module

Input file format: .pnml
Documentation: http://projects.laas.fr/tina//manuals/formats.html

ptnet.py is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
ptnet.py is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with ptnet.py. If not, see <https://www.gnu.org/licenses/>.
"""

__license__ = "GPLv3"
__version__ = "1.0.0"

import sys
import xml.etree.ElementTree as ET

from pandas import DataFrame


class PetriNet:
    """
    Petri Net.
    """

    def __init__(self, filename):
        """ Initializer.
        """
        self.places = {}
        self.transitions = {}

        self.initial_marking = []
        self.matrix = []

        self.parse_net(filename)
        self.compute_initial_marking()
        self.compute_incidence_matrix()

    def show(self):
        """ Show the incidence matrix and the iniial marking.
        """
        print("INCIDENCE MATRIX")
        print('================')
        print(DataFrame(self.matrix, index=self.places.keys(), columns=self.transitions.keys()))
        print()
        print("INITIAL MARKING")
        print("===============")
        print(DataFrame(self.initial_marking, index=self.places.keys(), columns=["m0"]))

    def parse_net(self, filename):
        """ Petri Net parser.
            Input format: .pnml
        """
        xmlns = "{http://www.pnml.org/version-2009/grammar/pnml}"

        tree = ET.parse(filename)
        root = tree.getroot()

        for index, place in enumerate(root.iter(xmlns + "place")):
            initial_marking = place.find(xmlns + 'initialMarking/' + xmlns + 'text')
            if initial_marking is not None:
                initial_marking = int(initial_marking.text)
            else:
                initial_marking = 0
            self.places[place.attrib['id']] = Place(place.attrib['id'], initial_marking, index)

        self.transitions = {transition.attrib['id']:Transition(transition.attrib['id'], index) for index, transition in enumerate(root.iter(xmlns + "transition"))}

        for arc in root.iter(xmlns + "arc"):
            source, target = arc.attrib['source'], arc.attrib['target']

            weight = arc.find(xmlns + 'inscription/' + xmlns + 'text')
            if weight is not None:
                weight = int(weight.text)
            else:
                weight = 1

            if source in self.places:
                place, transition = self.places[source], self.transitions[target]
                transition.pre[place] = weight
            else:
                place, transition = self.places[target], self.transitions[source]
                transition.post[place] = weight

    def compute_initial_marking(self):
        """ Compute the initial marking.
        """
        self.initial_marking = [0 for _ in range(len(self.places))]

        for place in self.places.values():
            if place.initial_marking != 0:
                self.initial_marking[place.index] = place.initial_marking

    def compute_incidence_matrix(self):
        """ Compute the incidence matrix.
        """
        self.matrix = [[0 for y in range(len(self.transitions))] for x in range(len(self.places))]
        
        for transition in self.transitions.values():
            for place, weight in transition.pre.items():
                self.matrix[place.index][transition.index] = -weight

            for place, weight in transition.post.items():
                self.matrix[place.index][transition.index] = weight


class Place:
    """
    Place.
    """

    def __init__(self, id, initial_marking, index):
        """ Initializer.
        """
        self.id = id
        self.initial_marking = initial_marking
        self.index = index

    def __str__(self):
        return self.id


class Transition:
    """
    Transition. 
    """

    def __init__(self, id, index):
        """ Initializer.
        """
        self.id = id
        self.index = index

        self.pre = {}
        self.post = {}


if __name__ == "__main__":

    if len(sys.argv) == 1:
        exit("File missing: ./ptnet.py <path_to_file>")

    ptnet = PetriNet(sys.argv[1])
    ptnet.show()
