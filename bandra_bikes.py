from sys import exit
import random
class Bicycles():
    def __init__(self):
        self.models=['atlas','bmx','slr']
        self.weights={'atlas':10,'bmx':13,'slr':8}
        self.cost={'atlas':93,'bmx':78,'slr':129}
        self.num_models =len (self.models)
        
class Shops(Bicycles):
    def inventory(self,number):
        bikes_available=[]
        inventory_cost=0
        for i in range(0,number/self.num_models):
            for k in self.models:
               bikes_available.append(k)
               inventory_cost+=self.cost[k]  
        return bikes_available, inventory_cost
    
       
    def sales_ftd(self,bikes, inventory):
        sales = 0
        profit = 0
        margin = int(raw_input("What % profit margin did we set: "))
        print "We sold %s bikes today" % bikes
        for i in range(0,bikes):
            sell_index = random.randrange(0,len(inventory)-1)
            sell = inventory[sell_index]
            cost_price=self.cost[sell]
            sell_price= self.cost[sell] * (1+(margin/100.0))
            print "Sale #%s was %s" % (i+1,sell)
            print "its cost was %s" % cost_price
            print "it was sold for %s" % sell_price
            profit += sell_price-cost_price
            print "Total profit for day upto this sale is %s" % profit 
            inventory.pop(sell_index)
        return inventory, profit
            
        
industry = Bicycles()
print "models: ", industry.models
print "models and thier weights: ", industry.weights
print "models and their cost: ", industry.cost
for i in industry.models:
    print "%s model has weight: %s and costs %s" % (i,industry.weights[i],industry.cost[i])

shop1=Shops()
print "shop1.models: ",shop1.models
shop1_inventory, shop1_cost = shop1.inventory(12)
print "shop1_inventory: ", shop1_inventory
print "shop1_cost: ", shop1_cost
shop1_inventory, shop1_profit = shop1.sales_ftd(5,shop1_inventory)
print "shop1_inventory after sale: ", shop1_inventory
print "shop1_profit: ", shop1_profit


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


