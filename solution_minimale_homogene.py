#verifier s'il y a une solution minimale
def existence_solution(valeur_bis,nombre_equations,vecteurs_bis):

  solution_minimale = []
  valeur_minimale_ajoutee = None

  for j in range(0, len(valeur_bis),1):
    indice = 0
    for k in range(0, nombre_equations,1):
      if valeur_bis[j][k] == 0:
        indice = indice + 1

    valeur_minimale_ajoutee = 0

    if indice == nombre_equations:
      solution_minimale.append(vecteurs_bis[j])
      del(valeur_bis[j])
      del(vecteurs_bis[j])
      valeur_minimale_ajoutee = valeur_minimale_ajoutee +1

  return(solution_minimale, valeur_minimale_ajoutee)


#verifier qu'on garde bien uniquement les solutions minimales
def verif_solution_minimale(solution_minimale, valeur_minimale_ajoutee, nombre_variables):

  if len(solution_minimale)>1 and valeur_minimale_ajoutee != 0:
    for i in range(0, len(solution_minimale), 1):
      for j in range(0, len(solution_minimale),1):
        if i != j :
          indice = 0
          for k in range(0, nombre_variables, 1):
            if solution_minimale[i][k] >= solution_minimale[j][k]:
              indice = indice +1
      if indice == nombre_variables:
        del(solution_minimale[i])

  return(solution_minimale)


#verifier que les valeurs calculees ne sont pas superieures aux solutions minimales deja trouvees
def verif_valeurs(solution_minimale, valeur_bis, nombre_variables, vecteurs_bis):

  if len(solution_minimale) != 0:
    for i in range(0, len(solution_minimale), 1):
      for j in range(0, len(valeur_bis), 1):
        indice = 0
        for k in range(0, nombre_variables, 1):
          if valeur_bis[j][k]<=solution_minimale[i][k]:
            indice = indice + 1
        if indice == nombre_variables :
          del(valeur_bis[j])
          del(vecteurs_bis[j])
  
  return(valeur_bis, vecteurs_bis)