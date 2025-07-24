#Singly Linked list :An individual node of a linked list contains data and a reference to the next node in the sequence.# and require more control over memory usage.
# Example of a static array in Python (using the array module)
#"self"(a reference to the current instance of the class) is the node having data and pointing to the next node in the sequence.
#arr = [X10->, []20, []30, []40, []50]
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #none indicates that there is no next node yet(or it is the last node in the list)

class LinkedList:
    def __init__(self):
        self.head=None #head is the first node in the linked list
    
    #add a new node to the front of the linked list
    def insert_front(self, data):
        new_node = Node(data) #inserting a new node at the beginning of the list
        new_node.next = self.head #the new node's next points to the current head
        self.head = new_node #the head now points to the new node

        #print the linked list
    def print_list(self):
        curr = self.head

        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None") #indicates the end of the linked list


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_front(10)
    ll.insert_front(20)
    ll.insert_front(30)
    ll.insert_front(40)
    ll.insert_front(50)

    ll.print_list()  # Output: 50 -> 40 -> 30 -> 20 -> 10 -> None
    # Linked lists are useful for applications where frequent insertions and deletions are required, such as in implementing queues, stacks, and adjacency lists for graphs.
    # They allow for dynamic memory allocation and can grow or shrink in size as needed.
    #LIFO (Last In First Out)

    #Double Linked List: A node contains a reference to the next node and the previous node in the sequence.
    # This allows traversal in both directions, making it more flexible than a singly linked list.
    # However, it requires more memory due to the additional pointer for the previous node.

    class DNode:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None