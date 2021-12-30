
personas= input("Ingresa un nombre: ")
ins = []
while len(ins) < 5 :
    ins.append(personas)
    personas=input("Ingresa un nombre : ")
    if len(ins)== 5 :
        choise=input("desea continuar: ")
        if choise == 0 :
            print("hola")


