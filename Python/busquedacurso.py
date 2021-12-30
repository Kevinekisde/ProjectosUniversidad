def busqueda():
    busca=input("introduce la busqueda:")
    print("resultado: ",curso.get(busca,"no encontramos nada"))

#activad 8 introduccion ala programacion    
#palabras claves nombre,profesor,alumnos,numero.
print("informacion curso 1°A de un colegio ")
curso={'nombre':'1°A','profesor': 'matias vidal', 'alumnos': '39','numero':'20'}
busca=input("introduce la busqueda:")
print("resultado: ",curso.get(busca,"no encontramos nada"))
busqueda()
busqueda()
busqueda()
busqueda()