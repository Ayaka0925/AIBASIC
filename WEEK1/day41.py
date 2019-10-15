import os

class Car:
    def __init__(self,car_data):
        self.__engine_code=''
        self.engine_code_pub = ''
        self.car_data = car_data
        self.speedlimit = self.car_data[0]['speedlimit']
        self.speed = 0
        self.fuellimit = self.car_data[0]['fuellimit']
        self.fuel = 0
    #private ptoperty 外部からアクセスできない
    #__アンダースコア二つ
    
    def setEngineCode(self,engine_code):
        self.__engine_code = engine_code

    #private propertyにアクセスする機能を追加

    def getEngineCode(self):
        return self.__engine_code
    
    #private propertyから値をもらうため

    def information(self):
        return self.car_data[0]['car_name']

    def startUp(self):
        self.speed += 1
        return f'speed is now {self.speed}'

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
        
# car1=Car()
# car1.setEngineCode('XXXCC1234')

# print(car1.getEngineCode())

class Owner(Car):
    def __init__(self,car_data):
        Car.__init__(self,car_data)
        #super().__init__(self)
        self.car_data = car_data

    def ownerinformation(self):
        return f'The owner is {self.car_data[0]["owner_name"]}'

    def ownerView(self):
       
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
                print(self.information())
                continue
            elif choice ==2:
                os.system("clear")
                print(self.startUp())
                continue
            elif choice ==3:
                os.system("clear")
                print(self.speedUp())
                continue
            elif choice ==4:
                os.system("clear")
                print(self.speedDown())
                continue
            elif choice ==5:
                os.system("clear")
                print(self.fuelUp())
                continue
            elif choice ==6:
                os.system("clear")
                print(self.stop())
                continue
            if choice ==0:
                os.system("clear")
                break
            else:
                break

car_data=[
    {'ownew_id':1, 'car_name':'Ferrari','car_color':'red','owner_name':'Jan','speedlimit':280,'fuellimit':25}
]

# owner1 = Owner('Jan','Cebu')
# owner1.setEngineCode('XXX333')
# print(owner1.getEngineCode())
       
owner1 = Owner(car_data)
print(owner1.ownerinformation())
print(owner1.information())
print(owner1.startUp())
print(owner1.ownerView())
