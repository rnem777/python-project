#it is to modify between the subject and the behaviour
# the name has always to stat with cabital litter
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def walk(self):#self here will give us access to name 
        print(self.name + ' is a student at sunderland university')
    # classes nd behavior and objects
    def speak(self):
        print('Hello my name is ' + self.name + ' and I am ' + str(self.age) + ' years old') 
    

ibrahim = Person('Ibrahim', 30)
sahem = Person('Sahem', 15)
print(ibrahim.name + ' ' + str(ibrahim.age))
ibrahim.speak()
ibrahim.walk()
print('---------------------')
print(sahem.name + ' ' + str(sahem.age))
sahem.speak()
sahem.walk()