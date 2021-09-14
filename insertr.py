# Data_structures-LinkedList
class Node:
    def __init__(self, v = None):#creates a node of a linkedlist using class
        self.value = v
        self.next = None
        return

    def isempty(self): #checks if the linked list is empty
        if self.value == None:
            return(True)
        else:
            return(False)

    def append(self,v):   # append, recursive
        if self.isempty():
            self.value = v
        elif self.next == None:
            newnode = Node(v)
            self.next = newnode
        else:
            self.next.append(v)
        return
    def __str__(self): #convert the linkedlist into a list to print
        selflist = []
        if self.value == None:
            return(str(selflist))

        temp = self
        selflist.append(temp.value)
        
        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)

        return(str(selflist))
    
l = Node(10)
print(l)
l.next = Node(20)
print(l)
