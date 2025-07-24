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
        curr = self.head #start from the head of the linked list (curr is a temporary variable to traverse the list)

        while curr:
            print(curr.data, end=" -> ") #attahed to the end of the current node's data
            curr = curr.next # #move to the next node in the linked list
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
            self.data = data #value stored in the node
            self.prev = None #pointer to the previous node
            self.next = None #pointer to the next node

    class DoublyLinkedList:
        def __init__(self):
            self.head = None

        def insert_front(self, data):
            new_node = DNode(data)
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node

        def print_list(self):
            curr = self.head
            while curr:
                print(curr.data, end=" <-> ")
                curr = curr.next
            print("None")   #indicates the end of the doubly linked list
    
    if __name__ == "__main__":
        dll = DoublyLinkedList()
        dll.insert_front(10)
        dll.insert_front(20)
        dll.insert_front(30)
        dll.insert_front(40)
        dll.insert_front(50)

        dll.print_list()  # Output: 50 <-> 40 <-> 30 <-> 20 <-> 10 <-> None
        # Doubly linked lists are useful for applications where bidirectional traversal is needed, such as
        # in implementing navigation systems, undo/redo functionality, and more complex data structures like deques.
        # and require more control over memory usage.
        # They allow for efficient insertions and deletions at both ends of the list.
        # and require more control over memory usage.


#Node holds data and pointers to the next node in the sequence.
# -Data= value of the node (eg 10, apple, x)
# -Next= pointer to the next node in the sequence (eg next node with value 20)
    #Example:
      #[10 | next] -> [20 | next] -> [30 | next] -> [40 | next] -> [50 | None]

# -Head= pointer to the first node in the linked list (eg first node with value 10)
# -Tail= pointer to the last node in the linked list (eg last node with value 50)
# -Linked lists are useful for applications where frequent insertions and deletions are required, such

