print("Bienvenido al cajero")
x=input("presione enter para empezar")
a=int(input("ingrese su rut sin comas ni guion:"))
if a>10000000:
 print("bienvenido a su cuenta")
else:
 input("adios porfiado")
 quit()

 
print("selecciona la operacion que desea utilizar")
print("1.retirar dinero")
print("2.transferir dinero")
print("3.salir")
choise = input("elije una operacion(1/2/3):")
if choise == "1":
  q=int(input("ingrese la cantidad a retirar:"))
  print("procesando....")
  print("la operacion fue exitosa")
  print("desea hacer otra operacion")
  print("si(1),no(2)")
  choise = input("elije una operacion(1/2):")
  if choise == "1":
      print("selecciona la operacion que desea utilizar")
      print("1.retirar dinero")
      print("2.transferir dinero")
      print("3.salir")
      choise = input("elije una operacion(1/2/3):")
      if choise == "2":
          e=int(input("digite el numero de cuenta ala que va a transferir:"))
          r=int(input("digite la cantidad a transferir:"))
          print("procesando.....")
          print("la operacion fue exitosa")
          print("desea hacer otra operacion")
          print("si(1),no(2)")
          choise = input ("elije una operacion (1/2):")
          if choise == "1":
              print("selecciona la operacion que desea utilizar")
              print("1.retirar dinero")
              print("2.transferir dinero")
              print("3.salir")
              if choise == "3":
                  input("adios")
              elif choise == "1":
                  input("el tiempo se agoto")
              elif choise == "2":
                  input("el tiempo se agoto")
              
  elif choise == "2":
      input("adios")
          
elif choise == "2" :
    print("seleccione el tipo de cuenta a transeferir")
    print("1.cuenta visa")
    print("2.cuenta rut")
    choise = input("elije un tipo de cuenta(1/2)")
    if choise == "1":
        e=int(input("digite el numero de cuenta ala que va a transferir:"))
        r=int(input("digite la cantidad a transferir"))
        print("procesando.....")
        print("la operacion fue exitosa")
        print("desea hacer otra operacion")
        print("si(1),no(2)")
        choise = input("elije una operacion(1/2):")
        if choise == "1":
            print("selecciona la operacion que desea utilizar")
            print("1.retirar dinero")
            print("2.transferir dinero")
            print("3.salir")
            choise = input("elije una operacion(1/2/3):")
            if choise == "1":
                q=int(input("ingrese la cantidad a retirar"))
                print("procesando....")
                print("la operacion fue exitosa")
                print("desea hacer otra operacion")
                print("si(1),no(2)")
                choise = input("elije una operacion(1/2/):")
                if choise == "1":
                    print("selecciona la operacion que desea utilizar")
                    print("1.retirar dinero")
                    print("2.transferir dinero")
                    print("3.salir")
                    choise = input("elije una operacion(1/2/3):")
                    if choise == "3":
                        input("adios")
                    elif choise == "2":
                        input("el tiempo se agoto")
                    elif choise == "1":
                        input("el tiempo se agoto")
        
    elif choise == "2":
        e=int(input("digite el numero de cuenta ala que va a transferir:"))
        r=int(input("digite la cantidad a transferir"))
        print("procesando.....")
        print("la operacion fue exitosa")
        print("desea hacer otra operacion")
        print("si(1),no(2)")
        choise = input("elije una operacion(1/2):")
        if choise == "1":
            print("selecciona la operacion que desea utilizar")
            print("1.retirar dinero")
            print("2.transferir dinero")
            print("3.salir")
            choise = input("elije una operacion(1/2/3):")
            if choise == "1":
                q=int(input("ingrese la cantidad a retirar"))
                print("procesando....")
                print("la operacion fue exitosa")
                print("desea hacer otra operacion")
                print("si(1),no(2)")
                choise = input("elije una operacion(1/2/):")
                if choise == "1":
                    print("selecciona la operacion que desea utilizar")
                    print("1.retirar dinero")
                    print("2.transferir dinero")
                    print("3.salir")
                    choise = input("elije una operacion(1/2/3):")
                    if choise == "3":
                        input("adios")
                    elif choise == "2":
                        input("el tiempo se agoto")
                    elif choise == "1":
                        input("el tiempo se agoto")
        elif choise == "2":
            input("adios")
            
        
elif choise == "3":
    input("adios")