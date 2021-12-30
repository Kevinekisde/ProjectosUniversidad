class reserva(object):
   nombre=input("ingrese su nombre: ")
   apellido= input("ingrese su apellido: ")
   telefono= int(input("ingrese su numero de telefono: "))
   correo= input("ingrese su correo: ")
   numdedias= int(input("cuantos dias quiere reservar: "))
   def final(self):
       print("muy bien %s %s su reserva de %s dias se ha concretado cualquier error se notificara al correo %s o al numero %s " % (self.nombre, self.apellido,self.numdedias,self.correo,self.telefono))
objeto= reserva()
objeto.final()
