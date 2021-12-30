print("ahorros de un año")
ahorro= 0 
mes= 1
while(mes<=12):
    dinero=input("ingrese cantidad de dinero ahorrado:")
    ahorro= int(ahorro)+int(dinero)
    print(f"en este mes lleva",{ahorro} )
    mes= mes+1
final=ahorro
print("el dinero ahorrado en total es de :" + str(final))