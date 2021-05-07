def memoire_premier_tour(valeur, nombre_variables, nombre_equations, base):

  memoire = [valeur[0]]

  for i in range(1, nombre_variables,1):
    for j in range(0, len(memoire), 1):
      indice = 0
      for k in range(0, nombre_equations, 1):
        
        if valeur[i][k]==memoire[j][k]:
          indice = indice +1
      
    if indice == nombre_equations:
        del(valeur[i])
        del(base[i])

    else :
      memoire.append(valeur[i])

  return(memoire)



#garder en memoire toutes les valeurs calculees
def memoire_tour_suivant(memoire, valeur_bis, nombre_equations, vecteurs_bis):

  for i in range(0, len(valeur_bis),1):
    for j in range(0, len(memoire), 1):
      indice = 0
      for k in range(0, nombre_equations, 1):
        
        if valeur_bis[i][k]==memoire[j][k]:
          indice = indice +1
      
    if indice == nombre_equations:
      del(valeur_bis[i])
      del(vecteurs_bis[i])

    else :
      memoire.append(valeur_bis[i])
  
  return(memoire)