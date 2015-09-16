class Parent(object): #create a class named Parent where an object can be passed
    
    def implicit(self): #define a function for all instances of class Parent
        print"Parent implicit()" #action when function called
    def override(self): #define a function for all instances of class PArent
        print "Parent override()" #action when function called
    def altered(self): # define a function for all instances of class Parent
        print "Parent altered()" # action when function called
    last_name="Khanna" #last name assigned value for all instances of class Parent
    def __init__(self, name): #initialise every instance of Parent with a value name
       self.name=name #assign name to self

class Child(Parent): #define a class named Child of(belonging to) class Parent
    def override(self): # define a function for all instance of class Child (? can a parent also call this function??)
        print "Child override()" #action when function called
    def altered(self): # define a function for all instance of class Child
        print "Child, before Parent altered()" #action when function called
        super(Child, self).altered() # call function as defined in super class Parent
        print "Child, after parent altered()" # action of function defined in class Child
    def unique(self): #like all functions of class Child it is unique to class Child and its subclasses, class Parent does not have access to it
        print "I am a Child who is unique()" #action of functio defined in class Child
    #def __init__(self): #call initialise self 
     #   super (Child,self).__init__("Dev") #alternative to initialising every child with a name here no value needs to be passed with child
       
        
dad=Parent("Ram")
son=Child("Dev")
#son=Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

son.unique()

print dad.name
print dad.last_name
print son.name
print son.last_name

# dad.unique() "#dad.unique() #not allowed as instance of parent has no unique member"


#class SuperFun(Child, Badstuff): #define a class SuperFun that inherits/subclass from Child and Badstuff at the same time
