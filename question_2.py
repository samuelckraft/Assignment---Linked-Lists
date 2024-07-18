#Task 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


#Task 2

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data) 
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, data):
        current = self.head 
        prev = None

        while current: 
            if current.data == data: 
                if prev: 
                    prev.next = current.next
                else:
                    self.head = current.next

                if current.next is None: 
                    self.tail = prev 
                return True
            
            prev = current 
            current = current.next
        return False
    
    def __iter__(self): 
        current = self.head
        while current:
            yield current.data
            current = current.next

    def traversal(self):
        print("Linked list elements:")
        for data in self:
            print(data, end=' <-> ')
        print("None")

#Task 3

my_doubly_linked_list = DoublyLinkedList()

my_doubly_linked_list.append('1')
my_doubly_linked_list.append('2')
my_doubly_linked_list.append('3')

my_doubly_linked_list.delete('2')

my_doubly_linked_list.traversal()