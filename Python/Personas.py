class Persona():
    __Nombre__: str()
    __Segundo_Nombre__: str()
    __Apellido__ : str()
    __Segundo_Apellido__: str()
    __Edad__: int()
    def __init__(self,__Nombre__,__Segundo_Nombre__,__Apellido__,__Segundo_Apellido__,__Edad__):
        self.Name = __Nombre__
        self.Middle_Name = __Segundo_Nombre__
        self.Last_Name = __Apellido__
        self.Second_Surname = __Segundo_Apellido__
        self.Age = __Edad__
        self.Gmail = __Nombre__.lower() + "-" + __Apellido__.lower() + "@Gmail.Com"
        
    def Get_Name(self):
        return self.Name + (" ") + self.Middle_Name +(" ") + self.Last_Name +(" ")+ self.Second_Surname
    
    def Get_Age(self):
        return self.Age

    def Get_Gmail(self):
    	return self.Gmail

    def Get_Adult(self):
    	if self.Age >= 18 :
    		return print("Mayor de edad")
    	else:
    		return print("Menor de edad")

    def Get_Mayor(self):
    	if Persona1.Get_Age() > Persona2.Get_Age():
    		return print(Persona1.Get_Name() + " is older than " + Persona2.Get_Name())
    	else:
    		return print(Persona2.Get_Name() + " is older than " + Persona1.Get_Name())



Persona1 = Persona("Kevin","Ignacio","Leiva","Puga", 18)
Persona2 = Persona("Sonia","Beatriz","Puga","Collio",36)
Persona1.Get_Name()
Persona1.Get_Mayor()
