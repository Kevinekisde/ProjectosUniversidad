#Programa Maquina de Cafe
#Kevin Leiva
#Matias Gaete
##### Universidad Autononoma De Chile
#### INTRODUCCION ALA PROGRAMACION
#### PROFESOR:Matias Ambrosio Vidal
################################################################################

########################################################## Bucle de Maquina DE CAFE #####################################################################################

### funciones y definiciones globales ###

import sys ############## Funcion integrada para finalizar el programa en algunas opciones ########

dinero=0

cafes=[] ########Lista para almacenar tipos de cafe comprados ###################

vasos=0 ########### Cuenta los vasos de cafe/s se hicieron en total ##################

total=0 ############ Suma todos los cafes comprados y muestra el total #####################

############# Esta funcion es para simular un proceso de compra como el analizar saldo ################################################################
def compra():
    print("Su compra se ha realizado efectivamente")
    print(".................................................")
    print("Su pedido de cafe express se hara en un instante")
    print(".................................................")
    print("Espere porfavor")
    print("...................................................")
    print("Su pedido se ha hecho correctamente")
    print("...................................................")
    print("Gracias por su compra")
#### Esta funcion genera una respuesta segun falta de dinero , eleccion de cafe , resta saldo,agrega los tipos de cafe comprados a una lista y crea un bucle ###################
def fdinero():
    global vasos
    global dinero
    global monedas
    global total
    while dinero < 100 :
        print("#################################################################")
        print("Con el saldo ingresado no le alcanzara para un cafe")
        print("Tu saldo es de",dinero)
        print("El cafe minimo es de 100$")
        monedas=int(input("Ingrese otra moneda:"))
        print("#################################################################")
        dinero= int(monedas) +int(dinero)
        print("El saldo ingresado es de: ",dinero,"$")
        print("#################################################################")

    print("Selecione el cafe que desea tomar: ")
    print("#####################################################################")
    print("1.Expresso 100$")
    print("2.Americanno 200$")
    print("3.Seleccionar mas de un cafe")
    print("4.salir")
    print("#####################################################################")

    choise = input("Elija una opcion (1/2/3): ")
    if choise =="1":
        print("#################################################################")
        print("Ha seleccionado un cafe expresso: ")
        choise= input("presione 1 para confirmar o 0 para volver atras: ")
        if choise == "1":
            dinero= dinero-100
            total= total + 100
            print("Se ha descontado 100 $ de su saldo ingresado")
            compra()
            cafes.append('Cafe expresso 100$')
            vasos= vasos+1
            print("#################################################################")
        if choise == "0":
            fdinero()
        elif choise > "1" :
            print("el caracter ingresado no es valido volvera ala seleccion de cafe")
            fdinero()


    elif choise == "2":
        while dinero < 200:
            print("#############################################################")
            print("Su dinero no es suficiente para este cafe")
            print("Ingrese mas dinero para este cafe")
            print("El dinero que lleva es de: ",dinero)
            monedas=int(input("Ingrese otra moneda:"))
            dinero= int(monedas) +int(dinero)
            print("#############################################################")
        print("#################################################################")
        print("Ha seleccionado un cafe americano")
        choise= input("presione 1 para confirmar o 0 para volver atras: ")
        if choise == "1":
            print("Se ha descontado 200 $ de su saldo")
            print("#############################################################")
            dinero= dinero-200
            total= total + 200
            cafes.append('Cafe americanno 200$')
            vasos=vasos + 1
            compra()
            print("#################################################################")
        elif choise == "0":
            fdinero()
        elif choise > "1":
            print("el caracter ingresado no es valido volvera ala seleccion de cafe")
            fdinero()


    elif choise == "3":
        print("#####################################################################")
        CantNumeros=int(input("Cuantos cafes deseas realizar?\n"))
        for i in range(1,CantNumeros+1):
            print("###################################################################")
            print("Ingrese el ",i,"ªcafe")
            print("ingrese el numero 1 para cafe expresso y 2 para cafe americano:")
            print("##################################################################")
            Numero=(input())
            while Numero > "2":
                print("El numero ingresado no es valido, intentelo denuevo:")
                Numero=(input())
            if Numero == "1":
                while dinero < 100:
                    print("###########################################################")
                    print("Su dinero no es suficiente")
                    print("Ingrese mas dinero para este cafe")
                    print("El dinero que lleva es de: ",dinero)
                    monedas=int(input("Ingrese otra moneda:"))
                    dinero= int(monedas) +int(dinero)
                print("se ha ingresado un cafe Expresso a la lista de cafes")
                dinero= dinero-100
                total= total + 100
                cafes.append('Cafe expresso 100$')
                vasos= vasos+1

            elif Numero == "2":
                while dinero < 200:
                    print("#############################################################")
                    print("Su dinero no es suficiente para este cafe")
                    print("Ingrese mas dinero para este cafe")
                    print("El dinero que lleva es de: ",dinero)

                    monedas=int(input("Ingrese otra moneda:"))
                    dinero= int(monedas) +int(dinero)
                print("se ha ingresado un cafe Americanno a la lista de cafes")
                dinero= dinero-200
                total= total + 200
                cafes.append('Cafe americanno 200$')
                vasos=vasos + 1

    elif choise == "4":
        print("Su vuelto sera de:",dinero,"$")
        print("Adios")
        print("Cualquier reclamo made un sms al 555")
        print("#######################n##############################################")
        input("presione una Enter para salir:")
        sys.exit(1)


    elif choise > "4":
        print("el caracter ingresado no es valido")
        fdinero()

    otro()
######################################## Esta funcion es para preguntarle al cliente si necesita otro cafe ###########################################################
def otro():
    print("##########################################################################")
    print("Desea realizar otro pedido:")
    print("Su saldo restante es de:",dinero,"$")
    print("#####################################################################")
    print("1.si")
    print("2.no (salir)")
    print("#####################################################################")
    opcion= input("Seleccione una opcion (1/2): ")
    while opcion == "1":
        fdinero()
    if opcion == "2":
        print("Se imprimira su boleta:")
        for sabor in cafes:
            print(sabor)
        print("El total de su pedido es: ",total,"$")
        print("Su vuelto sera de:",dinero,"$")
        print("Adios")
        int(input("Presione una tecla para salir"))
        sys.exit(1)
    elif opcion > "2":
        print("El caracter ingrsado no es valido ,se imprimira su boleta")
        for sabor in cafes:
            print(sabor)
        print("El total de su pedido es: ",total,"$")
        print("Su vuelto sera de:",dinero,"$")
        print("Adios")
        int(input("Presione una tecla para salir"))
        sys.exit(1)

#//////////////////////////////////////////////////////////////////// codigo inicial ////////////////////////////////////////////////////////////////////////////////////////#
print("#########################################################################")
print("                         Bienvenido a Su Maquina de Cafe")
print("#########################################################################")
print("Esta maquina vende cafes de 100 y 200 $")
dinero=int(input("Ingrese cuanto dinero a insertado: "))
fdinero()