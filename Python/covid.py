
texto='INFORME COVID19 POR MHB'
print(texto)
dias= int(input("ingrese el numero de dias que quiere registrar:"))
suma= 0
x=1
y=True
mayor=0
menor=100000000000000000000000000000000000000000000000000000000
while x<=dias:
    datos=int(input("escriba el reporte diario de contagiados: "))
    suma= int(suma)+int(datos)
    print(f"el numero de contagiados que lleva es de",{suma} )
    x=x+1
    if datos>mayor:
        mayor=datos
    else:
        mayor = mayor
    if datos < menor:
        menor=datos
    else:
        menor = menor
final=suma
promedio= final/dias
print("los pacientes total entre los dias mencionados son de:" + str(final))
print("el promedio de pacientes total es de :",promedio)
print("el dia que mas pacientes se registraron fueron:",mayor,"paciente/s")
print("el dia que menos pacientes se registraron fueron:",menor,"paciente/s")
z=input("presione enter para terminar el programa: ")

