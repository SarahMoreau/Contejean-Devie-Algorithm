def resolution_systemes_equations (systeme, constante):
    from equations_homogenes import resoudre_systeme_equations_homogenes
    from equations_non_homogenes import resoudre_systeme_equations_non_homogenes

    indice = 0
    for i in range(0, len(constante), 1):
      if  constante[i]== [0]:
        indice = indice +1 

    if indice == len(constante):
        solution_minimale = resoudre_systeme_equations_homogenes(systeme, constante)
    else :
        solution_minimale = resoudre_systeme_equations_non_homogenes(systeme, constante)

    return(solution_minimale)

if __name__ == '__main__':
  constante = [[0],[0]]
  systeme = [[1,2,-9],[1,-5,-2]]
  resolution_systemes_equations(systeme,constante)