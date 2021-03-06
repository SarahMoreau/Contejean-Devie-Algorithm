def resoudre_systeme_inequations_homogenes (systeme,signe):
  
  from sous_programmes_inequations_homogenes import taille_systeme, creer_base_canonique, valeurs_base_canonique, memoire_premier_tour, memoire_tour_suivant, calculer_vecteurs, calculer_valeurs, existence_solution, verif_solution_minimale, mise_a_jour_listes, calculer_vecteurs_bis, existence_solution_premier_tour

  print("1 : <=, 2 : <, 3 : >=, 4 : >")

  nombre_equations, nombre_variables = taille_systeme(systeme)

  vecteur, base = creer_base_canonique(nombre_variables)

  valeur, valeur_canonique = valeurs_base_canonique(systeme, nombre_variables, base)

  solution_minimale, valeur_minimale_ajoutee, valeur,vecteur = existence_solution_premier_tour(valeur, nombre_equations,vecteur,signe)

  solution_minimale = verif_solution_minimale(nombre_equations,systeme, solution_minimale, valeur_minimale_ajoutee, nombre_variables)

  memoire, valeur,vecteur = memoire_premier_tour(valeur, nombre_equations, vecteur)

  vecteurs_bis = calculer_vecteurs(valeur, valeur_canonique, base, vecteur, nombre_variables)

  valeur_bis = calculer_valeurs(vecteurs_bis, systeme)

  solution_minimale, valeur_minimale_ajoutee, valeur_bis, vecteurs_bis = existence_solution(valeur_bis,nombre_equations,vecteurs_bis, solution_minimale,signe)

  solution_minimale = verif_solution_minimale(nombre_equations,systeme, solution_minimale, valeur_minimale_ajoutee, nombre_variables)

  memoire = memoire_tour_suivant(memoire, valeur_bis, nombre_equations, vecteurs_bis)

  valeur, vecteur, valeur_bis, vecteurs_bis =  mise_a_jour_listes (valeur, vecteur, valeur_bis, vecteurs_bis)

  while valeur != []:
    vecteurs_bis = calculer_vecteurs_bis(valeur, valeur_canonique, vecteur, base, nombre_variables)

    valeur_bis = calculer_valeurs(vecteurs_bis, systeme)

    solution_minimale, valeur_minimale_ajoutee, valeur_bis, vecteurs_bis = existence_solution(valeur_bis,nombre_equations,vecteurs_bis, solution_minimale,signe)

    solution_minimale = verif_solution_minimale(nombre_equations,systeme, solution_minimale, valeur_minimale_ajoutee, nombre_variables)

    memoire = memoire_tour_suivant(memoire, valeur_bis, nombre_equations, vecteurs_bis)

    valeur, vecteur, valeur_bis, vecteurs_bis =  mise_a_jour_listes (valeur, vecteur, valeur_bis, vecteurs_bis)
  
  nombre_solution = len(solution_minimale)

  print("nombre de solution(s) minimales(s) du syst??me d'in??quations homog??nes : ", nombre_solution)

  print("solution(s) minimale(s) du syst??me d'in??quations homog??nes : ", solution_minimale)
  
  return(solution_minimale)


if __name__ == '__main__':
  
  systeme = [[1,-1,]]
  signe = [[1]]
  resoudre_systeme_inequations_homogenes(systeme, signe)