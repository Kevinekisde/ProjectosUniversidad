contador=0
mayor=0
menor=100000000000000000000000000000000000000000000000000000000
i=1
suma=0
print("Tiempo canciones de Luis Jara")
while i:
    segundos=int(input("ingresar segundos de canciones de luis jara en numeros enteros:"))
    contador= contador + int(1)
    suma=int(suma) + int(segundos)
    print(f"lleva",{suma},"en total")
    if segundos >= 360:
        contador=contador-1
        print("solo se puede ingresar canciones de 360 segundos el programa calculara los resultados del proceso")
        print(f"lleva",{suma-segundos},"en total")
        suma=suma - segundos
        break
    elif segundos < 0:
        print("el programa no admite cifras negativas se restara la cifra indicada ,y se calculara los resultados del proceso")
        print(f"lleva",{suma-segundos},"en total")
        break
    elif segundos ==0:
        break
    if segundos>mayor:
        mayor=segundos
    else:
        mayor = mayor
    if segundos < menor:
        menor=segundos
    else:
        menor = menor
contador=contador-1
print("proceso terminara de calcular sus resultados")
print("el promedio de los segundos totales es",suma/contador)
print("la cancion de menos segundos fue de:",menor)
print("la cancion de mayor segundos fue de:",mayor)
input("presione enter para salir del programa:")
