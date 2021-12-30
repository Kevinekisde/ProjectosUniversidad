## python programacion orientada a objetos

ingenieros = list()
abogado = list()
otro = list()

class entrevistados():
    Nombre: str()
    Edad: int()
    Sexo : str()
    Profecion: str()
    Sueldo: int()

def __init__(self,Nombre,Edad,Sexo,Profecion,Sueldo):
    self.Nombre= Nombre
    self.Edad = Edad
    self.Sexo = Sexo
    self.Profecion = Profecion
    self.Sueldo = Sueldo

def Registrar_Personas():
    print("ingrese sus datos porfavor")
    E = entrevistados()

    E.Nombre= input("ingrese su nombre:")
    E.Edad= input("ingrese su edad:")
    E.Sexo= input("ingrese su sexo:")
    E.Sueldo= input("ingrese su sueldo:")
    E.Profecion= input("ingrese su profecion:")

    if E.Profecion == ("Ingeniero" or "ingeniero"):
        ingenieros.append(E)
    elif E.Profecion == ("Abogado" or "abogado"):
        abogado.append(E)
    else:
        otro.append(E)
    print ("Desea registrar otra persona?")
    print ("1.Si")
    print ("2.No")
    choise = input("Seleccione una opcion 1/2 : ")
    if choise == 1:
        repeat()
    else:
        print(ingenieros)
        print(abogado)
        print(otro)
    
def repeat():
    return Registrar_Personas()


Registrar_Personas()
