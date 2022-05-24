class Dog:
    def __init__(self, name):
        self.name = name
        print(name)
    
    def add_one(self, x):
        return x+1

    def bark(self):
        print("bark")

d = Dog("Tim")
print(d.add_one(5))
d.bark()


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

c = Cat("Tom", 12)
print(c.get_name())
print(c.get_age())
c.set_age(20)
print(c.get_age())