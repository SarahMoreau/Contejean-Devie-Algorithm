#creer base canonique
def creer_base_canonique(nombre_variables):
  import numpy as np

  base = []
  vecteur = []

  for i in range(0, nombre_variables, 1):
    vecteur_canonique = np.zeros((nombre_variables,1))
    vecteur_canonique[i]=1
    base.append(vecteur_canonique)
    vecteur.append(vecteur_canonique)

  return(vecteur, base)


#associer les valeurs aux vecteurs de la base canonique
def valeurs_base_canonique(systeme, nombre_variables, base):
  import numpy as np

  valeur = []
  valeur_canonique = []

  for i in range(0, nombre_variables, 1):
    produit = np.dot(systeme,base[i])
    valeur.append(produit)
    valeur_canonique.append(produit)

  return(valeur, valeur_canonique)