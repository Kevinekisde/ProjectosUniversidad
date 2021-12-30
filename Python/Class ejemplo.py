###### CREACION DE CLASES ######################################
class user:   ##### creas clase
    name = ""       ##### se crean variables
    last_name = ""

    def __init__(self,name,last_name):
        self.name=name
        self.last_name=last_name
        self.email= name.lower() + "." + last_name.lower()+"@cloud.uautonoma.cl"
    
    def get_email(self):
        return self.email

########################## HERENCIA #################################

class student(user):

    institucion=""

    def __init__(self,name,last_name,school):
        super().__init__(name,last_name) ### le pido ala clase user que use sus atributos
        self.institucion=school
    
    #def get_email(self):                 ############# Sobre carga de metodos #####################
        #mail = self.email.split("@")
        #return mail[0] + "@uautonoma.cl"

student1= user("Edith","Aguilera")
student2= user("Kevin","Leiva")
student_3=student("Edith","Aguilera","Universidad autonoma")

print(student_3.institucion) ####### HERENCIA #############
print(student1.get_email())     ####  manera mas adecuada de hacer
print(user.get_email(student2)) ######
