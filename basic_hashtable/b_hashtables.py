

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return f"{self.key}, {self.value}"

# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function

# '''
def hash(string, max):
    # not sure how/why to incorporate "max"
    print("MAX", max)
    num = 5381
    for char in string:
        num = (num * 33) + ord(char)
    
    # if num >= max:
    #     print("Hashed key is out of range")
    #     return None
    # else:
    return num % max

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # hash and modulo the key to get the index
    index = hash(key, hash_table.capacity)
    print("INDEX IN INSERT", index)

    # create new Pair from index and value -- not sure how to utilize this properly?
    pair = Pair(index, value)
    print("PAIR", pair)

    # if key already has a value, print a warning -- collision to be dealt with later
    if hash_table.storage[pair.key] is not None:
        print("WARNING: Value will be overridden!")

    # insert value at given index, even if existing value is not None
    hash_table.storage[pair.key] = pair.value

    # printing just to see process when running tests
    print("STORAGE IN INSERT")
    for i in range(len(hash_table.storage)):
        print(i, hash_table.storage[i])
    


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # hash and modulo the key to get the index
    index = hash(key, hash_table.capacity)
    print("INDEX IN REMOVE", index)

    # if the value at the given index is none print warning
    if hash_table.storage[index] is None:
        print("WARNING: No value to remove!")
    # else set the value to None
    else:
        hash_table.storage[index] = None

    # printing just to see process when running tests
    print("STORAGE IN REMOVE")
    for i in range(len(hash_table.storage)):
        print(i, hash_table.storage[i])


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    # hash and modulo the key to get the index
    index = hash(key, hash_table.capacity)
    print("INDEX IN RETRIEVE", index)
    
    # if the value at that index is None return None
    if hash_table.storage[index] is None:
        return None
    # else return the value
    else:
        return hash_table.storage[index]


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
