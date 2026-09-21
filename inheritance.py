class vehicle:
    brand="BMW"
    model="MS"
class car(vehicle):
    def road(self):
        print("BMW car is a brand")
class bike(vehicle):
    def road(self):
        print("while driving wear helmet")
d1=car()
d1.road()
d1=bike()
d1.road()
