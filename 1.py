class Car:
    def Drive(self):
        print("I am driving on")
    def Load(self):
        print("I am loading up")
    def Fill(self):
        print("I am filling up")

class Legkovushka(Car):
    def Load(self):
        print("I can't loading up more  than 2kg")

class Gruzovik(Car):
    def Load(self):
        print("I can't loading up more than 25kg")

class Belaz(Car):
    def Drive(self):
        print("My speed is bad")

def Info(self):
        print(Car)

leg = Legkovushka()
leg.Info