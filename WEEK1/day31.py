"""
x = 4
y = x**2 + 3*x +2
print(y)
"""

# #functionを作成
# # def f(x=2):
# #     y = x**2 + 3*x +2
# #     print(y)

# #ここに数値入れたら、こちら
# # f(4)

# number = int(input('Enter a number:'))
# f(number)
"""
def add(x,y,z=2):
    return(x+y+z)
def mul(z,y):
    return x*y*z
def change():
    global x
    x=2
x=5
num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
change()
answer = mul(num1,num2)
print(f'the answer is {answer}')
"""
"""
function for 
subtract
multiply
divide
"""
"""
def subtract(x,y):
    return(x-y)

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

answer = subtract(num1,num2)
print(f'the answer is {answer}')

def multiply(x,y):
    return(x*y)

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

answer = multiply(num1,num2)
print(f'the answer is {answer}')

def devide(x,y):
    return(x/y)

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))

answer = devide(num1,num2)
print(f'the answer is {answer}')
"""
"""
name = input('name:')
time = int(input('time:'))

def total(number_of_items, price):
    return(number_of_items * price)

number_of_items = int(input('items:'))
price = int(input('price:'))
total = total(number_of_items,price)

if time>=15 and number_of_items>=5:
    total = total *0.9*0.9
    print(f'Total amount of {name} is {total}')
elif time<15 and number_of_items>=5:
    total = total *0.9
    print(f'Total amount of {name} is {total}')
elif time>=15:
    total = total *0.9
    print(f'Total amount of {name} is {total}')
else:
    print(f'Total amount of {name} is {total}')
"""

import os

class Car:
    def __init__(self,car,brand,speedlimit,fuellimit):
        self.color = car
        self.brand = brand
        self.speedlimit = speedlimit
        self.speed = 0
        self.fuellimit = fuellimit
        self.fuel = 0

    def information(self):
        return f"color: {self.color} brand: {self.brand}"

    def startUp(self):
        self.speed += 1
        return f"Car is Starting and Speed is now {self.speed}"

    def speedUp(self):
        if self.speed > 0 and self.fuel > 0:
            self.speed += 30
            self.fuel -= 1
            if self.speed > self.speedlimit:
                self.speed = self.speedlimit
                return f"Speed is now {self.speed}"
            else:
                return f"Speed is now {self.speed}"
        else:
            return "Please startup before speedup or fuel is nothing"

    def speedDown(self):
        if self.speed > 0 and self.fuel > 0:
            self.speed -= 30
            self.fuel -= 1
            if self.speed < 0:
                self.speed = 0
                return f" Speed is now {self.speed}.It's Stopped."
            else:
                return f"Speed is now {self.speed}"
        else:
            return "Please startup before speeddown or fuel is nothing"

    def fuelUp(self):
        self.fuel =self.fuellimit
        return f"Fuel is full.it is {self.fuel}"
        
    def stop(self):
        self.speed =0
        return "Car is stopped."



Car1 = Car("red","Toyota",200,20)
Car2 = Car("black","Ferrari",280,25)

# print(Car2.information())
# print(Car2.startUp())
# print(Car2.speedUp())

while True:
    print("Welcome to My Car")
    print(" [1]information")
    print(" [2]startup")
    print(" [3]speedup")
    print(" [4]speeddown")
    print(" [5]fuelup")
    print(" [6]stop")
    print(" [0]stop and exit")
    choice = int(input("Make Your Choice"))

    if choice ==1:
        os.system("clear")
        print(Car2.information())
        continue
    elif choice ==2:
        os.system("clear")
        print(Car2.startUp())
        continue
    elif choice ==3:
        os.system("clear")
        print(Car2.speedUp())
        continue
    elif choice ==4:
        os.system("clear")
        print(Car2.speedDown())
        continue
    elif choice ==5:
        os.system("clear")
        print(Car2.fuelUp())
        continue
    elif choice ==6:
        os.system("clear")
        print(Car2.stop())
        continue
    if choice ==0:
        os.system("clear")
        break
    else:
        break