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
    
class Band():
    newband={"drummer":[],"guitarist":[],"bassist":[]}
    def __init__(self,name):
        self.name=name
    def hire(self, kind, name):
        newband[kind]=name
        self.name = name
        
        
        
        