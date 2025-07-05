class Dog:
    species = "Canine"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def ctg(self):
        print("Dog name is :",self.name)
        print("Dog age is :",self.age)

dog1 = Dog("Buddy",3)
dog2 = Dog("Madyy",2)
dog1.ctg()
print(dog2.ctg())

#
# print(dog1.name,dog1.age)
# print(dog1.species)
# print(dog2.name)
# print("Age :",dog2.age)
#
# #Modifing the dog1 name
# dog1.name = "Max"
# print(dog1.name) # Max
#
# #Modifing the class variable
# print("Modifing the class variable")
# Dog.species = "Fanine"
# print(Dog.species) # Fanine
# print(dog1.species) # Fanine
# print(dog2.species) # Fanine