print("aumento de un numero")
numero1=int(input("numero incial:"))
numerofinal=int(input("numero final:"))
numerodeaumento=int(input("numero de aumento:"))
for i in range(numero1,numerofinal,numerodeaumento):
    print(i-1)
    if i > numerofinal:
        break

print("fin")