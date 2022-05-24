class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")


p = Pet("Tim Pet", 19)
p.show()

c = Cat("Tim Cat", 10)
c.show()

d = Dog("Tim Dog", 10)
d.show()