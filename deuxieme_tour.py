#calculer les vecteurs du deuxieme tour
def calculer_vecteurs(valeur, valeur_canonique, base, vecteur, nombre_variables):
  import numpy as np

  taille = len(valeur)
  vecteurs_bis = []
  for i in range(0, taille, 1):
    for j in range(0, len(valeur_canonique),1):
      if i != j:
        produit_scalaire = np.vdot(valeur[i],valeur_canonique[j])
        if produit_scalaire<0:
          nouveau_vecteur = vecteur[i]+base[j]
          vecteurs_bis.append(nouveau_vecteur)

          if len(vecteurs_bis)>1:
            nombre_vecteurs = len(vecteurs_bis)
            for k in range(0, len(vecteurs_bis)-1, 1):
              indice = 0
              
              for l in range(0, nombre_variables, 1):
                dernier_vecteur = vecteurs_bis[-1]
               
                if dernier_vecteur[l]==vecteurs_bis[k][l]:
                  indice = indice+1
           
              if indice == nombre_variables and len(vecteurs_bis)==nombre_vecteurs:
                del(vecteurs_bis[-1])
            
  return(vecteurs_bis)


#associer les valeurs aux vecteurs bis
def calculer_valeurs(vecteurs_bis, systeme):
  import numpy as np

  valeur_bis = []
  for i in range(0, len(vecteurs_bis), 1):
    produit = np.dot(systeme,vecteurs_bis[i])
    valeur_bis.append(produit)
  
  return (valeur_bis)