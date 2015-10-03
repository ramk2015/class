import math #to round up decimals so profit margin maintained and some

class Bicycles(object):
    def __init__(self):
        self.models=['atlas','bmx','slr', 'kross', 'hercules', 'hero']
        self.weights={'atlas':10,'bmx':13,'slr':8, 'kross':15, 'hercules':11, 'hero':4}
        self.cost={'atlas':193,'bmx':78,'slr':229, 'kross':65, 'hercules':185, 'hero':499}
        self.num_models =len (self.models)


class Shops(Bicycles):
    def __init__(self,name,profit_margin, inventory_size):
        self.name=name
        self.profit_margin=1+profit_margin/100.0
        self.inventory_size = int(inventory_size)
        super(Shops,self).__init__() # superimpose parent class' initialization - not too comfortable with super yet

    inventory=[]
    models=list(set(inventory)) # can get the unique values by converting the list to a set
    brochure={}
    inventory_cost=int()
    profit=float()
    inventory_count={}
    
    def make_inventory(self):
        bikes_available=[]
        inventory_cost=0
        count = self.inventory_size #ensures that if inventory size desired is not a multiple of len(models) we account for the remainder
        
        if self.inventory_size > self.num_models:
            runs = self.inventory_size/self.num_models + 1 
            #runs to be 1 more as 8/6 = 2 thus inventory size will be 6, here we will make run 3 and stop it at 8 thru count
        else:
            runs = 1
        for i in range(0,runs):
            for k in self.models:
                if count > 0:
                    bikes_available.append(k)
                    inventory_cost+=self.cost[k]
                    count -=1
        inventory_count = dict((k, bikes_available.count(k)) for k in bikes_available)
        return bikes_available, inventory_cost, inventory_count
        
    def get_brochure(self):
        brochure = dict((k,math.ceil(v*self.profit_margin)) for k,v in self.cost.items() if k in self.models)
        return brochure
        
    def get_offer(self,budget):
        offer = dict((k,v) for k,v in self.brochure.items() if v <= budget)
        return offer
    
    def sell_bike(self,bike_sold): 
        # will need to add proft,remove from inventory, cost & inventory_count & if needed update models and brochure
        self.profit += self.brochure[bike_sold] - self.cost[bike_sold]
        self.inventory.remove(bike_sold)
        self.inventory_cost -= self.cost[bike_sold]
        self.inventory_count[bike_sold] -=1
        
        if bike_sold not in self.inventory:
            self.models.remove(bike_sold)
            del self.brochure[bike_sold]
        else: 
            "nothing to do"
        
    def status(self): #prints shop status with inventory count of each model and profit booked
        print "-" *40
        print "\tS H O P - S T A T U S"
        print "\t***%s***" % self.name
        print "Our inventory for each model now is: "
        for k in self.inventory_count:
            print "Bike %r, Stock: %r" % (k,self.inventory_count[k])
        print "\n ***Our profit booked is $%d***" % self.profit
        
        
class Customer():
    def __init__(self, name,funds):
        self.name=name
        self.funds=int(funds)

    offer={}
    bike_sold=None
    
    def buy_bike(self,offer):
        if offer == {}:
            return None
        else:    
            print '-'*40
            print "\t   B U Y  B I K E  M E N U\n"
            print  "%s choose a Bike from our inventory, you have $%r\n" % (self.name, self.funds)
            options=1
            
            for k,v in offer.items():
                print "%d. %s bike for $%r" % (options, k, v)
                options += 1
            
            print '-'*40
            user_input=None
            
            while user_input not in offer:
                user_input=raw_input("Enter bike model to purchase: ")
            
            self.funds -= offer[user_input]
            print """Great Choice !
            You are now a proud owner of a %s bike 
            which you bought for only $%r
            and have %r dollars left in your pocket
            BYE""" % (user_input,offer[user_input],self.funds)
            
            return(user_input)

    
