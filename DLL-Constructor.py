class Node:
    def __init__(self, value):
        self.value = value
        self.next = None #arrow pointing right
        self.prev = None #arrow pointing left
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # Pointing the tail of the last node added to the list to the "new_node"
            new_node.prev = self.tail # The pointer to the previous node "prev" will point where "tail" is pointing 
            self.tail = new_node
        self.length += 1
        return True 

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev # the previous relative to what tail was pointing 
            self.tail.next = None # Break the connection ->
            temp.prev = None # Break the connection <-
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0: #length is zero
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True 

    def popfirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None 
        temp = self.head 
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def print_list(self): # Add the temp.value to check the value inside the nodes
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(11)
my_doubly_linked_list.append(21)
my_doubly_linked_list.append(31)
my_doubly_linked_list.get(0)

my_doubly_linked_list.print_list()




