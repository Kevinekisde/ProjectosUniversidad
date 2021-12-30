#Algoritmos llamadas:
#llamada:impuesto+impuesto+impuesto * minuto
#impuesto: 15% = 1.15
#llamada total= llamada * impuesto

def suma(x, y):
   return x + y

def resta(x, y):
   return x - y

def multiplica(x, y):
   return x * y

def divide(x, y):
   return x / y
print("                       llamadas chantaCa")
print("bienvenido al sistema de pago de llamadas chantaCa")
print("seleccione el el dia que realizo su llamada")
print("1.dia habil")
print("2.domingo")

choice = input("seleccione una opcion(1/2):")
if choice == "1" :
   print("muy bien la llamada se realizo en un dia habil")
   print("en que horario fue realizado")
   print("1.matutino")
   print("2.vespertino")
   choice = input("seleccione una opcion(1/2):")

   if choice == "1":
      minutos=int(input("cuanto duro su llamada: "))
      if minutos <= 5:
          impuesto1 = float(1.15)
          preciofinal= 1.00 * minutos * impuesto1
          print("el precio de su llamada es de:")
          print(preciofinal)
          input("presione enter para finalizar")
      if 8 >= minutos >=6:
         impuesto1= float(1.15)
         precio= 1.00 + 0.8 * minutos
         preciofinal2= precio * impuesto1
         print("el precio de su llamada es de: ")
         print("{:.2f}".format(preciofinal2))
         input("presione enter para finalizar")
      if 10 >= minutos > 8 :
         impuesto1 = float(1.15)
         precio2= 1.00 + 0.8 +0.7 * minutos
         preciofinal3= precio2 * impuesto1
         print("el precio de su llamada es de : ")
         print("{:.2f}".format(preciofinal3))
         input("presione enter para finalizar")
      if minutos >= 11:
         impuesto1 = float(1.15)
         precio3= 1.00 + 0.8 + 0.7+ 0.5 * minutos
         preciofinal4= precio3 * impuesto1
         print("el precio de su llamada es de : ")
         print("{:.2f}".format(preciofinal4))
         input("presione enter para finalizar")
            
            
   elif choice == "2":
      minutos=int(input("cuanto duro su llamada:"))
      if minutos <= 5:
          impuesto1 = float(1.10)
          preciofinal= 1.00 * minutos * impuesto1
          print("el precio de su llamada es de:")
          print(preciofinal)
          input("presione enter para finalizar")
      if 8 >= minutos >=6:
         impuesto1= float(1.10)
         precio= 1.00 + 0.8 * minutos
         preciofinal2= precio * impuesto1
         print("el precio de su llamada es de: ")
         print("{:.2f}".format(preciofinal2))
         input("presione enter para finalizar")
      if 10 >= minutos > 8 :
         impuesto1 = float(1.10)
         precio2= 1.00 + 0.8 +0.7 * minutos
         preciofinal3= precio2 * impuesto1
         print("el precio de su llamada es de : ")
         print("{:.2f}".format(preciofinal3))
         input("presione enter para finalizar")
      if minutos >= 11:
         impuesto1 = float(1.10)
         precio3= 1.00 + 0.8 + 0.7+ 0.5 * minutos
         preciofinal4= precio3 * impuesto1
         print("el precio de su llamada es de : ")
         print("{:.2f}".format(preciofinal4))
         input("presione enter para finalizar")

elif choice == "2" :
   ("su llamada fue realizada un dia domingo")
   minutos=int(input("cuanto duro su llamada: "))
   if minutos <= 5:
      impuesto1 = float(1.03)
      preciofinal= 1.00 * minutos * impuesto1
      print("el precio de su llamada es de:")
      print(preciofinal)
      input("presione enter para finalizar")
   if 8 >= minutos >=6:
      impuesto1= float(1.03)
      precio= 1.00 + 0.8 * minutos
      preciofinal2= precio * impuesto1
      print("el precio de su llamada es de: ")
      print("{:.2f}".format(preciofinal2))
      input("presione enter para finalizar")
         
   if 10 >= minutos > 8 :
      impuesto1 = float(1.03)
      precio2= 1.00 + 0.8 +0.7 * minutos
      preciofinal3= precio2 * impuesto1
      print("el precio de su llamada es de : ")
      print("{:.2f}".format(preciofinal3))
      input("presione enter para finalizar")
   if minutos >= 11:
      impuesto1 = float(1.03)
      precio3= 1.00 + 0.8 + 0.7+ 0.5 * minutos
      preciofinal4= precio3 * impuesto1
      print("el precio de su llamada es de : ")
      print("{:.2f}".format(preciofinal4))
      input("presione enter para finalizar")