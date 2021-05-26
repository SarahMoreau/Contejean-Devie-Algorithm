def taille_systeme(systeme):

  nombre_equations = len(systeme)
  nombre_variables = len(systeme[0])
  taille_systeme = (nombre_equations, nombre_variables)
  print("taille système : (nombre equations, nombre variables) = ", taille_systeme)

  return(nombre_equations, nombre_variables)

#creer base canonique
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


#associer les valeurs aux vecteurs de la base canonique
def valeurs_base_canonique(systeme, nombre_variables, base):
  import numpy as np

  valeur = []
  valeur_canonique = []

  for i in range(0, nombre_variables, 1):
    produit = np.dot(systeme,base[i])
    valeur.append(produit)
    valeur_canonique.append(produit)

  return(valeur, valeur_canonique)


def memoire_premier_tour(valeur, nombre_equations, vecteur):

  memoire = [valeur[0]]
  liste = []
  for i in range(0, len(valeur),1):
    for j in range(0, len(memoire),1):
      if (valeur[i] == memoire[j]).all():
        indice = nombre_equations
      else : 
        indice = 0
    if indice == nombre_equations :
      liste.append(i)
    else :
      memoire.append(valeur[i])
  while liste != []:
    del(valeur[liste[0]])
    del(vecteur[liste[0]])
    del(liste[0])
    if liste != []:
      for i in range(0, len(liste),1):
        liste[i]=liste[i]-1
    
  return(memoire,valeur,vecteur)

#calculer les vecteurs du deuxieme tour
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
              dernier_vecteur = vecteurs_bis[-1]
               
              if (dernier_vecteur==vecteurs_bis[k]).all():
                indice = nombre_variables
              else :
                indice = 0
           
              if indice == nombre_variables and len(vecteurs_bis)==nombre_vecteurs:
                del(vecteurs_bis[-1])
            
  return(vecteurs_bis)


#associer les valeurs aux vecteurs bis
def calculer_valeurs(vecteurs_bis, systeme):
  import numpy as np

  valeur_bis = []
  for i in range(0, len(vecteurs_bis), 1):
    produit = np.dot(systeme,vecteurs_bis[i])
    valeur_bis.append(produit)
  
  return (valeur_bis)

  #verifier s'il y a une solution minimale
def existence_solution(valeur_bis,nombre_equations,vecteurs_bis,nulle):
  import numpy as np
  liste = []
  valeur_minimale_ajoutee = None
  
  solution_minimale_ajoutee = []
  
  for j in range(0, len(valeur_bis),1):
    if (valeur_bis[j]==nulle).all():
        indice = nombre_equations
    else :
      indice = 0
    valeur_minimale_ajoutee = 0

    if indice == nombre_equations:
      solution_minimale_ajoutee.append(vecteurs_bis[j])
      liste.append(j)
      valeur_minimale_ajoutee = valeur_minimale_ajoutee +1
  while liste !=[]:
    del(valeur_bis[liste[0]])
    del(vecteurs_bis[liste[0]])
    del(liste[0])
    if liste != []:
      for i in range(0, len(liste),1):
        liste[i]=liste[i]-1

  return(solution_minimale_ajoutee, valeur_minimale_ajoutee,valeur_bis,vecteurs_bis)


#verifier qu'on garde bien uniquement les solutions minimales
def verif_solution_minimale(solution_minimale,solution_minimale_ajoutee, valeur_minimale_ajoutee, nombre_variables):

  if len(solution_minimale)>1 and valeur_minimale_ajoutee != 0:
    for i in range(0, len(solution_minimale_ajoutee), 1):
      for j in range(0, len(solution_minimale),1):
        if i != j :
          if (solution_minimale_ajoutee[i]>=solution_minimale[j]).all():
            indice = nombre_variables
          else :
            indice = 0

      if indice != nombre_variables :
        solution_minimale.append(solution_minimale_ajoutee[i])

  taille = len(solution_minimale_ajoutee)
  del(solution_minimale_ajoutee[0:taille])
  return(solution_minimale)


#verifier que les valeurs calculees ne sont pas superieures aux solutions minimales deja trouvees
def verif_valeurs(solution_minimale, valeur_bis, nombre_variables, vecteurs_bis):
  liste = []
  if len(solution_minimale) != 0:
    for i in range(0, len(solution_minimale), 1):
      for j in range(0, len(valeur_bis), 1):
        if (vecteurs_bis[j]<=solution_minimale[i]).all():
          indice = nombre_variables
        else :
          indice = 0
        if indice == nombre_variables :
          liste.append(j)
      while liste !=[]:
        del(valeur_bis[liste[0]])
        del(vecteurs_bis[liste[0]])
        del(liste[0])
        if liste != []:
          for i in range(0, len(liste),1):
            liste[i]=liste[i]-1
  
  return(valeur_bis, vecteurs_bis)


  #garder en memoire toutes les valeurs calculees
def memoire_tour_suivant(memoire, valeur_bis, nombre_equations, vecteurs_bis):
  
  liste = []
  for i in range(0, len(valeur_bis),1):
    for j in range(0, len(memoire),1):
      if (valeur_bis[i] == memoire[j]).all():
        indice = nombre_equations
      else : 
        indice = 0
    if indice == nombre_equations :
      liste.append(i)
    else :
      memoire.append(valeur_bis[i])
  while liste != []:
    del(valeur_bis[liste[0]])
    del(vecteurs_bis[liste[0]])
    del(liste[0])
    if liste != []:
      for i in range(0, len(liste),1):
        liste[i]=liste[i]-1
  return(memoire, valeur_bis,vecteurs_bis)


#mettre a jour les listes de vecteur et de valeur
def mise_a_jour_listes (valeur, vecteur, valeur_bis, vecteurs_bis):
  taille = len(valeur)
  del(valeur[0:taille])
  del(vecteur[0:taille])
  valeur = valeur_bis.copy()
  vecteur = vecteurs_bis.copy()

  taille1 = len(valeur_bis)
  del(valeur_bis[0:taille1])
  del(vecteurs_bis[0:taille1])

  return(valeur, vecteur, valeur_bis, vecteurs_bis)


def calculer_vecteurs_bis(valeur, valeur_canonique, vecteur, base, nombre_variables):
  import numpy as np

  taille = len(valeur)
  vecteurs_bis = []
  for i in range(0, taille, 1):
    for j in range(0, len(valeur_canonique),1):
       
      produit_scalaire = np.vdot(valeur[i],valeur_canonique[j])
      if produit_scalaire<0:
        nouveau_vecteur = vecteur[i]+base[j]
        vecteurs_bis.append(nouveau_vecteur)
            
        if len(vecteurs_bis)>1:
          nombre_vecteurs = len(vecteurs_bis)
          for k in range(0, len(vecteurs_bis)-1, 1):
            dernier_vecteur = vecteurs_bis[-1]
            if (dernier_vecteur==vecteurs_bis[k]).all():
              indice = nombre_variables
            else :
              indice = 0

            if indice == nombre_variables and len(vecteurs_bis)==nombre_vecteurs:
              del(vecteurs_bis[-1])

  return(vecteurs_bis)