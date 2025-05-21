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
        print("Number="+str(number))
        if self.head == None:
            self.head=newNode
            self.tail=newNode
        else:
            if number<self.head.get_data():
                newNode.set_next(self.head)
                self.head.set_previous(newNode)
                self.head=newNode
            else:
                curNode=self.head
                nextNode=self.head.get_next()
                while number > curNode.get_data() and number > nextNode.get_data() and nextNode !='None':
                    print("greater than")
                    curNode=curNode.get_next()
                    nextNode=curNode.get_next()
                curNode.set_next(newNode)
                newNode.set_previous(curNode)
                newNode.set_next(nextNode)
                nextNode.set_previous(newNode)
        pass
    
    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        # TODO: Type your code here
        return False