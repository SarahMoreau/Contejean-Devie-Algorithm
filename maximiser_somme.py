def maximiser_somme(systeme,constante):
    from equations_non_homogenes import resoudre_systeme_equations_non_homogenes
    systeme_fini, solution_non_homogene_final, solution_homogene_final = resoudre_systeme_equations_non_homogenes(systeme,constante)

    if systeme_fini != 0:
        somme = []
        for i in range(0, len(solution_non_homogene_final),1):
            somme.append(sum(solution_non_homogene_final[i]))
        liste_somme=[]
        for j in range(0, len(solution_non_homogene_final),1):
            liste_somme.append([j,somme[j]])

        for etape in range(0,len(liste_somme)-1,1):
            imax=liste_somme[etape][0]
            maxi = liste_somme[etape][1]

            for k in range(etape+1, len(liste_somme)):
                if liste_somme[k][1]>maxi:
                    imax,maxi = liste_somme[k][0], liste_somme[k][1]
                    liste_somme[k]=[liste_somme[etape][0],liste_somme[etape][1]]
                    liste_somme[etape]=[imax,maxi]
        
        indice = [liste_somme[0][0]]
        indice_max = [indice[0]]
        for i in range(1,len(somme),1):
            if liste_somme[0][1]==liste_somme[i][1] :
                indice_max.append(liste_somme[i][0])

        solution_max = []
        for i in range(0,len(solution_non_homogene_final),1):
            if i in indice_max:
                solution_max.append(solution_non_homogene_final[i])
        print("les solutions qui maximisent la somme sont : ", solution_max)
    return()


if __name__ == '__main__':
  constante = [[3],[3]]
  systeme = [[1,1,-1],[1,0,2]]
  maximiser_somme(systeme,constante)