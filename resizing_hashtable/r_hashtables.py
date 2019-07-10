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
        # if there's an item with a matching key
        if curr_item:
            # override the value with the passed in value
            curr_item.value = value
        else:
            # else, since it's None, set it as the list_node
            prev.next = list_node


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # hash the key
    index = hash(key, hash_table.capacity)

    # grab the current item
    curr_item = hash_table.storage[index]

    # if it's none print a warning
    if curr_item is None:
        print("No items at this index")
    else:
        if curr_item.next is None:
            hash_table.storage[index] = None
        else:
            while curr_item.next is not None:
                if curr_item.next.key == key:
                    curr_item.next = curr_item.next.next

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    curr_item = hash_table.storage[index]
    # print("CURR ITEM", index, curr_item)
    # if the item at that index is not None
    if curr_item is not None:
        # while there's an item and its key and the passed in key don't match
        while curr_item and curr_item.key is not key:
            # check if the item's key is equal to the passed in key
            curr_item = curr_item.next
        # if the keys are equal
        if curr_item.key == key:
            # return the value
            return curr_item.value
    # else return None
    return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    # double the capacity
    new_table = HashTable(hash_table.capacity * 2)
    # save the current storage in a temp variable
    curr_storage = hash_table.storage
    # for each index in the old storage, if the value at index is not none
    for i in range(len(curr_storage)):
        if curr_storage[i] is not None:
            # for all LLpairs, rehash the key
            if curr_storage[i].next is None:
                #insert them to the new bigger hash table
                hash_table_insert(new_table, curr_storage[i].key, curr_storage[i].value)
            else:
                curr_item = curr_storage[i]
                while curr_item.next is not None:
                    hash_table_insert(new_table, curr_item.key, curr_item.value)
                    curr_item = curr_item.next
    
    return new_table


def Testing():
    ht = HashTable(2)

    # hash_table_insert(ht, "line_1", "Tiny hash table")
    # hash_table_insert(ht, "line_2", "Filled beyond capacity")
    # hash_table_insert(ht, "line_3", "Linked list saves the day!")

    # print(hash_table_retrieve(ht, "line_1"))
    # print(hash_table_retrieve(ht, "line_2"))
    # print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
