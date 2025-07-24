# Index:0  1   2   3   4 (5 elements)
#array:[5, 10, 15, 20, 25]

#arr[2]=15
#arrays are fast for lookups (they have a constant time complexity O(1) for accessing elements by index)
#used in many applications like databases, image pixelation, audio buffers,leaderboards, game states, etc.

#Define an array(list in Python)
arr=[10, 20, 30, 40, 50]
#access
print(arr[2])  # Output: 30

#update (replacing an element)
arr[2]=55
print(arr[2])  # Output: 55

#Insert at the end
arr.append(60)
print(arr)  # Output: [10, 20, 55, 40, 50, 60]

#insert at a specific index
arr.insert(2, 25)
print(arr)  # Output: [10, 20, 15, 55, 40, 50, 60]

#delete an element
arr.pop(3)  # Removes the element at index 3 (55)       
print(arr)  # Output: [10, 20, 25, 40, 50, 60]

#search for a value
if 40 in arr:
    print("found 40")  # Output: found 40
    
# Arrays in Python (using lists)
# Python lists are dynamic arrays, meaning they can grow and shrink in size.
# They can hold elements of different data types, but they are not as memory efficient as static arrays in languages like C or Java.
# Lists in Python are implemented as dynamic arrays, which means they can grow and shrink in size
# and can hold elements of different data types.
# Example of a dynamic array in Python
# Dynamic array example
dynamic_array = [1, 2, 3]
dynamic_array.append(4)  # Add an element
dynamic_array.append(5)  # Add another element
print(dynamic_array)  # Output: [1, 2, 3, 4, 5]
# Example of a static array in Python (using the array module)
import array
static_array = array.array('i', [1, 2, 3])  # 'i' indicates an array of integers
static_array.append(4)  # Add an element
static_array.append(5)  # Add another element

print(static_array)  # Output: array('i', [1, 2, 3, 4, 5])
# Output: array('i', [1, 2, 3, 4, 5])
# Note: The array module is less commonly used in Python compared to lists, as lists are
# more versatile and easier to work with for most applications.
# Output: array('i', [1, 2, 3, 4, 5])
# However, the array module can be useful when you need to work with large amounts of data