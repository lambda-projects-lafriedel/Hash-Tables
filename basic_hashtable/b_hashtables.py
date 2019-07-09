

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
        # Note from class: apparently we should have a count?


# '''
# Fill this in.
# Research and implement the djb2 hash function

# '''
def hash(string, max):
    num = 5381
    for char in string:
        num = (num * 33) + ord(char)
    
    return num % max

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # hash and modulo the key to get the index
    index = hash(key, hash_table.capacity)
    print("INDEX IN INSERT", index)

    # create new Pair from key and value
    pair = Pair(key, value)
    print("PAIR", pair)

    # Addition from class: need to grab stored pair, if it exists
    stored_pair = hash_table.storage[index]

    # if index already has a pair, print a warning -- collision to be dealt with later
    if stored_pair is not None:
        # Addition from class: Need to check if the pair's key is equal to the stored pair's key
        if pair.key is not stored_pair.key:
            print("WARNING: Value will be overridden!")

    # insert value at given index, even if existing value is not None
    hash_table.storage[index] = pair

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
    if hash_table.storage[index] is None or hash_table.storage[index].key is not key:
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
        # print a warning
        print("Unable to find value with key " + key)
        return None
    # else, check if the stored index's key equals the key, and return the value
    else:
        if hash_table.storage[index].key == key:
            return hash_table.storage[index].value


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
