from NumberList import NumberList
from NumberListNode import NumberListNode

class SortedNumberList(NumberList):
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        newNode = NumberListNode(number)
        nextNode=NumberListNode(None)
        #check for an empty list
        if self.head == None:
            self.head=newNode
            self.tail=newNode
        else:
            #check to see if it needs to be entered at the beginning of list
            if number<self.head.get_data():
                newNode.set_next(self.head)
                self.head.set_previous(newNode)
                self.head=newNode
            else:
                #find spot after the head
                curNode=self.head
                nextNode=self.head.get_next()
                while number > curNode.get_data() and number > nextNode.get_data() and nextNode !='None':
                    print("greater than")
                    curNode=curNode.get_next()
                    nextNode=curNode.get_next()
                #after spot is found, insert the node
                curNode.set_next(newNode)
                newNode.set_previous(curNode)
                newNode.set_next(nextNode)
                nextNode.set_previous(newNode)
        pass
    
    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        #search for node within the list, start with list
        if self.head != None:
            curNode=self.head
        else:
            return False
        
        while curNode.get_data() != number and curNode.get_next() != None:
            curNode=curNode.get_next()

        if curNode.get_data != number and curNode.get_next()== None:
            return False
        
        #The node was found and can now be deleted
        if curNode is self.head:
            self.head = curNode.get_next()
        if curNode is self.tail:
            self.tail = curNode.get_previous()
        else:
            preDec=curNode.get_previous()
            succ=curNode.get_next()
            preDec.set_next(succ)
            succ.set_previous(preDec)

        return True