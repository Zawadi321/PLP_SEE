#LIFO (stack)
#-----------
#|50|
#|40|
#|30|
#|20|
stack = []

# Adding items to the stack
stack.append(10) # Push 10 onto the stack
stack.append(20) # Push 20 onto the stack
stack.append(30) # Push 30 onto the stack
stack.append(40) # Push 40 onto the stack
stack.append(50) # Push 50 onto the stack
print(stack) # Output: [10, 20, 30, 40, 50]
print(stack[1]) # Output: 20 (First item added)
print(stack[-1]) # Output: 50 (Last item added)

#removing the first item(LIFO)
stack.pop() # Pop the last item (50) from the stack
print(stack) # Output: [10, 20, 30, 40]


#Queue (FIFO)
#-----------
#front -->[A, B, C, D, E] --> rear

from collections import deque # Create a queue using deque
queue = deque() # Adding items to the queue
# Enqueue items to the queue(Adding items to the rear)
queue.append('A') # Enqueue 'A'
queue.append('B') # Enqueue 'B'
queue.append('C') # Enqueue 'C'
print(queue.popleft()) # Output: A (Dequeue 'A' from the front)
