print("Ejercicio 1 :v")
print()
 
numeros = []
nDatos = int(input("Cuántos números desea registrar? "))
 
for i in range(nDatos):
    N = int(input("Digite el número "))
    numeros.append(N)
 
print("\nLista de números ingresados: ", numeros,"\n")
 
for i in range(len(numeros)-1):
    for j in range(len(numeros) -1):
        if numeros[j] > numeros[j+1]:
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
 
print("Lista ordenada", numeros)
print("El número mayor es: ", numeros[i+1])