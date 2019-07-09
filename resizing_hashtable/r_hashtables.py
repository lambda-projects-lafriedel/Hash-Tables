'''
Your assignment is to upgrade your basic hash table to handle collisions with linked list chaining. You should be able to insert an arbitrary amount of elements into your hash table, regardless of table size, and read them back without any data loss. You should also implement a resizing function that doubles the size of your hash table and copies all elements into the new data structure.
'''

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __str__(self):
        return f"key: {self.key}, value: {self.value}, next: {self.next}"


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    num = 5381
    for char in string:
        num = (num * 33) + ord(char)
    
    return num % max

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    # hash the key
    index = hash(key, hash_table.capacity)
    
    # create a LL pair of the key/value
    list_node = LinkedPair(key, value)

    # check if index has ll pair at it already
    curr_item = hash_table.storage[index]
    
    # if no curr_item
    if curr_item is None:
        # set the index as the list_node
        hash_table.storage[index] = list_node
    else:
        # while curr_item is not None and that item's key does not equal the to-be-inserted key
        while curr_item and curr_item.key is not key:
            # set prev as the curr_item and curr_item as its next item
            prev, curr_item = curr_item, curr_item.next
        # if curr_item:
        #     print("INSIDE IF", curr_item)
        #     curr_item.value = value
        # else:
        prev.next = list_node

    for i in range(len(hash_table.storage)):
        print(i, hash_table.storage[i])


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    # print(hash_table_retrieve(ht, "line_1"))
    # print(hash_table_retrieve(ht, "line_2"))
    # print(hash_table_retrieve(ht, "line_3"))

    # old_capacity = len(ht.storage)
    # ht = hash_table_resize(ht)
    # new_capacity = len(ht.storage)

    # print("Resized hash table from " + str(old_capacity)
    #       + " to " + str(new_capacity) + ".")


Testing()
