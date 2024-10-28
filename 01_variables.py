"""variables"""
curso = "2SMR"
nombre_curso = "PYTHON"
alumno = "Lucía_Li"
nota_HLC = 9
nota_SOR = 6
nota_SI = 7
nota_media = (nota_HLC+nota_SOR+nota_SI)/3
publicado = True
print(curso,nombre_curso)
print("Nombre Alumno:", alumno, "Nota Media:",
      #round sirve para redondear un número
      round(nota_media,2), "Publicado:", publicado)