class student (#user):
    institucion=""

    def __init__(self,name,last_name,school):
        super().__init__(name,last_name)
        self.institucion=school

student_3=student("Edith","Aguilera","Universidad autonoma")
print(student_3.name)

