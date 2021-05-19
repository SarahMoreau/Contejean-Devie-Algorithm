def resoudre_systeme_inequations_non_homogenes (systeme,constante,signe):
  
  from sous_programmes_inequations_non_homogene import taille_systeme, transformer_systeme, creer_base_canonique, valeurs_base_canonique, memoire_premier_tour, calculer_vecteurs, calculer_valeurs, existence_solution, repartir_solution_minimale, verif_solution_minimale, memoire_tour_suivant, mise_a_jour_listes, calculer_vecteurs_bis   

  print("1 : <=, 2 : <, 3 : >=, 4 : >")

  solution_minimale = []
  solution_minimale_homogene = []
  solution_minimale_non_homogene = []

  nombre_equations, nombre_variables = taille_systeme(systeme)

  nombre_variables, systeme, constante = transformer_systeme(systeme,constante,nombre_equations, nombre_variables)

  vecteur, base = creer_base_canonique(nombre_variables)

  valeur, valeur_canonique = valeurs_base_canonique(systeme,nombre_variables,base)

  solution_minimale, valeur, vecteur = existence_solution(valeur,nombre_equations,vecteur,solution_minimale,signe)

  solution_minimale, solution_minimale_homogene, solution_minimale_non_homogene, valeur_ajoutee_homogene, valeur_ajoutee_non_homogene = repartir_solution_minimale(solution_minimale, solution_minimale_homogene, solution_minimale_non_homogene)

  solution_minimale_homogene, solution_minimale_non_homogene = verif_solution_minimale(solution_minimale_homogene,solution_minimale_non_homogene, valeur_ajoutee_homogene, valeur_ajoutee_non_homogene, nombre_variables)

  memoire, valeur, vecteur = memoire_premier_tour(valeur, nombre_variables, nombre_equations, vecteur)

  vecteurs_bis = calculer_vecteurs(valeur, valeur_canonique, base, vecteur, nombre_variables)

  valeur_bis = calculer_valeurs(vecteurs_bis, systeme)

  solution_minimale, valeur_bis, vecteurs_bis = existence_solution(valeur_bis,nombre_equations,vecteurs_bis,solution_minimale,signe)

  solution_minimale, solution_minimale_homogene, solution_minimale_non_homogene, valeur_ajoutee_homogene, valeur_ajoutee_non_homogene = repartir_solution_minimale(solution_minimale, solution_minimale_homogene, solution_minimale_non_homogene)


  solution_minimale_homogene, solution_minimale_non_homogene = verif_solution_minimale(solution_minimale_homogene,solution_minimale_non_homogene, valeur_ajoutee_homogene, valeur_ajoutee_non_homogene, nombre_variables)

  memoire = memoire_tour_suivant(memoire, valeur_bis, nombre_equations, vecteurs_bis)

  valeur, vecteur, valeur_bis, vecteurs_bis = mise_a_jour_listes (valeur, vecteur, valeur_bis, vecteurs_bis)

  while valeur != []:

    vecteurs_bis = calculer_vecteurs_bis(valeur, valeur_canonique, vecteur, base, nombre_variables)

    valeur_bis = calculer_valeurs(vecteurs_bis, systeme)

    solution_minimale, valeur_bis, vecteurs_bis = existence_solution(valeur_bis,nombre_equations,vecteurs_bis,solution_minimale,signe)

    solution_minimale, solution_minimale_homogene, solution_minimale_non_homogene, valeur_ajoutee_homogene, valeur_ajoutee_non_homogene = repartir_solution_minimale(solution_minimale, solution_minimale_homogene, solution_minimale_non_homogene)

    
    solution_minimale_homogene, solution_minimale_non_homogene = verif_solution_minimale(solution_minimale_homogene,solution_minimale_non_homogene, valeur_ajoutee_homogene, valeur_ajoutee_non_homogene, nombre_variables)

    memoire = memoire_tour_suivant(memoire, valeur_bis, nombre_equations, vecteurs_bis)

    valeur, vecteur, valeur_bis, vecteurs_bis = mise_a_jour_listes (valeur, vecteur, valeur_bis, vecteurs_bis)

  solution_non_homogene_final=[]
  solution_homogene_final = []

  systeme_fini = 0
  
  for i in range(0, len(solution_minimale_non_homogene), 1):
    valeur = []
    for j in range(1, nombre_variables,1):
      valeur.append(solution_minimale_non_homogene[i][j])
    solution_non_homogene_final.append(valeur)

  for j in range(0, len(solution_minimale_homogene), 1):
    valeur = []
    for k in range(1, nombre_variables,1):
      valeur.append(solution_minimale_homogene[j][k])
    solution_homogene_final.append(valeur) 

  if solution_non_homogene_final == []:
    print("il n'y a pas de solution")
  else :
    if solution_homogene_final != []:
      print("les solutions du système non homogène sont : ", solution_non_homogene_final)
      print("de plus, il existe une infinité de solution car on peut rajouter ou enlever ", solution_homogene_final, "tant que la combinaison linéaire reste strictement positive")

    else : 
      print("l'ensemble des solutions du système non homogène est fini : ", solution_non_homogene_final)
      systeme_fini += 1

  return(systeme_fini, solution_non_homogene_final, solution_homogene_final)



if __name__ == '__main__':
  
  systeme = [[1,1,-3],[1,-5,-2]]
  constante = [[-1],[2]]
  signe = [[1],[1]]
  resoudre_systeme_inequations_non_homogenes(systeme,constante,signe)