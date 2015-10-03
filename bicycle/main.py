from  bicycles import * 

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
shop_name = "Bandra Bikes"; shop_margin = 20; shop_inventory = 16
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
