class Dog:
    def __init__(self,name,tag):
        self.name = name
        self.tag = int(tag)
        self.tags=[tag]
    def change_tag(self,new_tag):
        self.tags.append(new_tag)
        self.tag = new_tag
        return self.tag
        
d=Dog("Moti",101)
print "Hi i m an object of class dog, this is what you see when you print me:",d
print "My name is %r and my tag no. is %r" % (d.name, d.tag)
print "Will change tag from 101 to 202 see my new tag %r" % d.change_tag(202)
print "Here is class Dog", .Dog