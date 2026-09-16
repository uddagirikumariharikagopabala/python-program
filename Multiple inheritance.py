class animal:
    def eat(self):
        print("Animal can eat")
class animal_1:
    def walk(self):
        print("can walk")
class child(animal,animal_1):
    def sleep(self):
        print("sleepy")
c1=child()
c1.eat()
c1.walk()
c1.sleep()
        

    
        
        
    


                
        