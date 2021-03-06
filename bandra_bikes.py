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
        super(Shops,self).__init__() # superimpose parent class' initialization
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
        # will need to remove from inventory & cost & if needed update models and brochure
        self.profit += self.brochure[bike_sold] - self.cost[bike_sold]
        self.inventory.remove(bike_sold)
        self.inventory_cost -= self.cost[bike_sold]
        self.inventory_count[bike_sold] -=1
        
        if bike_sold not in self.inventory:
            self.models.remove(bike_sold)
            del self.brochure[bike_sold]
        else: 
            "nothing to do"
        
    def status(self):
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



def buy(cust,shop):
    cust.offer=shop.get_offer(cust.funds)
    cust.bike_sold = cust.buy_bike(cust.offer)
    if cust.bike_sold != None:
        shop.sell_bike(cust.bike_sold)
    else: 
        print "%s happy window shopping, you have too few funds to buy today" % cust.name

def show_offer(cust,shop):
    cust.offer=shop.get_offer(cust.funds)
    print "\nHi %s \nBased on your budget of $%d we can offer you the following:\n " % (cust.name,cust.funds)
    for k in cust.offer:
        print "%r bike at a price of $%r" % (k,cust.offer[k])

#quick initialize shop
shop_name = "Bandra Bikes"; shop_margin = 20; shop_inventory = 6
shop1=Shops(shop_name,shop_margin,shop_inventory)


#build the shop
shop1.inventory, shop1.inventory_cost, shop1.inventory_count = shop1.make_inventory()
shop1.brochure=shop1.get_brochure()


#quick initialize customers
cust1=Customer("Ram",1000)
cust2=Customer("Que",500)
cust3=Customer("Jay",200)


show_offer(cust1,shop1)
show_offer(cust2,shop1)
show_offer(cust3,shop1)

shop1.status() #initial status

buy(cust1,shop1)
buy(cust2,shop1)
buy(cust3,shop1)

shop1.status() #final status


##initialize a shop user input way
"""
def make_shop():
    print '-' * 40,"\n","\t Initializing a Shop\n",'-' * 40
    shop_name =raw_input("What would you like to call the shop: ")
    shop_margin=0
    shop_inventory=0
    valid_inputs=list(range(1,100))
    while shop_margin not in valid_inputs:
        try:
            shop_margin = int(raw_input("What profit margin would you like the shop to run at (between 0-100): "))
        except ValueError:
            print "Numeric Inputs only"
    while shop_inventory not in valid_inputs:
        try:
            shop_inventory = int(raw_input("What inventory would you like to start the shop with (between 0-100): "))
        except ValueError:
            print "Numeric Inputs Only:"
    return shop_name, shop_margin, shop_inventory

shop_name, shop_margin, shop_inventory = make_shop()
"""