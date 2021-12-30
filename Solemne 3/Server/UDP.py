from tkinter import *
import random
import time
import socket



def sensor():
    
    while True:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        dato=(random.randrange(0,100,10))
        dato=str(dato)
        dato1=dato.encode()
        s.sendto(dato1,("192.168.18.3",2000))
        print(dato1)
        time.sleep(2)
        s.close()


ventana=Tk()
ventana.title("Enviar Datos")
ventana.geometry("500x600")
ventana.config(bg="gray24")
L1=Label(ventana,text="Envios De Datos",font=("Courier",35,"underline","bold"),bg="gray24").pack()
B1=Button(ventana,text="Enviar datos sensor",command=sensor, bg="light slate blue",width=20,height=15)
B1.place(x=170,y=200)

ventana.mainloop()
