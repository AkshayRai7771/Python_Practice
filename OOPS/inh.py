class Bikes:
    def type(self=None):
        self.t = "Petrol"
class TVS(Bikes):
    def show(self,max_speed,milage):
        super().type() #super() is a temp obj that allows subclass to call methods of  superclass
        self.max_speed =  max_speed
        self.milage = milage
        print(f"Max Speed : {self.max_speed} kmph , Milage : {self.milage} , Company Name : TVS , Type : {self.t}")
        print("")
class Bajaj(Bikes):
    def show(self,max_speed,milage):
        super().type()
        self.t = "EV"
        self.max_speed =  max_speed
        self.milage = milage
        print(f"Max Speed : {self.max_speed} kmph , Milage : {self.milage} Company Name : Bajaj , Type : {self.t}")
        print("")


model1 = TVS()
model2 = Bajaj()

model1.show(120,35)
model2.show(160,30)


