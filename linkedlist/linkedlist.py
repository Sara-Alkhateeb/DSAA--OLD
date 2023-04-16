from linkedlist.node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):

        output = ""
        
        if self.head is None:
            output = "Empty LinkedList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} --> '
                current = current.next
            
            output += " None"
        return output
    
    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self,value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
        
    def __str__(self):
        output = ""
        if self.head is None:
            output = "Empty LinkedList"
        else:
            current = self.head
            while(current):
                output += f'{{ {current.value} }} -> '
                current = current.next

            output += "NULL"
        return output

ll = LinkedList()

ll.insert(3)
ll.insert(5)
ll.insert(2)

print(ll) 

print( f"Is number 5 exist : {ll.includes(5)}") 
print(f"Is number 4 exist : {ll.includes(4)}") 