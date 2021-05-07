def taille_systeme(systeme):

  nombre_equations = len(systeme)
  nombre_variables = len(systeme[0])
  taille_systeme = (nombre_equations, nombre_variables)
  print("taille système : (nombre equations, nombre variables) = ", taille_systeme)

  return(nombre_equations, nombre_variables)