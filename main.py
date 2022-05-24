myString = "Hello"
myNumber = 20
print(myString)
print(myNumber)

myNumberList = [1,2,3]
myStringList = ["hello", "world"]
print(myStringList)
print(myStringList[0])

myStringList.append("it's me")
print(myStringList)

plus = 1+2
minus = 2-1
multiple = 2*3
division = 4/2
print(plus)
print(minus)
print(multiple)
print(division)

squaredNumber = 7 ** 2
cubedNumber = 2 ** 3
print(squaredNumber)
print(cubedNumber)


name = "John"
print("Hello %s!" % name)

if name == "John":
    print("This is John")
elif name== "Jhin":
    print("This is Jhin")
else:
    print("No Name")


def say_hi(name):
    print("hello hi %s!" % name)
say_hi("Jhin")

for x in myNumberList:
    print(x)


number = 0
while number<5:
    print(number)
    number += 1

months = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March"
}

print(months.get("Jan", "Not in dictionary"))
print(months.get("Nov", "Not in dictionary"))

# import moduleMatematika
# moduleMatematika.tambah(2,3)

# import moduleMatematika as math
# math.tambah(2,3)

# from moduleMatematika import tambah, kurang
# kurang(3,2)

# from moduleMatematika import *
# kurang(3,2)

from moduleMatematika import kurang as minus
minus(3,2)