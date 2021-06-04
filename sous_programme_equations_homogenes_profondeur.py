from ptnet.ptnet import PetriNet
import sys

def taille_systeme(systeme):

  nombre_equations = len(systeme)
  nombre_variables = len(systeme[0])
  taille_systeme = (nombre_equations, nombre_variables)
  print("taille système : (nombre equations, nombre variables) = ", taille_systeme)

  return(nombre_equations, nombre_variables)



def valeur_unitaire(nombre_equations, nombre_variables,systeme):

    import numpy as np

    valeur_unitaire = []
    
    for i in range(0, nombre_variables,1):
        valeur = []
        for j in range(0, nombre_equations,1):
            valeur.append(systeme[j][i])
        valeur_unitaire.append(valeur)

    return(valeur_unitaire)


def memoire_premier_tour(valeur_unitaire):

    from essaie_profondeur import dichotomie

    memoire = ["".join([str(_) for _ in valeur_unitaire[0]])]

    liste = []

    for i in range(1,len(valeur_unitaire),1):
        valeur = "".join([str(_) for _ in valeur_unitaire[i]])

        if dichotomie(memoire,valeur)==False:
            memoire.append(valeur)
            memoire = sorted(memoire)
        else : 
            liste.append(i)

    while liste != []:
        del(valeur_unitaire[liste[0]])
        del (liste[0])
        if liste != []:
            for i in range(0, len(liste),1):
                liste[i]=liste[i]-1

    memoire = sorted(memoire)
    return(memoire, valeur_unitaire)


def dichotomie(memoire, valeur):
    a = 0
    b = len(memoire) - 1
    while a <= b:
        m = (a + b) // 2
        if memoire[m] == valeur:
            # on a trouvé v
            return True
        elif memoire[m] < valeur:
            a = m + 1
        else:
            b = m - 1
    # on a a > b
    return False




def trouver_solution(memoire, valeur_unitaire, nombre_equations, nombre_variables):

    import numpy as np
    from sous_programme_equations_homogenes_profondeur import dichotomie

    
    etape = 0
    parcours = {}
    vecteur = np.zeros((nombre_variables,1))
    solution_minimale = []

    i=0
    j=1

    produit_scalaire = np.dot(valeur_unitaire[i],valeur_unitaire[j])
    limite = 0

    while produit_scalaire >= 0 and limite == 0:
        j+=1
        if i != j:
            if j < len(valeur_unitaire) :
                produit_scalaire = np.dot(valeur_unitaire[i], valeur_unitaire[j])

            elif j == len(valeur_unitaire)-1 and i < len(valeur_unitaire)-1:
                i+=1
                j=0
                if i != j :
                    if i < len(valeur_unitaire) :
                        produit_scalaire = np.dot(valeur_unitaire[i], valeur_unitaire[j])
        if i==j==len(valeur_unitaire)-1:
            limite = 1

    if produit_scalaire >= 0 :
        print("le systeme homogène n'a pas de solution minimale")
        return(solution_minimale)
    
    else : 
        parcours[etape]=[]
        for k in range(0,i,1):
            parcours[etape].append(1)
        parcours[etape].append(0)

        etape +=1
        parcours[etape]=[]
        for k in range(0,j,1):
            parcours[etape].append(1)
        parcours[etape].append(0)

        vecteur[i]+=1
        vecteur[j]+=1

        valeur = np.array(valeur_unitaire[i]) + np.array(valeur_unitaire[j])

        while etape >=0:

            indice = 0
            for k in range(0, nombre_equations,1):
                if valeur[k]==0:
                    indice +=1



            if indice == nombre_equations:
                
                indice = 0
                stocker = vecteur.copy()
                
                solution_minimale.append(stocker)
                print("solution", solution_minimale)
                
                taille = len(parcours.get(etape))
                valeur = np.array(valeur) - np.array(valeur_unitaire[taille-1])
                vecteur[taille-1]-=1

                while taille == len(valeur_unitaire) and etape >= 0:
                
                    etape -= 1
                    taille = len(parcours.get(etape))
                    valeur = np.array(valeur) - np.array(valeur_unitaire[taille-1])
                    vecteur[taille-1]-=1


                if taille == len(valeur_unitaire):
                    print('les solutions minimale du système homogène sont : ', solution_minimale)
                    return(solution_minimale)

                else :            
                    indice_bis = len(valeur_unitaire) - taille
                    l = indice_bis
                    produit_scalaire = np.dot(valeur, valeur_unitaire[l])

                    while produit_scalaire >= 0 :
                        l+=1
                        if l <len(valeur_unitaire):
                            produit_scalaire = np.dot(valeur, valeur_unitaire[l])

                        else : 
                            etape -=1
                            taille = len(parcours.get(etape))
                            valeur = np.array(valeur) - np.array(valeur_unitaire[taille-1])
                            vecteur[taille-1]-=1


                            while taille == len(valeur_unitaire) and etape >=0:
                                etape -=1
                                taille = len(parcours.get(etape))
                                valeur = np.array(valeur) - np.array(valeur_unitaire[taille-1])
                                vecteur[taille-1]-=1
                        
                            if taille == len(valeur_unitaire):
                                print("les solutions minimales du système homogène sont : ", solution_minimale)
                                return(solution_minimale)

                            else :
                                indice_bis = len(valeur_unitaire) - taille
                                l = indice_bis
                                produit_scalaire = np.dot(valeur, valeur_unitaire[l])
                
                    for k in range(indice_bis,l,1):
                        parcours[etape].append(1)
                    parcours[etape].append(0)

                    vecteur[l]+=1

                    valeur = np.array(valeur) + np.array(valeur_unitaire[l])
            


            else : 
                valeur_memoire = "".join([str(_) for _ in valeur])
            
                if dichotomie(memoire, valeur_memoire)==True:

                    taille = len(parcours.get(etape))
                    valeur = np.array(valeur) - np.array(valeur_unitaire[taille-1])
                    vecteur[taille-1]-=1

                    while taille == len(valeur_unitaire) and etape > 0:
                    
                        etape -= 1
                        taille = len(parcours.get(etape))
                        valeur = np.array(valeur) - np.array(valeur_unitaire[taille-1])
                        vecteur[taille-1]-=1

                    if taille == len(valeur_unitaire):
                        print('les solutions minimale du système homogène sont : ', solution_minimale)
                        return(solution_minimale)

                    else :            
                        indice_bis = len(valeur_unitaire) - taille
                        l = indice_bis
                        produit_scalaire = np.dot(valeur, valeur_unitaire[l])

                        while produit_scalaire >= 0 :
                            l+=1
                            if l <len(valeur_unitaire):
                                produit_scalaire = np.dot(valeur, valeur_unitaire[l])

                            else: 
                                if etape >0:
                                    etape -=1
                                    
                                    taille = len(parcours.get(etape))
                                    valeur = np.array(valeur) - np.array(valeur_unitaire[taille-1])
                                    vecteur[taille-1]-=1
                                    while taille == len(valeur_unitaire) and etape >=0:
                                        etape -=1
                                        taille = len(parcours.get(etape))
                                        valeur = np.array(valeur) - np.array(valeur_unitaire[taille-1])
                                        vecteur[taille-1]-=1
                                else : 
                                    print("les solutions minimales du système homogenes sont : ", solution_minimale)
                                    return(solution_minimale)
                        
                                if taille == len(valeur_unitaire):
                                    print("les solutions minimales du système homogène sont : ", solution_minimale)
                                    return(solution_minimale)

                                else :
                                    indice_bis = len(valeur_unitaire) - taille
                                    l = indice_bis
                                    produit_scalaire = np.dot(valeur, valeur_unitaire[l])

                        for k in range(indice_bis,l,1):
                            parcours[etape].append(1)
                        parcours[etape].append(0)

                        vecteur[l]+=1

                        valeur = np.array(valeur) + np.array(valeur_unitaire[l])


                else : 

                    memoire.append(valeur_memoire)
                    memoire = sorted(memoire)

                    i = 0
                    produit_scalaire = np.dot(valeur, valeur_unitaire[i])

                    while produit_scalaire >=0 and i < len(valeur_unitaire)-1:
                        i+=1
                        produit_scalaire = np.dot(valeur, valeur_unitaire[i])
                    
                    if produit_scalaire >=0 : 
                        etape +=1
                        parcours[etape]=[]
                        for j in range(0, len(valeur_unitaire),1):
                            parcours[etape].append(1)


                        while produit_scalaire >= 0 and etape >0:

                            etape-=1   
                            taille = len(parcours.get(etape))
                            valeur = np.array(valeur) - np.array(valeur_unitaire[taille-1])
                            vecteur[taille-1]-=1

                            while taille == len(valeur_unitaire) and etape >=0:
                                etape -=1
                                taille = len(parcours.get(etape))
                                valeur = np.array(valeur) - np.array(valeur_unitaire[taille-1])
                                vecteur[taille-1]-=1


                        if taille == len(valeur_unitaire):
                            print("les solutions minimales du système homogène sont : ", solution_minimale)
                        else :
                                indice_bis = len(valeur_unitaire) - taille
                                l = indice_bis
                                produit_scalaire = np.dot(valeur, valeur_unitaire[l])
                                

                                etape+=1
                                for k in range(indice_bis,l,1):
                                    parcours[etape].append(1)
                                parcours[etape].append(0)

                                vecteur[l]+=1

                                valeur = np.array(valeur) + np.array(valeur_unitaire[l])
                    else : 
                        etape +=1
                        parcours[etape]=[]
                        for k in range(0,i,1):
                            parcours[etape].append(1)
                        parcours[etape].append(0)

                        vecteur[i]+=1

                        valeur = np.array(valeur) + np.array(valeur_unitaire[i])

    return(solution_minimale)


#rajouter comparaison avec solution minimale





if __name__ == '__main__':
  
  
  '''
  if len(sys.argv) < 2:
    print("Error: missing input Petri net")
    exit(1)

  path_ptnet = sys.argv[1]
  ptnet = PetriNet(path_ptnet)
  matrice = ptnet.matrix
  '''
  systeme = [[-1,1,3],[-1,3,-2]]
  nombre_equations, nombre_variables = taille_systeme(systeme)
  valeur_unitaire = valeur_unitaire(nombre_equations, nombre_variables, systeme)
  memoire, valeur_unitaire = memoire_premier_tour(valeur_unitaire)
  trouver_solution(memoire, valeur_unitaire, nombre_equations, nombre_variables)
 