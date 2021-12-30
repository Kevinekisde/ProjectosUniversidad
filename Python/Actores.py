class actor:
    nombre=""
    edad=int()
    nacionalidad=""

    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad

class pelicula(actor):
    titulo=""
    duracion=int()
    año=int()


    def __init__(self,titulo,duracion,año):
        self.titulo=titulo
        self.duracion=duracion
        self.año=año
        self.actores=[]
        # self.nombre=nombre
        # self.edad=edad
        # self.nacionalidad=nacionalidad
    
    def lista_actores():
        actores=["Vin Diesel",53,"Estadounidense","Paul Walker",40,"Estadounidense",
        "Michelle Rodriguez",42,"Estadounidense","Jordana Brewster",40,"Panameña",
        "Tyrese Gibson",41,"Estadounidense"
        ]
        print(actores)


    def agregaActor(self):
        actores=["Vin Diesel",53,"Estadounidense","Paul Walker",40,"Estadounidense",
        "Michelle Rodriguez",42,"Estadounidense","Jordana Brewster",40,"Panameña",
        "Tyrese Gibson",41,"Estadounidense"
        ]
        nuevo1=actor("Chris Ludacris Bridges",43,"Estadounidense")
        actores.append(nuevo1.nombre)
        actores.append(nuevo1.edad)
        actores.append(nuevo1.nacionalidad)
        nuevo2=actor("Devon Edwenna Aoki",38,"Estadounidense")
        actores.append(nuevo2.nombre)
        actores.append(nuevo2.edad)
        actores.append(nuevo2.nacionalidad)

        print(actores)
        

        
        


# for i in range (3):
lista=[]
pelicula1=pelicula("Rapidos y furiosos 1",107,2001)
pelicula2=pelicula("Rapidos y furiosos 2",108,2003)
pelicula3=pelicula("Rapidos y furiosos 3",105,2006)
lista.append(pelicula1)  #### se agrega pelicula 1
for elemento in range(len(lista)):  ###### como se tiene un solo elemento mostra solo pelicula 1 por ahora junto co sus actores
    print(pelicula1.titulo,pelicula1.duracion,pelicula1.año) ## imprime info de pelicula
    pelicula.lista_actores()### imprime los actores
    pelicula2=pelicula("Rapidos y furiosos 2",108,2003)### creamos la 2 pelicula
    lista.append(pelicula2) ### la agreagamos a la lista
    del(lista[1]) ## borramos la pelicula 1 de la lista para que no se duplique la pelicula 2
    for elemento in range(len(lista)):
        print(pelicula2.titulo,pelicula2.duracion,pelicula2.año)
        pelicula.agregaActor("")
        del(lista[0])
        lista.append(pelicula3)
        for elemento in range(len(lista)):
            pelicula.agregaActor("")
            print(pelicula3.titulo,pelicula3.duracion,pelicula3.año)
            nuevo3=pelicula.agregaActor("")
            