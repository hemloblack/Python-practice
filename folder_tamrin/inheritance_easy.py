class Person:
    def __init__(self, name):
        self.name = name
        
    def info(self):
        print(f"hello my name is {self.name}")
        
        
class Student(Person):
    def study(self):
        print("I am studying")
        

user = Person("Hamid")
student = Student("Ali")

user.info()
student.info()
student.study()
