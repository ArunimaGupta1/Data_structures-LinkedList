class Node:
    def __init__(self,initval = None):
        self.value = initval
        self.next = None

    def isempty(self):
        return(self.value==None)

    def insert(self,v):
        if self.isempty():
            self.value = v
            return()

        newnode = Node(v)
        (self.value,newnode.value) = (newnode.value,self.value)
        (newnode.next,self.next) = (self.next,newnode)
        return()

    def __str__(self):
        s = []
        if self.value == None:
            return(str(s))
        temp = self
        s.append(temp.value)
        while temp.next is not None:
            temp = temp.next
            s.append(temp.value)
        return(str(s))

l = Node(10)
print(l)
l.next = Node(20)
print(l)
