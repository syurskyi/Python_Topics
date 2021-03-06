from pprint import pprint


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = None 

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def insertatEnd(self,item):
        current = self.head
        if current:
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(Node(item))
        else:
            self.head = Node(item)


    def size(self):
        current = self.head
        count = 0
        while current:
          count += 1
          current = current.get_next()
        return count 


    def modnodefromend(self, n):
            current=self.head
            modnode=None
     
            i=1
            if n <= 0:
               return None
     
            while current != None:
                  if i%n == 0:
                       modnode=current
                  i=i+1
                  current=current.next_node
     
            return modnode





    def __str__( self ) :
        s = ""
        p = self.head
        if p != None :
                while p.next_node != None :
                        s += p.data
                        p = p.next_node
                s += p.data
        return s


l = LinkedList()

l.insert( '250' )
l.insert( '200' )
l.insert( '100' )
l.insert( '25' )
l.insert( '20' )
l.insert( '10' )
print l
print(l.modnodefromend(3).data)
 
