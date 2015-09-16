class Algos(object):
    pass
    purpose="execution"
    def __init__(self, name):
        self.name=name
        self.strategies=[]
    def add_strat(self, strat):
        self.strategies.append(strat)
        
a=Algos("Cover")
a.add_strat("extremes")
a.add_strat("mmk")
a.add_strat("liquidate")
print a.name,a.strategies
