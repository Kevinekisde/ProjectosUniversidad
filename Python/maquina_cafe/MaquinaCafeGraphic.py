#Maquina de cafe. Codigo basado en una simulacion de una maquina que vende cafes
##Matias Gaete
##Kevin Leiva
##introduccion a la programacion
##solemne 2
##Julio 2020

from tkinter import*
from tkinter import messagebox

cafe1=0
cafe2=0
cafe3=0
cafe4=0
dinero=0
total_pagar=0
tupla=[]#tupla que almacenara el pago por cada vez que se haga una compra,
        #y que no se reinicie el total cuando el usuario pida comprar otro cafe


###########OTRO CAFE
##en el caso de querer otro cafe se reinician todos los widgets y varaiables
##(excepto la tupla que debe almacenar el total), y mandara al main nuevamente

def otro():
    global cafe1, cafe2, cafe3, cafe4, total_pagar
    cafe1=0
    cafe2=0
    cafe3=0
    cafe4=0
    total_pagar=0
    menu_preparando.withdraw()
    lista.delete(0,END)
    caja.config(state="normal")
    caja.delete(0,END)
    caja.insert(0,0)
    caja.config(state="readonly")
    menu_principal.deiconify()

#############BOLETA CAFE
##si el usuario decide que no quiere otro se preguntara si quiere recibo
##se preparara la boleta
##y si hay vuelto te lo mostrara en una alerta
    
def no_otro():
    global total_pagar, dinero
    menu_preparando.withdraw()
    recibo=messagebox.askyesno(message="¿Desea imprimir el recibo?")
    if recibo==True:
        boleta.deiconify()
        total_boleta=sum(tupla)
        lista1.insert(END,"")
        lista1.insert(END,("TOTAL.................",total_boleta))
        lista1.insert(END,("VUELTO................",dinero))
        lista1.config(width=30,height=(lista1.size()+1),font=("Consolas",10))
    if dinero>0:
            messagebox.showinfo("!HASTA LA PROXIMA¡",
                                ("NO","OLVIDE","RETIRAR","SU","VUELTO","$",dinero,))

#########FUNCION DONDE SE PREPARA EL CAFE
###esta funcion es solo de interfaz donde te dice que el cafe se esta preparando
###tambien te pregunta si quiere otro cafe o no

def preparacion():
    global menu_preparando, dinero, total_pagar
    menu_preparando=Toplevel()
    menu_preparando.title("preparando")
    menu_preparando.geometry("580x500+460+175")
    menu_preparando.configure(background="#faffa7")

    PREPARANDO=Label(menu_preparando,text="PREPARANDO")
    PREPARANDO.pack()
    PREPARANDO.config(fg="#f37736",bg="#faffa7",font=("Colonna MT",40))

    a=Label(menu_preparando,text="Su(s) cafe(s) se esta(n) preparando")
    a.place(x=95,y=90)
    a.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",21))
    
    a1=Label(menu_preparando,text="Porfavor espere")
    a1.place(x=195,y=140)
    a1.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",21))
    
    a2=Label(menu_preparando,text=".............")
    a2.place(x=235,y=190)
    a2.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",21))

    a3=Label(menu_preparando,text="Su(s) cafe(s) esta(n) listos")
    a3.place(x=135,y=240)
    a3.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",21))

    a4=Label(menu_preparando,text="Su VUELTO es   $")
    a4.place(x=165,y=290)
    a4.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",21))

    a5=Label(menu_preparando,text=dinero)
    a5.place(x=367,y=290)
    a5.config(fg="#1d0149",bg="#faffa7",font=("Imprint MT Shadow",18))

    a6=Label(menu_preparando,text="¿Desea comprar otro  cafe?")
    a6.place(x=135,y=340)
    a6.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",21))


    ##BOTONES

    si=Button(menu_preparando,width=5,text="SI",bg="#45a32e",command=otro)
    si.place(x=322,y=400)
    si.config(font=(8))##boton para comprar otro cafe

    no=Button(menu_preparando,width=5,text="NO",bg="#ff3030",command=no_otro)
    no.place(x=202,y=400)
    no.config(font=(8))##boton para finalizar el programa


###########VOLVER ATRAS
##esta opcion es si el usuario por cualquier razon desea volver atras del menu
##de pago y reinicia todas las variables y widgets(excepto el dinero para no perderlo)

def atras():
    menu_pago.withdraw()
    menu_principal.deiconify()
    
##################################PROCESO DEL PAGO###############################
##########verifica el dinero ingresado, se hace la lista de lo comprado,
#y se ingresa en la boleta
    
def proceso():
    global dinero, total_pagar, cafe1, cafe2, cafe3, cafe4
    ingresar=int(caja3.get())
    ingresado=int(caja2.get())
    dinero=ingresado+ingresar
    if dinero<total_pagar:
        messagebox.showwarning("ERROR","DINERO INSUFICIENTE")
        caja2.config(state="normal")
        caja2.delete(0,END)
        caja2.insert(0,dinero)
        caja2.config(state="readonly")
        caja3.delete(0,END)
    else:
        menu_pago.withdraw()
        tupla.append(int(total_pagar))
        dinero=dinero-total_pagar
        for i in range(0,cafe1):
            lista1.insert(END,"CAPUCCINO............$ 800")
     
        for x in range(0,cafe2):
            lista1.insert(END,"EXPRESO..............$ 1000")
            
        for z in range(0,cafe3):
            lista1.insert(END,"VAINILLA.............$ 1200")

        for y in range(0,cafe4):
            lista1.insert(END,"LATE.................$ 1400")
        preparacion()



################################################################################
########################FUNCION PAGO
##Funcion donde el usuario pagara, si el valor de la caja es 0 el programa
##mostrara una alerta de que no se ha comprado nada y no dejara avanzar,
##si es mayor que 0 se cerrara el main y abrira la ventana pago

def pagar():
    global dinero, menu_pago, total_pagar
    if total_pagar==0:
        messagebox.showwarning("ERROR", "NO HA ELEGIDO NADA")
    elif total_pagar>0:
        menu_principal.withdraw()
        menu_pago=Toplevel()
        menu_pago.title("pagar")
        menu_pago.geometry("500x340+500+245")
        menu_pago.configure(background="#faffa7")

        ##ETIQUETAS

        LBL11=Label(menu_pago,text="PAGO")
        LBL11.pack(anchor=CENTER)
        LBL11.config(fg="#f37736",bg="#faffa7",font=("Colonna MT",40))

        LBL12=Label(menu_pago,text="TOTAL A PAGAR")
        LBL12.place(x=40,y=100)
        LBL12.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",20))

        LBL13=Label(menu_pago,text="TIENES")
        LBL13.place(x=40,y=150)
        LBL13.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",20))

        LBL14=Label(menu_pago,text="INGRESAR")
        LBL14.place(x=40,y=200)
        LBL14.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",20))

        LBL15=Label(menu_pago,text="$")
        LBL15.place(x=275,y=100)
        LBL15.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",20))

        LBL16=Label(menu_pago,text="$")
        LBL16.place(x=275,y=150)
        LBL16.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",20))

        LBL17=Label(menu_pago,text="$")
        LBL17.place(x=275,y=200)
        LBL17.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",20))
        
        ##CAJAS
        global caja1
        global caja2
        global caja3

        ##caja donde se mostrara el total a pagar
        caja1=Entry(menu_pago,width=13)
        caja1.place(x=305,y=106)
        caja1.insert(0,total_pagar)
        caja1.config(state="readonly",font=(20))

        ##caja donde se mostrara cuanto dinero se ha ingresado en la maquina
        caja2=Entry(menu_pago,width=13)
        caja2.place(x=305,y=156)
        caja2.insert(0,dinero)
        caja2.config(state="readonly",font=(20))

        ##caja donde el usuario ingresara el dinero
        caja3=Entry(menu_pago,width=13)
        caja3.place(x=305,y=206)
        caja3.config(font=(20))
        
        if dinero>=total_pagar:
            caja3.insert(0,0)

        PAGAR=Button(menu_pago,text="PAGAR",bg="#45a32e",command=proceso)
        PAGAR.place(x=305,y=255)##boton para hacer efectivo el pago

        ATRAS=Button(menu_pago,text="CANCELAR",bg="#ff3030",command=atras)
        ATRAS.place(x=205,y=255)##boton para volver al menu principal


#######################################################################
#############################FUNCION SALIR
##aqui el programa vera si el usuario tiene dinero en la maquina o no
##y si ha comprado algo para que ocurra la funcion correspondiente
##y la maquina entregue el vuelto y no se cierre si darlo
    
def salir():
    respuesta=messagebox.askyesno("SALIR","¿ESTAS SEGURO QUE DESEAS SALIR?")
    if respuesta==True:
        global menu_preparando, dinero, cafe1, cafe2, cafe3, cafe4
        cafe1=0
        cafe2=0
        cafe3=0
        cafe4=0
        lista.delete(0,END)
        if dinero>0:
            if sum(tupla)>0:
                menu_preparando=Toplevel()
                no_otro()
                menu_principal.destroy()
            elif sum(tupla)<=0:
                menu_principal.destroy()
                messagebox.showinfo("!HASTA LA PROXIMA¡",
                                ("NO","OLVIDE","RETIRAR","SU","VUELTO","$",dinero,))
                
        elif dinero<=0:
            if sum(tupla)>0:
                menu_preparando=Toplevel()
                no_otro()
                menu_principal.destroy()
            elif sum(tupla)<=0:
                menu_principal.destroy()

########################################################################################
###################################FUNCIONES SUMA#######################################
##########################################################################################

def eleccion1mas():
    global total_pagar, cafe1, caja
    cafe1=cafe1+1
    lista.insert(END,"CAPUCCINO.............$800")
    total_pagar=800+total_pagar
    caja.config(state="normal")
    caja.delete(0,END)
    caja.insert(0,total_pagar)
    caja.config(state="readonly")
    
def eleccion2mas():
    global caja, total_pagar, cafe2
    cafe2=cafe2+1
    lista.insert(END,"EXPRESO....................$1000")
    total_pagar=1000+total_pagar
    caja.config(state="normal")
    caja.delete(0,END)
    caja.insert(0,total_pagar)
    caja.config(state="readonly")
    
def eleccion3mas():
    global caja, total_pagar, cafe3
    cafe3=cafe3+1
    lista.insert(END,"VAINILLA...................$1200")
    total_pagar=1200+total_pagar
    caja.config(state="normal")
    caja.delete(0,END)
    caja.insert(0,total_pagar)
    caja.config(state="readonly")
    
def eleccion4mas():
    global caja, total_pagar, cafe4
    cafe4=cafe4+1
    lista.insert(END,"LATE...........................$1400")
    total_pagar=1400+total_pagar
    caja.config(state="normal")
    caja.delete(0,END)
    caja.insert(0,total_pagar)
    caja.config(state="readonly")
    
######################################################################################
###########################FUNCIONNES DE BORRADO
######################################################################################
    
def borrar():
    global cafe1, cafe2, cafe3, cafe4, total_pagar, caja
    eliminar=lista.get(END)
    lista.delete(END)
    caja.config(state="normal")
    if eliminar == "CAPUCCINO.............$800":
        cafe1=cafe1-1
        total_pagar=total_pagar-800
        caja.delete(0,END)
        caja.insert(0,total_pagar)
    elif eliminar == "EXPRESO....................$1000":
        cafe2=cafe2-1
        total_pagar=total_pagar-1000
        caja.delete(0,END)
        caja.insert(0,total_pagar)
    elif eliminar == "VAINILLA...................$1200":
        cafe3=cafe3-1
        total_pagar=total_pagar-1200
        caja.delete(0,END)
        caja.insert(0,total_pagar)
    elif eliminar == "LATE...........................$1400":
        cafe4=cafe4-1
        total_pagar=total_pagar-1400
        caja.delete(0,END)
        caja.insert(0,total_pagar)
    caja.config(state="readonly")
    
def borrar_todo():
    global caja, total_pagar, cafe1, cafe2, cafe3, cafe4
    cafe1=0
    cafe2=0
    cafe3=0
    cafe4=0
    total_pagar=0
    lista.delete(0,END)
    caja.config(state="normal")
    caja.delete(0,END)
    caja.insert(0,total_pagar)
    caja.config(state="readonly")
    
    
####Abro la pantalla donde se mostraran los cafes disponibles
####y se dara la opcion de pedir un cafe o borrar el pedido


def menu1(event):
    global menu_principal, borrar, borrar_todo, salir, caja, lista
    ventana.withdraw()
    menu_principal=Toplevel()
    menu_principal.title("menu principal")
    menu_principal.geometry("900x430+300+200")
    menu_principal.configure(background="#faffa7")

    ##Creo una listbox donde se mostrara una lista de todos los cafes pedidos
    ##por el ususario

    lista=Listbox(menu_principal,fg="#1d0149")
    lista.place(x=715,y=149)                 
    lista.config(height=11,width=25)


    ##Creo una caja donde se mostrara el total de lo pedido por el usuario

    caja=Entry(menu_principal)
    caja.place(x=800,y=347)
    caja.insert(0,0)
    caja.config(width=11,state="readonly")

    #######################################################################################
    #######################LABELS
    ########################################################################################


    LBL1=Label(menu_principal,text="BIENVENIDO")
    LBL1.pack(anchor=CENTER)
    LBL1.config(fg="#f37736",bg="#faffa7",font=("Colonna MT",40))

    LBL2=Label(menu_principal,text="LISTA DE CAFES DISPONIBLES:")
    LBL2.place(x=15,y=90)
    LBL2.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",23))

    LBL3=Label(menu_principal,text=" Presione para comprar Capuccino")
    LBL3.place(x=25,y=140)
    LBL3.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",22))

    LBL4=Label(menu_principal,text=" Presione para comprar Expreso")
    LBL4.place(x=25,y=190)
    LBL4.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",22))

    LBL5=Label(menu_principal,text=" Presione para comprar Vainilla")
    LBL5.place(x=25,y=240)
    LBL5.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",22))

    LBL6=Label(menu_principal,text=" Presione para comprar Late")
    LBL6.place(x=25,y=290)
    LBL6.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",22))

    ##VALORES CAFES

    LBL7=Label(menu_principal,text="$800")
    LBL7.place(x=450,y=140)
    LBL7.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",22))

    LBL8=Label(menu_principal,text="$1000")
    LBL8.place(x=450,y=190)
    LBL8.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",22))

    LBL9=Label(menu_principal,text="$1200")
    LBL9.place(x=450,y=240)
    LBL9.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",22))

    LBL10=Label(menu_principal,text="$1400")
    LBL10.place(x=450,y=290)
    LBL10.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",22))

    LBLT=Label(menu_principal,text="TOTAL $")
    LBLT.place(x=715,y=345)
    LBLT.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",15))

    CARRITO=Label(menu_principal,text="CARRITO:")
    CARRITO.place(x=725,y=107)
    CARRITO.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",22))

    ##########################################################################################
    #########################BOTONES
    ###########################################################################################

    bmas1=Button(menu_principal,text="+",width=5,bg="#45a32e",command=eleccion1mas)
    bmas1.place(x=550,y=150)##boton para agregar un capuccino al pedido

    bmas2=Button(menu_principal,text="+",width=5,bg="#45a32e",command=eleccion2mas)
    bmas2.place(x=550,y=200)##boton para agregar un expreso al pedido

    bmas3=Button(menu_principal,text="+",width=5,bg="#45a32e",command=eleccion3mas)
    bmas3.place(x=550,y=250)##boton para agregar un cafe de vainilla al pedido

    bmas4=Button(menu_principal,text="+",width=5,bg="#45a32e",command=eleccion4mas)
    bmas4.place(x=550,y=300)##boton para agregar un late al pedido

    borrar=Button(menu_principal,text="BORRAR",width=12,bg="#ff3030",command=borrar)
    borrar.place(x=610,y=175)##boton para borrar el ultimo cafe pedido

    borrar_todo=Button(menu_principal,text="BORRAR TODO",width=12,bg="#ff3030",command=borrar_todo)
    borrar_todo.place(x=610,y=275)##boton para borrar toda la compra

    confirmar=Button(menu_principal,text="CONFIRMAR",bg="#45a32e",command=pagar)
    confirmar.place(x=525,y=355)
    confirmar.config(width=10,height=2)##boton para confirmar los cafes pedidos

    salir=Button(menu_principal,text="SALIR",bg="#ff3030",command=salir)
    salir.place(x=300,y=355)
    salir.config(width=10,height=2)##boton para salir del programa

##funcion que hace parpadear el label

def flash():
    color=ETIQUETA2.cget("foreground")
    if color=="#1d0149":
        ETIQUETA2.configure(foreground="#faffa7")
        ETIQUETA2.after(450,flash)
    elif color=="#faffa7":
        ETIQUETA2.configure(foreground="#1d0149")
        ETIQUETA2.after(600,flash)

#######################################################################################
##########################Inicio del programa
########################################################################################


#####Creo una ventana donde inserto una listbox que almacenara los cafes
#####comprados para despues mostrarlos en la boleta, luego la cierro para que
#####no aparezca al inicio

global boleta
boleta=Tk()
boleta.geometry("+450+200")
scrollbar=Scrollbar(orient=VERTICAL)
lista1=Listbox(boleta,fg="black",yscrollcommand=scrollbar.set)
lista1.insert(0,("-----------------------------------"))
lista1.insert(1,("              BOLETA"))
lista1.insert(2,("-----------------------------------"))
lista1.insert(3,(""))
scrollbar.config(command=lista1.yview)
scrollbar.pack(side=RIGHT, fill=Y)
lista1.pack()
boleta.withdraw()

####Inicio del main
####pantalla principal solo de diseño

global ventana

ventana=Tk()
ventana.title("Bienvenido")
ventana.geometry("800x460+350+185")
ventana.configure(background="#faffa7")
ETIQUETA=Label(ventana,text="Bienvenido a su maquina de cafe")
ETIQUETA.pack(anchor=CENTER)
ETIQUETA.config(fg="#f37736", bg="#faffa7", font=("Colonna MT",40))

foto=PhotoImage(master=ventana,file="cafe2.png")
F=Label(ventana,image=foto)
F.place(x=230,y=70)

ETIQUETA2=Label(ventana,text="Presione tecla ENTER para continuar")
ETIQUETA2.config(fg="#faffa7", bg="#faffa7", font=("Colonna MT",25))
ETIQUETA2.place(x=140,y=380)

ventana.bind('<Return>', menu1)
flash()

ventana.mainloop()
