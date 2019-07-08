

# Do not use any of the built in array functions for this exercise
class array:
    def __init__(self, capacity):
        '''
        What do we need in our array to make it work?
        Determine capacity
        Determine current size
        Allocate memory
        Values being stored in array
        '''
        self.capacity = capacity # Max size the array can be
        self.count = 0 # Current size being used
        self.elements = [None] * capacity # Instantiate empty cells


# Double the size of the given array
def resize_array(array):
    '''
    If we double it in size every time, it means we wouldn't always need to reallocate when something is appended
    '''
    new_capacity = array.capacity * 2 # double the current capacity
    new_elements = [None] * new_capacity # double the amount of cells

    # loop over count since that's the current size
    for i in range(array.count): 
        new_elements[i] = array.elements[i]
    
    # set elements and capacity as new values
    array.elements = new_elements
    array.capacity = new_capacity


# Return an element of a given array at a given index
def array_read(array, index):
    '''
    We know we're out of bounds if the index is greater than the array.count
    '''
    # Throw an error if array is out of the current count
    if index >= array.count:
        print("Read Error: out of bounds")
        return None
    
    return array.elements[index]


# Insert an element in a given array at a given index
def array_insert(array, element, index):
    # Throw an error if array is out of the current count
    if index > array.count:
        print("Insert Error: Out of bounds")
        return None

    # Resize the array if the number of elements is over capacity
    if array.capacity <= array.count:
        resize_array(array)

    # Move the elements to create a space at 'index' -- needs to move anything to the right of index
    # Start at the end of the array and go backwards, stopping at the index point
    for i in range(array.count, index, -1):
        array.elements[i] = array.elements[i-1]

    # Add the new element to the array and update the count
    array.elements[index] = element
    array.count += 1


# Add an element to the end of the given array
def array_append(array, element):

    # Hint, this can be done with one line of code
    # (Without using a built in function)

    array_insert(array, element, array.count)


# Remove the first occurence of the given element from the array
# Throw an error if the value is not found
def array_remove():
    # Your code here
    pass


# Remove the element in a given position and return it
# Then shift every element after that occurrance to fill the gap
def array_pop():
    # Throw an error if array is out of the current count
    # Your code here
    pass


# Utility to print an array
def array_print(array):
    string = "["
    for i in range(array.count):
        string += str(array.elements[i])
        if i < array.count - 1:
            string += ", "

    string += "]"
    print(string)


# Testing
arr = array(1)

array_insert(arr, "STRING1", 0)
array_print(arr)
# array_pop(arr, 0)
# array_print(arr)
array_insert(arr, "STRING1", 0)
array_append(arr, "STRING4")
# array_insert(arr, "STRING2", 1)
# array_insert(arr, "STRING3", 2)
array_print(arr)
