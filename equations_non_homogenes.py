def resoudre_systeme_equations_non_homogenes(systeme, constante):

  from equations_homogenes import resoudre_systeme_equations_homogenes
  from solution_equation_non_homogene import solution_equation_non_homogene


  solution_1 = resoudre_systeme_equations_homogenes(systeme)
  solution_2 = solution_equation_non_homogene(systeme, constante)

  solution_minimale = []

  if solution_2 != [] :
    for i in range(0,len(solution_1), 1):
      for j in range(0, len(solution_1),1):

        solution_minimale.append(solution_1[j] + solution_2[i])
  
  else :
    solution_minimale = solution_2

  nombre_solution = len(solution_minimale)

  print("nombre de solution(s) minimales(s) : ", nombre_solution)

  print("solution(s) minimale(s) du systeme d'équations non homogènes : ", solution_minimale)

  return(solution_minimale)


if __name__ == '__main__':
  constante = [[7],[5]]
  systeme = [[1,2,-9],[1,-5,-2]]
  resoudre_systeme_equations_non_homogenes(systeme,constante)