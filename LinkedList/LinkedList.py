from LinkedList.node import Node

class LinkedList:
    def init(self):
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

print(ll.includes(5))

print(ll)  