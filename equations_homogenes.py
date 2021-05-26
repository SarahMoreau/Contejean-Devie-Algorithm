
from ptnet.ptnet import PetriNet
import sys
import numpy as np

def resoudre_systeme_equations_homogenes (systeme):
  
  from sous_programmes_equations_homogenes import taille_systeme, creer_base_canonique, valeurs_base_canonique, memoire_premier_tour, memoire_tour_suivant, calculer_vecteurs, calculer_valeurs, existence_solution, verif_solution_minimale, verif_valeurs, mise_a_jour_listes, calculer_vecteurs_bis
  
  solution_minimale = []

  nombre_equations, nombre_variables = taille_systeme(systeme)
  nulle = np.zeros((nombre_equations,1))
  vecteur, base = creer_base_canonique(nombre_variables)
  

  valeur, valeur_canonique = valeurs_base_canonique(systeme, nombre_variables, base)
  
  memoire,valeur,vecteur = memoire_premier_tour(valeur, nombre_equations, vecteur)
  
  vecteurs_bis = calculer_vecteurs(valeur, valeur_canonique, base, vecteur, nombre_variables)
  
  valeur_bis = calculer_valeurs(vecteurs_bis, systeme)

  solution_minimale_ajoutee, valeur_minimale_ajoutee, valeur_bis, vecteurs_bis = existence_solution(valeur_bis,nombre_equations,vecteurs_bis,nulle)

  solution_minimale = verif_solution_minimale(solution_minimale,solution_minimale_ajoutee, valeur_minimale_ajoutee, nombre_variables)

  valeur_bis, vecteurs_bis = verif_valeurs(solution_minimale, valeur_bis, nombre_variables, vecteurs_bis)

  memoire,valeur_bis,vecteurs_bis = memoire_tour_suivant(memoire, valeur_bis, nombre_equations, vecteurs_bis)

  valeur, vecteur, valeur_bis, vecteurs_bis =  mise_a_jour_listes (valeur, vecteur, valeur_bis, vecteurs_bis)
  i = 0
  while valeur != []:
    vecteurs_bis = calculer_vecteurs_bis(valeur, valeur_canonique, vecteur, base, nombre_variables)

    valeur_bis = calculer_valeurs(vecteurs_bis, systeme)

    solution_minimale_ajoutee, valeur_minimale_ajoutee, valeur_bis,vecteurs_bis = existence_solution(valeur_bis,nombre_equations,vecteurs_bis,nulle)

    solution_minimale = verif_solution_minimale(solution_minimale,solution_minimale_ajoutee, valeur_minimale_ajoutee, nombre_variables)

    valeur_bis, vecteurs_bis = verif_valeurs(solution_minimale, valeur_bis, nombre_variables, vecteurs_bis)

    memoire,valeur_bis,vecteurs_bis = memoire_tour_suivant(memoire, valeur_bis, nombre_equations, vecteurs_bis)

    valeur, vecteur, valeur_bis, vecteurs_bis =  mise_a_jour_listes (valeur, vecteur, valeur_bis, vecteurs_bis)
    i += 1
    print(i)
    print(len(valeur))
  nombre_solution = len(solution_minimale)

  print("nombre de solution(s) minimales(s) du système homogène : ", nombre_solution)

  print("solution(s) minimale(s) du système d'équations homogènes : ", solution_minimale)
  
  return(solution_minimale)


if __name__ == '__main__':
  
  if len(sys.argv) < 2:
    print("Error: missing input Petri net")
    exit(1)

  path_ptnet = sys.argv[1]
  ptnet = PetriNet(path_ptnet)
  matrice = ptnet.matrix
  systeme = np.transpose(matrice)

  #print(ptnet.matrix)
  #print(ptnet.initial_marking)
  resoudre_systeme_equations_homogenes(systeme)

  #ptnet.show()

  '''systeme = [[1,1,-3],[1,-5,-2]]
  resoudre_systeme_equations_homogenes(systeme)'''
  