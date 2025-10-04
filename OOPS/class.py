class character :
    def __init__(self,name,health,attack):# def set_details(self, name , health, attack): 
        self.name = name
        self.health = health
        self.attack = attack
    def info(self):
        print(self.name," ",self.attack," ",self.health)


war = character("T",90,90)
mag = character("G",80,80)
arc = character("L",70,70)

# def win (a1,a2,a3):
#     if a1>a2 and a1>a3:
#         print("Mage wins")
#     elif a2>a3:
#         print("Warrior Wins")
#     else :
#         print ("Archer wins")
# mag.attack = 100
# win(mag.attack,war.attack,arc.attack)
# war = character()
# mag = character()
# arc = character ()

# arc.set_details("L",50,100)
# war.set_details("T",90,90)
# mag.set_details("M",70,70)

# war.info()
# mag.info()
# arc.info()


#Self - predefined parameter/object