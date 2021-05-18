#definit le nombre d'équations et de variable du système de départ
def taille_systeme(systeme):

  nombre_equations = len(systeme)
  nombre_variables = len(systeme[0])

  return(nombre_equations, nombre_variables)


#transforme le système non homogène en un système homogène en rajoutant une variable
def transformer_systeme(systeme,constante,nombre_equations, nombre_variables):

  for i in range (0, nombre_equations, 1):
    systeme[i].insert(0,-constante[i][0])
    constante[i]=0

  nombre_variables = nombre_variables +1
  
  return(nombre_variables,systeme,constante)


#creation de la base canonique 
def creer_base_canonique(nombre_variables):
  import numpy as np

  base = []
  vecteur = []

  for i in range(0, nombre_variables, 1):
    vecteur_canonique = np.zeros((nombre_variables,1))
    vecteur_canonique[i]=1
    base.append(vecteur_canonique)
    vecteur.append(vecteur_canonique)

  return(vecteur, base)


#calcul des valeurs associées aux vecteurs de la base canonique
def valeurs_base_canonique(systeme, nombre_variables, base):
  import numpy as np

  valeur = []
  valeur_canonique = []

  for i in range(0, nombre_variables, 1):
    produit = np.dot(systeme,base[i])
    valeur.append(produit)
    valeur_canonique.append(produit)

  return(valeur, valeur_canonique)


#garder en mémoire les valeurs calculées au premier tour
def memoire_premier_tour(valeur, nombre_variables, nombre_equations, vecteur):

  memoire = [valeur[0]]
  liste = []
  for i in range(1, len(valeur),1):
    for j in range(0, len(memoire), 1):
      indice = 0
      for k in range(0, nombre_equations, 1):
        
        if valeur[i][k]==memoire[j][k]:
          indice = indice +1
      
    if indice == nombre_equations:
        liste.append(i)

    else :
      memoire.append(valeur[i])

  for l in range(0, len(liste),1):
      del(valeur[liste[l]])
      del(vecteur[liste[l]])

  return(memoire,valeur,vecteur)


#calcule les vecteurs du deuxième tour 
def calculer_vecteurs(valeur, valeur_canonique, base, vecteur, nombre_variables):
  import numpy as np

  taille = len(valeur)
  vecteurs_bis = []
  for i in range(0, taille, 1):
    for j in range(0, len(valeur_canonique),1):
      if i != j:
        produit_scalaire = np.vdot(valeur[i],valeur_canonique[j])
        if produit_scalaire<0:
          nouveau_vecteur = vecteur[i]+base[j]
          vecteurs_bis.append(nouveau_vecteur)

          if len(vecteurs_bis)>1:
            nombre_vecteurs = len(vecteurs_bis)
            for k in range(0, len(vecteurs_bis)-1, 1):
              indice = 0
              
              for l in range(0, nombre_variables, 1):
                dernier_vecteur = vecteurs_bis[-1]
               
                if dernier_vecteur[l]==vecteurs_bis[k][l]:
                  indice = indice+1
           
              if indice == nombre_variables and len(vecteurs_bis)==nombre_vecteurs:
                del(vecteurs_bis[-1])
  return(vecteurs_bis)
  

#calcule les valeurs associées aux vecteurs du deuxième tour
def calculer_valeurs(vecteurs_bis, systeme):
  import numpy as np

  valeur_bis = []
  for i in range(0, len(vecteurs_bis), 1):
    produit = np.dot(systeme,vecteurs_bis[i])
    valeur_bis.append(produit)

  return (valeur_bis)


#vérifie s'il y a une solution dans les valeurs calculées
def existence_solution(valeur_bis,nombre_equations,vecteurs_bis,solution_minimale):
  
  liste = []

  for j in range(0, len(valeur_bis),1):
    indice = 0
    for k in range(0, nombre_equations,1):
      if valeur_bis[j][k] <= 0:
        indice = indice + 1

    if indice == nombre_equations:
      solution_minimale.append(vecteurs_bis[j])
      liste.append(j)
  print(valeur_bis)
  print(liste)
  for i in range (0, len(liste), 1):
    del (valeur_bis[liste[i]])
    del(vecteurs_bis[liste[i]])
    if i in liste :
        for j in range(1, len(liste),1):
            liste[j]=liste[j]-1
      
  return(solution_minimale,valeur_bis,vecteurs_bis)


#reparti les solutions entre les solutions minimales homogenes et non homogenes
def repartir_solution_minimale(solution_minimale, solution_minimale_homogene, solution_minimale_non_homogene):


  valeur_ajoutee_homogene = 0
  valeur_ajoutee_non_homogene = 0

  if solution_minimale != []:
    for i in range(0, len(solution_minimale),1):
      if solution_minimale[i][0]==1:
        solution_minimale_non_homogene.append(solution_minimale[i])
        valeur_ajoutee_non_homogene +=1

      else :
        solution_minimale_homogene.append(solution_minimale[i])
        valeur_ajoutee_homogene += 1

    for j in range(0, len(solution_minimale), 1):
      del(solution_minimale[0])

  return(solution_minimale, solution_minimale_homogene, solution_minimale_non_homogene, valeur_ajoutee_homogene, valeur_ajoutee_non_homogene)



#verifier qu'on garde bien uniquement les solutions minimales
def verif_solution_minimale(solution_minimale_homogene,solution_minimale_non_homogene, valeur_ajoutee_homogene, valeur_ajoutee_non_homogene, nombre_variables):

  if len(solution_minimale_homogene)>1 and valeur_ajoutee_homogene != 0:
    for i in range(0, len(solution_minimale_homogene), 1):
      for j in range(0, len(solution_minimale_homogene),1):
        if i != j :
          indice = 0
          for k in range(0, nombre_variables, 1):
            if solution_minimale_homogene[i][k] >= solution_minimale_homogene[j][k]:
              indice = indice +1
      if indice == nombre_variables:
        del(solution_minimale_homogene[i])


  if len(solution_minimale_non_homogene)>1 and valeur_ajoutee_non_homogene != 0:
    for i in range(0, len(solution_minimale_non_homogene), 1):
      for j in range(0, len(solution_minimale_non_homogene),1):
        if i != j :
          indice = 0
          for k in range(0, nombre_variables, 1):
            if solution_minimale_non_homogene[i][k] >= solution_minimale_non_homogene[j][k]:
              indice = indice +1
      if indice == nombre_variables:
        del(solution_minimale_non_homogene[i])

  return(solution_minimale_homogene, solution_minimale_non_homogene)


#verifier que les valeurs calculees ne sont pas superieures aux solutions minimales deja trouvees
def verif_valeurs(solution_minimale_homogene,solution_minimale_non_homogene, valeur_bis, nombre_variables, vecteurs_bis):

  liste1 = []
  liste2 = []
  if len(solution_minimale_homogene) != 0:
    for i in range(0, len(solution_minimale_homogene), 1):
      for j in range(0, len(vecteurs_bis), 1):
        indice = 0
        for k in range(0, nombre_variables, 1):
          if vecteurs_bis[j][0]==0 :

            if vecteurs_bis[j][k]<=solution_minimale_homogene[i][k]:
              indice = indice + 1
          if indice == nombre_variables :
            liste1.append(j)
      
      for l in range(0, len(liste1), 1):
          del(valeur_bis[liste1[l]])
          del(vecteurs_bis[liste1[l]])
  

  if len(solution_minimale_non_homogene) != 0:
    
    for i in range(0, len(solution_minimale_non_homogene), 1):
      for j in range(0, len(vecteurs_bis), 1):
        indice = 0
        for k in range(0, nombre_variables, 1):
          if vecteurs_bis[j][0]==1 :
            
            if vecteurs_bis[j][k]<=solution_minimale_non_homogene[i][k]:
              indice = indice + 1
          if indice == nombre_variables :
            liste2.append(j)

      for l in range(0, len(liste2), 1):
          del(valeur_bis[liste2[l]])
          del(vecteurs_bis[liste2[l]])
  
  return(valeur_bis, vecteurs_bis)


#garder en memoire toutes les valeurs calculees
def memoire_tour_suivant(memoire, valeur_bis, nombre_equations, vecteurs_bis):
  liste = []
  for i in range(0, len(valeur_bis),1):
    for j in range(0, len(memoire), 1):
      indice = 0
      
      for k in range(0, nombre_equations, 1):
        
        if valeur_bis[i][k]==memoire[j][k]:
          indice = indice +1
      
    if indice == nombre_equations:
      liste.append(i)

    else :
      memoire.append(valeur_bis[i])

  for i in range (0, len(liste), 1):
    del (valeur_bis[liste[i]])
    del(vecteurs_bis[liste[i]])
  
  return(memoire)


#mettre a jour les listes de vecteur et de valeur
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


#calculer les vecteurs de chaque tour 
def calculer_vecteurs_bis(valeur, valeur_canonique, vecteur, base, nombre_variables):
  import numpy as np

  taille = len(valeur)
  vecteurs_bis = []
  for i in range(0, taille, 1):
    for j in range(1, len(valeur_canonique),1):
       
      produit_scalaire = np.vdot(valeur[i],valeur_canonique[j])
      if produit_scalaire<0:
        nouveau_vecteur = vecteur[i]+base[j]
        vecteurs_bis.append(nouveau_vecteur)
            
        if len(vecteurs_bis)>1:
          nombre_vecteurs = len(vecteurs_bis)
          for k in range(0, len(vecteurs_bis)-1, 1):
            indice = 0
              
            for l in range(0, nombre_variables, 1):
              dernier_vecteur = vecteurs_bis[-1]
               
              if dernier_vecteur[l]==vecteurs_bis[k][l]:
                indice = indice+1
           
            if indice == nombre_variables and len(vecteurs_bis)==nombre_vecteurs:
              del(vecteurs_bis[-1])


    for i in range(0, taille, 1):
      if vecteur[i][0]==0:
        produit_scalaire = np.vdot(valeur[i], valeur_canonique[0])

        if produit_scalaire<0:
          nouveau_vecteur = vecteur[i]+base[0]
          vecteurs_bis.append(nouveau_vecteur)


          if len(vecteurs_bis)>1:
            nombre_vecteurs = len(vecteurs_bis)
            for k in range(0, len(vecteurs_bis)-1, 1):
              indice = 0
              
              for l in range(0, nombre_variables, 1):
                dernier_vecteur = vecteurs_bis[-1]
               
                if dernier_vecteur[l]==vecteurs_bis[k][l]:
                  indice = indice+1
           
              if indice == nombre_variables and len(vecteurs_bis)==nombre_vecteurs:
                del(vecteurs_bis[-1])

  return(vecteurs_bis)