# name="law khon maine"
# print(name.upper())


class Car :
    sterring_wheel=1
    def __init__(self,name,wheels):
        self.name=name
        self.wheels=wheels

    def drive(self):
        print(f'{self.name} is driving.') 

    def full(self):
        print(f'{self.name} has {self.wheels} wheels.')  

    @classmethod
    def common(cls):
        print(f'All cars have only {Car.sterring_wheel} sterring wheel.')



name_car=input("Marcedes or Lamborghini :")

mar=Car(name_car,4)
mar.full()
Car.common()

drive_car=input("Would you like to drive? y/n :")

if drive_car == "y" :
    mar.drive()
else :
    print("Your car is stopped.")    
