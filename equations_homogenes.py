def resoudre_systeme_equations_homogenes (systeme):
  
  from systeme import taille_systeme
  from base_canonique import creer_base_canonique, valeurs_base_canonique
  from memoire import memoire_premier_tour, memoire_tour_suivant
  from deuxieme_tour import calculer_vecteurs, calculer_valeurs
  from solution_minimale_homogene import existence_solution, verif_solution_minimale, verif_valeurs
  from mise_a_jour import mise_a_jour_listes
  from nieme_tour import calculer_vecteurs_bis


  nombre_equations, nombre_variables = taille_systeme(systeme)

  vecteur, base = creer_base_canonique(nombre_variables)

  valeur, valeur_canonique = valeurs_base_canonique(systeme, nombre_variables, base)

  memoire = memoire_premier_tour(valeur, nombre_variables, nombre_equations, base)

  vecteurs_bis = calculer_vecteurs(valeur, valeur_canonique, base, vecteur, nombre_variables)

  valeur_bis = calculer_valeurs(vecteurs_bis, systeme)

  solution_minimale, valeur_minimale_ajoutee = existence_solution(valeur_bis,nombre_equations,vecteurs_bis)

  solution_minimale = verif_solution_minimale(solution_minimale, valeur_minimale_ajoutee, nombre_variables)

  valeur_bis, vecteurs_bis = verif_valeurs(solution_minimale, valeur_bis, nombre_variables, vecteurs_bis)

  memoire = memoire_tour_suivant(memoire, valeur_bis, nombre_equations, vecteurs_bis)

  valeur, vecteur, valeur_bis, vecteurs_bis =  mise_a_jour_listes (valeur, vecteur, valeur_bis, vecteurs_bis)

  while valeur != []:
    vecteurs_bis = calculer_vecteurs_bis(valeur, valeur_canonique, vecteur, base, nombre_variables)

    valeur_bis = calculer_valeurs(vecteurs_bis, systeme)

    solution_minimale, valeur_minimale_ajoutee = existence_solution(valeur_bis,nombre_equations,vecteurs_bis)

    solution_minimale = verif_solution_minimale(solution_minimale, valeur_minimale_ajoutee, nombre_variables)

    valeur_bis, vecteurs_bis = verif_valeurs(solution_minimale, valeur_bis, nombre_variables, vecteurs_bis)

    memoire = memoire_tour_suivant(memoire, valeur_bis, nombre_equations, vecteurs_bis)

    valeur, vecteur, valeur_bis, vecteurs_bis =  mise_a_jour_listes (valeur, vecteur, valeur_bis, vecteurs_bis)
  
  nombre_solution = len(solution_minimale)

  print("nombre de solution(s) minimales(s) du système homogène : ", nombre_solution)

  print("solution(s) minimale(s) du système homogène : ", solution_minimale)
  
  return(solution_minimale)


if __name__ == '__main__':
  
  systeme = [[1,1,-3],[1,-5,-2]]
  resoudre_systeme_equations_homogenes(systeme)