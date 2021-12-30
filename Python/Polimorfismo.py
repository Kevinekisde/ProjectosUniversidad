class user:   ##### creas clase
    name = ""       ##### se crean variables
    last_name = ""

    def __init__(self,name,last_name):
        self.name=name
        self.last_name=last_name
        self.email= name.lower() + "." + last_name.lower()+"@cloud.uautonoma.cl"
    
    def get_email(self):
        return self.email

student1= user("Edith","Aguilera")
student2= user("Kevin","Leiva")


print(student1.get_email())     ####  manera mas adecuada de hacer
print(user.get_email(student2))