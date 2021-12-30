from tkinter import*
from tkinter import messagebox
import functools

totalT=[]
total=0

############################## CAFES ###############################
class Cafes():
    
         #############  Propiedades de la clase  ##############
    
    def __init__(self):
        self.cantidad = 0
        self.sabor = str
        self.valor = int
        self.total = 0
        self.lista = []
        self.lista_total = []
        self.lista_cantidad = []
        
         ###############  Metodos de la clase  #################
        
    def cafes_mas(self):
        global lista, total
        self.cantidad=self.cantidad+1
        self.total=self.cantidad*self.valor
        self.lista.append((self.cantidad,"×",self.sabor,self.total))
        self.lista = list(filter(lambda n: n==(self.cantidad,"×",self.sabor,
                                               self.total),self.lista))
        total=capuccino.total+expreso.total+vainilla.total+late.total
        lista = capuccino.lista+expreso.lista+late.lista+vainilla.lista
        caja.config(state="normal")
        caja.delete(0,END)
        caja.insert(END,total)
        caja.config(state="readonly")
        listbox.delete(0,END)
        listbox.insert(END, *lista)
        
    def cafe_menos(self):
        global lista, total
        self.cantidad=self.cantidad-1
        if self.cantidad<1:
            self.cantidad=0
        self.total=self.cantidad*self.valor
        self.lista.append((self.cantidad,"×",self.sabor,self.total)) 
        self.lista = list(filter(lambda n: n==(self.cantidad,"×",self.sabor,
                                               self.total),self.lista))
        if self.cantidad==0:
            self.lista.remove((self.cantidad,"×",self.sabor,self.total))
        total=capuccino.total+expreso.total+vainilla.total+late.total
        lista = capuccino.lista+expreso.lista+late.lista+vainilla.lista
        caja.config(state="normal")
        caja.delete(0,END)
        caja.insert(END,total)
        caja.config(state="readonly")
        listbox.delete(0,END)
        listbox.insert(END, *lista)

    def borrar_todo(self):
        global lista, total
        self.cantidad=0
        self.total=0
        self.lista[:]=[]
        lista[:]=[]
        total=0
        caja.config(state="normal")
        caja.delete(0,END)
        caja.insert(END,total)
        caja.config(state="readonly")
        listbox.delete(0,END)

    def recibo_total(self):
        self.lista_total.append(self.total)
        self.lista_cantidad.append(self.cantidad)
        self.c = functools.reduce(lambda x, y: x+y,self.lista_cantidad)
        self.t = functools.reduce(lambda x, y: x+y,self.lista_total)

        ###############  Objetos de la clase cafe  #####################

capuccino=Cafes()
capuccino.sabor="CAPUCCINO.........."
capuccino.valor=800

expreso=Cafes()
expreso.sabor="EXPRESO............"
expreso.valor=1000

late=Cafes()
late.sabor="LATE..............."
late.valor=1200

vainilla=Cafes()
vainilla.sabor="VAINILLA..........."
vainilla.valor=1400
        

#################################### Dinero   ##############################################

class Dinero():
    
    def __init__(self):
        self.cantidad = 0

    def transaccion(self):
        global caja2, caja3
        self.cantidad=int(caja3.get())+int(caja2.get())
        caja2.config(state="normal")
        caja2.delete(0,END)
        caja2.insert(0,self.cantidad)
        caja2.config(state="readonly")
        caja3.delete(0,END)
        if self.cantidad>=total:
            self.cantidad=self.cantidad-total

        #################### Objeto de la clase ##################

dinero=Dinero()

#############################   BOLETA    #########################################################

class Boleta():

        
    def insertar(self):

        ################################archivo de texto##################
        b=open("boleta.txt","a+")
        b.write("\n")
        b.write('############################ comprobante de compra ############################')
        b.write("\n")


        if late.c>0:
            b.write(f"{late.c} × {late.sabor} ${late.t}")

        b.write("\n")

        if vainilla.c>0:
            b.write(f"{vainilla.c} × {vainilla.sabor} ${vainilla.t}")

        b.write("\n")

        if expreso.c>0:
            b.write(f"{expreso.c} × {expreso.sabor} ${expreso.t}")

        b.write('\n')

        if capuccino.c>0:
            b.write(f"{capuccino.c} × {capuccino.sabor} ${capuccino.t}")
        b.write("\n")
        b.write((f"TOTAL.................. ${sum(totalT)}"))
        b.write("\n")
        b.write(f"VUELTO................. ${dinero.cantidad}")

        #################### Objeto de la clase ##################

boleta=Boleta()

##########################################################################

def menu_boleta():
    
    global boleta, ventana4, recibo

    menu_preparando.withdraw()
    ventana4 = Toplevel()
    ventana4.title("boleta")

    recibo=Listbox(ventana4)
    recibo.insert(0,"--------------------------------------")
    recibo.insert(1,"  Su comprobante se ha creado")
    recibo.insert(2,"  Porfavor desecharlo una vez leido")
    recibo.insert(3,"--------------------------------------")
    recibo.insert(4,"")
    recibo.pack()   
    boleta.insertar()
    recibo.config(width=36,height=recibo.size()+1,font=("Consolas",10))

###########################################################################################################
################################### MENUS #################################################################

def menu_preparacion():

    global menu_preparando, total
    
    if int(caja2.get())<total:
        messagebox.showwarning("ERROR", "DINERO INSUFICIENTE")
        
    else:

        menu_pago.withdraw()
        
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

        a4=Label(menu_preparando,text=f"Su VUELTO es   $ {dinero.cantidad}")
        a4.place(x=165,y=290)
        a4.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",21))

        a6=Label(menu_preparando,text="¿Desea comprar otro cafe?")
        a6.place(x=135,y=340)
        a6.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",21))

        capuccino.recibo_total()
        expreso.recibo_total()
        late.recibo_total()
        vainilla.recibo_total()
        totalT.append(total)
        
        si=Button(menu_preparando,text="SI",command=lambda:[capuccino.borrar_todo(),
                                                     late.borrar_todo(),
                                                     expreso.borrar_todo(),
                                                     vainilla.borrar_todo(),
                                                     otro()])
        si.place(x=322,y=400)
        si.config(font=(8),width=5,bg="#45a32e")

        
        no=Button(menu_preparando,text="NO",command=menu_boleta)
        no.place(x=202,y=400)
        no.config(font=(8),width=5,bg="#ff3030")

        
def menu_pago():
    global caja2, caja3, caja4, menu_pago

    if total==0:
        messagebox.showwarning("ERROR", "NO HA ELEGIDO NADA")

    else:
        ventana.withdraw()
        menu_pago = Toplevel()

        menu_pago.title("pagar")
        menu_pago.geometry("500x340+500+245")
        menu_pago.configure(background="#faffa7")

        ##ETIQUETAS

        LBL12=Label(menu_pago,text="PAGO")
        LBL12.pack(anchor=CENTER)
        LBL12.config(fg="#f37736",bg="#faffa7",font=("Colonna MT",40))

        LBL13=Label(menu_pago,text="TOTAL A PAGAR")
        LBL13.place(x=40,y=100)
        LBL13.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",20))

        LBL14=Label(menu_pago,text="TIENES")
        LBL14.place(x=40,y=150)
        LBL14.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",20))

        LBL15=Label(menu_pago,text="INGRESAR")
        LBL15.place(x=40,y=200)
        LBL15.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",20))

        LBL16=Label(menu_pago,text="$")
        LBL16.place(x=275,y=100)
        LBL16.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",20))

        LBL17=Label(menu_pago,text="$")
        LBL17.place(x=275,y=150)
        LBL17.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",20))

        LBL18=Label(menu_pago,text="$")
        LBL18.place(x=275,y=200)
        LBL18.config(fg="#1d0149",bg="#faffa7",font=("Colonna MT",20))

        caja1=Entry(menu_pago,width=13)
        caja1.insert(0,total)
        caja1.config(state="readonly", fg="#1d0149", font=("Consolas",15))
        caja1.place(x=305,y=106)

        caja2=Entry(menu_pago,width=13)
        caja2.insert(0,dinero.cantidad)
        caja2.config(state="readonly", fg="#1d0149", font=("Consolas",15))
        caja2.place(x=305,y=156)

        caja3=Entry(menu_pago,width=13)
        caja3.config(fg="#1d0149", font=("Consolas",15))
        caja3.place(x=305,y=206)

        if dinero.cantidad>=total:
                caja3.insert(0,0)

        pagar=Button(menu_pago,text="PAGAR",bg="#45a32e",command=lambda:[dinero.transaccion(),
                                                           menu_preparacion()])
        pagar.place(x=305,y=255)

        atras=Button(menu_pago,text="CANCELAR",bg="#ff3030",command=volver_atras)
        atras.place(x=205,y=255)
##################################### funciones varias ###################################################
def otro():
    menu_preparando.withdraw()
    ventana.deiconify()

def volver_atras():
    menu_pago.withdraw()
    ventana.deiconify()

def salir():
    global menu_preparando
    respuesta=messagebox.askyesno("SALIR","¿ESTAS SEGURO QUE DESEAS SALIR?")
    if respuesta==True:
        if dinero.cantidad>0:
            if sum(totalT)>0:
                menu_preparando=Toplevel()
                menu_boleta()
                ventana.destroy()
            elif sum(totalT)<=0:
                messagebox.showinfo("!HASTA LA PROXIMA¡",
                                    (f"NO OLVIDE RETIRAR SU VUELTO ${dinero.cantidad}"))
                ventana.destroy()
                
        elif dinero.cantidad<=0:
            if sum(totalT)>0:
                menu_preparando=Toplevel()
                menu_boleta()
                ventana.destroy()
            elif sum(totalT)<=0:
                ventana.destroy()


################################################ menu principal ##############################################              
ventana=Tk()
ventana.title("menu_principal")
ventana.geometry("900x450")
ventana.config(bg="#faffa7")

LBL1=Label(ventana,text="BIENVENIDO")
LBL1.config(font=("Colonna MT", 40), bg="#faffa7", fg="#f37736")
LBL1.pack()

LBL2=Label(ventana,text="Lista de cafes disponibles:")
LBL2.config(font=("Colonna MT", 23), bg="#faffa7", fg="#1d0149")
LBL2.place(x=15, y=90)

LBL3=Label(ventana,text=" Presione para comprar Capuccino")
LBL3.config(font=("Colonna MT", 20), bg="#faffa7", fg="#1d0149")
LBL3.place(x=25, y=140)

LBL4=Label(ventana,text=" Presione para comprar Expreso")
LBL4.config(font=("Colonna MT", 20), bg="#faffa7", fg="#1d0149")
LBL4.place(x=25, y=190)

LBL5=Label(ventana,text=" Presione para comprar Late")
LBL5.config(font=("Colonna MT", 20), bg="#faffa7", fg="#1d0149")
LBL5.place(x=25, y=240)

LBL6=Label(ventana,text=" Presione para comprar Vainilla")
LBL6.config(font=("Colonna MT", 20), bg="#faffa7", fg="#1d0149")
LBL6.place(x=25, y=290)

LBL7=Label(ventana,text="$800")
LBL7.config(font=("Colonna MT", 20), bg="#faffa7", fg="#1d0149")
LBL7.place(x=450, y=140)

LBL8=Label(ventana,text="$1000")
LBL8.config(font=("Colonna MT", 20), bg="#faffa7", fg="#1d0149")
LBL8.place(x=450, y=190)

LBL9=Label(ventana,text="$1200")
LBL9.config(font=("Colonna MT", 20), bg="#faffa7", fg="#1d0149")
LBL9.place(x=450, y=240)

LBL10=Label(ventana,text="$1400")
LBL10.config(font=("Colonna MT", 20), bg="#faffa7", fg="#1d0149")
LBL10.place(x=450, y=290)

LBL11=Label(ventana,text="TOTAL   $")
LBL11.config(font=("Colonna MT", 16), bg="#faffa7", fg="#1d0149")
LBL11.place(x=660, y=280)

capuccino.botonmas=Button(text="+",command=capuccino.cafes_mas)
capuccino.botonmas.config(width=4, bg="#45a32e")
capuccino.botonmas.place(x=535, y=143)

expreso.botonmas=Button(text="+",command=expreso.cafes_mas)
expreso.botonmas.config(width=4, bg="#45a32e")
expreso.botonmas.place(x=535, y=193)

late.botonmas=Button(text="+",command=late.cafes_mas)
late.botonmas.config(width=4, bg="#45a32e")
late.botonmas.place(x=535, y=243)

vainilla.botonmas=Button(text="+",command=vainilla.cafes_mas)
vainilla.botonmas.config(width=4, bg="#45a32e")
vainilla.botonmas.place(x=535, y=293)

capuccino.botonmenos=Button(text="-",command=capuccino.cafe_menos)
capuccino.botonmenos.config(width=4, bg="#ff3030")
capuccino.botonmenos.place(x=595, y=143)

expreso.botonmenos=Button(text="-",command=expreso.cafe_menos)
expreso.botonmenos.config(width=4, bg="#ff3030")
expreso.botonmenos.place(x=595, y=193)

late.botonmenos=Button(text="-",command=late.cafe_menos)
late.botonmenos.config(width=4, bg="#ff3030")
late.botonmenos.place(x=595, y=243)

vainilla.botonmenos=Button(text="-",command=vainilla.cafe_menos)
vainilla.botonmenos.config(width=4, bg="#ff3030")
vainilla.botonmenos.place(x=595, y=293)

borrar_todo=Button(text="BORRAR TODO",command=lambda:[capuccino.borrar_todo(),
                                                      expreso.borrar_todo(),
                                                      late.borrar_todo(),
                                                      vainilla.borrar_todo()])
borrar_todo.config(bg="#ff3030")
borrar_todo.place(x=540, y=343)

confirmar=Button(text="CONFIRMAR",command=menu_pago)
confirmar.config(bg="#45a32e", height=2, width=10)
confirmar.place(x=750, y=350)

salir=Button(text="SALIR", command=salir)
salir.config(bg="#ff3030", height=2, width=10)
salir.place(x=75, y=350)

listbox=Listbox()
listbox.config(width=30, height=4, fg="#1d0149", font=("Consolas",10))
listbox.place(x=660, y=170)

caja=Entry(ventana)
caja.config(state="readonly", width=10, fg="#1d0149", font=("Consolas",10))
caja.place(x=760, y=284)


ventana.mainloop()
