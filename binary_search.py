class Node: #creates a class called Node
    def __init__(self,val): # def initialization on self with val passed thru
        self.l_child = None # create empty variable l.child
        self.r_child = None # create empty variable r.child
        self.data = val # data assigned pass thru value val
        
def binary_insert(root,node):
    if root is None:
        root = node
    else:
        
        if root.data > node.data:
            
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child,node)
                
def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)

r=None
#print "assigning r = Node(3)" ; r = Node(3)
#print "printing values of r.data: %s, r.l_child: %s, r.r_child: %s " % (r.data, r.l_child, r.r_child)
binary_insert(r, Node(7))
binary_insert(r, Node(1))
binary_insert(r, Node(5))    
#in_order_print(r)                
                
                