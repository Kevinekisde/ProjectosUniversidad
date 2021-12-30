def multiplicacion(a,b):
    return a * b
def multiplica(x,y):
    return x * y
def resta(x,y):
    return x - y
def suma(x,y):
    return x + y
print("                                              ganancias de una empresa")
z=int(input("ingrese el costo fijo de su empresa:"))
x=int(input("ingresar ventas de 100 dolares:"))
y=int(input("ingresar ventas de 25 dolares:"))
print("calculando")

costo_fijo=int(4000)
resultado_a=int(x)*int(100)
resultado_b=int(y)*int(25)
resultado_c= costo_fijo + resultado_b
ganancias= resultado_a - resultado_c
print("las ganancias totales de tu empresa son:")
print(ganancias)
if ganancias > 1000 :
 print("felicidades las ganancias estan arriba de los 1000 dolares se le entregara un bono al jefe de produccion")
elif 1000 > ganancias >= 500 :
 print("sus ganancias estan entre 1000 y 500 se enviara correo de alerta al jefe de produccion")
elif ganancias < 500 :
 print("sus ganancias estan por debajo de 500 el jefe de produccion sera despedido")

input("presione enter para salir")
