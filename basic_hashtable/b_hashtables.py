

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function

# '''
def hash(string, max):
    # not sure how/why to incorporate "max"
    num = 5381
    for char in string:
        num = (num * 33) + ord(char)
    
    # if num >= max:
    #     print("Hashed key is out of range")
    #     return None
    # else:
    return num

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # hash the passed in value to get index value
    index = hash(value, hash_table.capacity) % hash_table.capacity
    print("INDEX", index)
    # feed k/v into Pair?
    pair = Pair(index, value)

    # if key already has a value, print a warning
    if hash_table.storage[index] is not None:
        print("WARNING: Value will be overridden!")

    # insert value at given index
    hash_table.storage[pair.key] = pair.value

    for i in range(len(hash_table.storage)):
        print(hash_table.storage[i])
    


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


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
