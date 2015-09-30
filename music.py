class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"

class Drummer(Musician):
    def __init__(self):
        super (Drummer, self).__init__(["Dham","Dhoom","Dhad", "Dhitak"])
    def count(self):
        i=1
        while i < 5:
            print "counting", i
            i+=1
    def combust(self):
        print "dave poofed into thin air"
    
class Band(Drummer, Guitarist, Bassist):
    members=[]
    def __init__(self,name):
        self.name=name
    def hire(self,mem):
        self.members.append(mem)
        print "You are hiring ",mem," for ",self.name
        inp_type=raw_input("Enter 1 if drummer, 2 to if guitarist, 3 if bassist any other keystroke will assume drummer: ")
        if inp_type == "3":
            print "you have chosen a bassist for ",self.name
            mem = Bassist()
        elif inp_type == "2":
            print "you have chosen a guitarist for ",self.name
            mem = Guitarist()
        else: 
            print "you have chosen a drummer for ",self.name
            mem = Drummer()
            print mem.__class__.__name__
    def fire(self, mem):
        self.members.remove(mem)
        print "you have fired ",mem," from ",self.name
    def play(self, length):
        for i in range(len(self.members)):
            #temp = self.members[i]
            print self.members[i].__class__.__name__
            #if self.members[i].__class__.__name__ == "Drummer":
             #   self.members[i].count()
       # for i in range(len(self.members)):
        #    self.members[i].solo(length)
            
        
            
        #filter (lambda mem: mem.__class__.__name__ == "Drummer", members)
    
    #def play(self
      
       
       # inp_num= raw_input("Enter number of members (min 1 drummer) if not a number greater than 1 will assume 1")
        
        #inp_choice= raw_input ("Would you like to hire or fire members, for hire enter 1 any other keystroke for fire")
        #if inp_choice == 1:
         #   do 
          #  inp_choice=raw_input("Enter 1 to hire drummer, 2 to hire guitarist, 3 for bassist any other keystroke if decided not to hire")
           #     if inp_choice == 1:
            #        inp_drummer = raw_input ("Enter name of drummer")
             #       inp_drummer = Drummer()
              #      hire_members(inp_drummer)
               # el if inp_choice 
            
    

dave=Drummer()
dave.count()
dave.solo(10)
dave.combust()
a=Band("aerosmith")
a.hire("steve")
print a.name
a.hire("john")
a.hire("harry")
a.play(2)


