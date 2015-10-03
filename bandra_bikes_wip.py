from sys import exit
import random #for simulating random sales
import math #to round up decimals so profit margin maintained and some
class Bicycles(object):
    def __init__(self):
        self.models=['atlas','bmx','slr']
        self.weights={'atlas':10,'bmx':13,'slr':8}
        self.cost={'atlas':93,'bmx':78,'slr':129}
        self.num_models =len (self.models)
        
class Shops(Bicycles):
    def __init__(self,name,profit_margin, inventory_size):
        self.name=name
        self.profit_margin=1+profit_margin/100.0
        self.inventory_size = int(inventory_size)
        super(Shops,self).__init__() # superimpose parent class' initialization
    
    def get_brochure(self):
        brochure={}
        for k,v in self.cost.items():
            brochure[k]=math.ceil(v*self.profit_margin)
        return brochure
    
    def make_inventory(self):
        number=self.inventory_size
        bikes_available=[]
        inventory_cost=0
        for i in range(0,number/self.num_models):
            for k in self.models:
               bikes_available.append(k)
               inventory_cost+=self.cost[k]
        return bikes_available, inventory_cost
    
       
    def simulate_sales_ftd(self,bikes, inventory):
        sales = 0
        profit = 0
        print "We sold %r bikes today" % bikes
        for i in range(0,bikes):
            sell_index = random.randrange(0,len(inventory)-1)
            sell = inventory[sell_index]
            cost_price=self.cost[sell]
            sell_price= self.cost[sell] * self.profit_margin
            print "Sale #%r was %r" % (i+1,sell)
            print "its cost was %r" % cost_price
            print "it was sold for %r" % sell_price
            profit += sell_price - cost_price
            print "Total profit for day upto this sale is %r" % profit 
            inventory.pop(sell_index)
        return inventory, profit

    

class Customer():
    def __init__(self, name,funds):
        self.name=name
        self.funds=int(funds)
    
    def buy_bike(self):
        open_funds=self.funds
    
    
        
industry = Bicycles()

shop1=Shops("Freddy's Bike Shop",20,100)
shop1_inventory, shop1_cost = shop1.make_inventory()
shop1_brochure=shop1.get_brochure()
shop1_brochure_2=dict((k,math.ceil(v*shop1.profit_margin)) for k,v in shop1.cost.items())
print shop1_brochure
print "should be same as"
print shop1_brochure_2
#sales_today=5
#shop1_inventory, shop1_profit = shop1.simulate_sales_ftd(sales_today,shop1_inventory)
cust1=Customer("Ram",100)
cust1_offer=dict((k,v) for k,v in shop1_brochure.items() if v <= cust1.funds)
#shop1.offer(cust1.funds)
print cust1_offer
#print "Hi %r we can offer you the following bikes:" % cust1.name
#for i in cust1_offer:
#    print i, "at a price of %r" % cust1_offer[i]*(1+shop1.profit_margin/100.0)
"""
print "models: ", industry.models
print "models and thier weights: ", industry.weights
print "models and their cost: ", industry.cost
for i in industry.models:
    print "%s model has weight: %s and costs %s" % (i,industry.weights[i],industry.cost[i])
print "Welcome to %r, we have the following bikes for you %r" % (shop1.name,shop1.models)
print "shop1_inventory: ", shop1_inventory
print "shop1_cost: ", shop1_cost
print "shop1_inventory after sale: ", shop1_inventory
print "shop1_profit: ", shop1_profit
"""

"""        
class Shops(Bicycles, object):
    def __init__(self,name):
        self.name=name
        
    
    def inventory(self, number):
        bikes_for_sale=[]
        for i in number/num_models:
            for i in self.models:
                bikes_for_sale.append(i)
        print bikes_for_sale
                
shop1=Shops("a to z sports")
shop1.inventory(12)
"""
        
        
        
            
        
    














'''import random

bikes = {
    "atlas":(10,93), 
    "slr":(13,78),
    "bmx":(8,140)
    }

bike1=bicycle(


# or
bikes_list= ["atlas","slr","bmx"]
print "intializing bikes"

class bicycle:
    models=[]
    def __init__(self,model_name,weight,cost):
        self.name=model_name
        self.weight = weight
        self.cost=cost
        bicycle.models.append(self)
        
class shops:
    def __init__(self,name,num_bikes,margin):
        self.name = name
        self.bikes=int(num_bikes)
        self.margin = margin
    #def build_inventory():
     #   for i in range(0,self.bikes):
     
bike1 = bicycle(bikes_list[0], random.randrange(8,20), random.randrange(70,200))
print "bike name: %r, weight: %r, cost: %r" % (bike1.name,bike1.weight, bike1.cost)
'''


