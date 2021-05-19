def resoudre_systeme(systeme, constante,signe):
    from equations_homogenes import resoudre_systeme_equations_homogenes
    from equations_non_homogenes import resoudre_systeme_equations_non_homogenes
    from inequations_homogenes import resoudre_systeme_inequations_homogenes
    from inequations_non_homogenes import resoudre_systeme_inequations_non_homogenes

    print("0 : =, 1 : <=, 2 : <, 3 : >=, 4 : >")

    nombre_equations = len(systeme)
    nombre_variables = len(systeme[0])

    systeme_equation = []
    systeme_inequation = []
    signe_inequation = []
    constante_equation = []
    constante_inequation = []

    for i in range(0, nombre_equations,1):
        if signe[i]==[0]:
            systeme_equation.append(systeme[i])
            constante_equation.append(constante[i])
        else :
            systeme_inequation.append(systeme[i])
            signe_inequation.append(signe[i])
            constante_inequation.append(constante[i])

    systeme_equation_homogene = []
    systeme_equations_non_homogene = []
    constante_equation_non_homogene = []

    for i in range(0, len(systeme_equation),1):
        if constante_equation[i] == [0]:
            systeme_equation_homogene.append(systeme_equation[i])
        else :
            systeme_equations_non_homogene.append(systeme_equation[i])
            constante_equation_non_homogene.append(constante_equation[i])

    systeme_inequation_homogene = []
    systeme_inequation_non_homogene = []
    constante_inequation_non_homogene = []
    signe_inequation_homogene = []
    signe_inequation_non_homogene = []

    for i in range(0, len(systeme_inequation),1):
        if constante_inequation == [0]:
            systeme_inequation_homogene.append(systeme_inequation[i])
            signe_inequation_homogene.append(signe_inequation[i])
        else :
            systeme_inequation_non_homogene.append(systeme_inequation[i])
            constante_inequation_non_homogene.append(constante_inequation[i])
            signe_inequation_non_homogene.append(signe_inequation[i])
    
    if systeme_equation_homogene != []:
        solution_1 = resoudre_systeme_equations_homogenes(systeme_equation_homogene)
    else:
        solution_1 = []
    
    if systeme_equations_non_homogene != []:
        systeme_fini, solution_2, solution_homogene_final = resoudre_systeme_equations_non_homogenes(systeme_equations_non_homogene, constante_equation_non_homogene)
    
    else :
        solution_2 = []

    if systeme_inequation_homogene != [] :
        solution_3 = resoudre_systeme_inequations_homogenes(systeme_inequation_homogene,signe_inequation_homogene)
    
    else :
        solution_3 = []

    if systeme_inequation_non_homogene != []:
        systeme_fini1, solution_4, solution_homogene_final1 = resoudre_systeme_inequations_non_homogenes(systeme_inequation_non_homogene, constante_inequation_non_homogene, signe_inequation_non_homogene)

    else :
        solution_4 = []
    solution_systeme = []


    if systeme_equation_homogene != []:
        for i in range(0, len(solution_1),1):
            if solution_1[i] in solution_2:
                if solution_1[i] in solution_3:
                    if solution_1[i] in solution_4:
                        solution_systeme.append(solution_1[i])
    elif systeme_equations_non_homogene != []:
        for i in range(0, len(solution_2),1):
            if solution_2[i] in solution_1:
                if solution_2[i] in solution_3:
                    if solution_2[i] in solution_4:
                        solution_systeme.append(solution_2[i])
    elif systeme_inequation_homogene != []:
        for i in range(0, len(solution_3),1):
            if solution_3[i] in solution_2:
                if solution_3[i] in solution_1:
                    if solution_3[i] in solution_4:
                        solution_systeme.append(solution_3[i])
    elif systeme_inequation_non_homogene != []:
        for i in range(0, len(solution_4),1):
            if solution_4[i] in solution_2:
                if solution_4[i] in solution_3:
                    if solution_4[i] in solution_1:
                        solution_systeme.append(solution_4[i])
    print("l'ensemble des solutions du systeme est : ", solution_systeme)
    return()

if __name__ == '__main__':
  
  systeme = [[1,1,-3],[1,-5,-2]]
  constante = [[-1],[2]]
  signe = [[0],[1]]
  resoudre_systeme(systeme, constante, signe)
