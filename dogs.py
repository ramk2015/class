class Dog:
    def __init__(self,name):
        self.name=name
        self.tricks=[]
    def add_trick(self,trick):
        self.tricks.append(trick)
    kind = "canine"

d=Dog("Moti")
e=Dog("Biggy")
d.add_trick("roll over")
e.add_trick("play dead")
print d.name, d.kind, d.tricks
print e.name, e.kind, e.tricks
print type(d).__name__
print d.__class__.__name__== "Dog"
