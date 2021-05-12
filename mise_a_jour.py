#mettre a jour les listes de vecteurs et de valeurs
def mise_a_jour_listes (valeur, vecteur, valeur_bis, vecteurs_bis):

  for i in range(0,len(valeur),1):
    del(valeur[0])
    del(vecteur[0])
  valeur = valeur_bis.copy()
  vecteur = vecteurs_bis.copy()

  for i in range(0, len(valeur_bis),1):
    del(valeur_bis[0])
    del(vecteurs_bis[0])  

  return(valeur, vecteur, valeur_bis, vecteurs_bis)