import unittest

from r_hashtables import (HashTable,
                          hash_table_insert,
                          hash_table_remove,
                          hash_table_retrieve,
                          hash_table_resize)


class TestFullHashTable(unittest.TestCase):

    def test_hash_table_insertion_and_retrieval(self):
        ht = HashTable(8)

        hash_table_insert(ht, "key-0", "val-0")
        hash_table_insert(ht, "key-1", "val-1")
        hash_table_insert(ht, "key-2", "val-2")
        hash_table_insert(ht, "key-3", "val-3")
        hash_table_insert(ht, "key-4", "val-4")
        hash_table_insert(ht, "key-5", "val-5")
        hash_table_insert(ht, "key-6", "val-6")
        hash_table_insert(ht, "key-7", "val-7")
        hash_table_insert(ht, "key-8", "val-8")
        hash_table_insert(ht, "key-9", "val-9")

        return_value = hash_table_retrieve(ht, "key-0")
        self.assertTrue(return_value == "val-0")
        return_value = hash_table_retrieve(ht, "key-1")
        self.assertTrue(return_value == "val-1")
        return_value = hash_table_retrieve(ht, "key-2")
        self.assertTrue(return_value == "val-2")
        return_value = hash_table_retrieve(ht, "key-3")
        self.assertTrue(return_value == "val-3")
        return_value = hash_table_retrieve(ht, "key-4")
        self.assertTrue(return_value == "val-4")
        return_value = hash_table_retrieve(ht, "key-5")
        self.assertTrue(return_value == "val-5")
        return_value = hash_table_retrieve(ht, "key-6")
        self.assertTrue(return_value == "val-6")
        return_value = hash_table_retrieve(ht, "key-7")
        self.assertTrue(return_value == "val-7")
        return_value = hash_table_retrieve(ht, "key-8")
        self.assertTrue(return_value == "val-8")
        return_value = hash_table_retrieve(ht, "key-9")
        self.assertTrue(return_value == "val-9")

    def test_hash_table_insertion_overwrites_correctly(self):
        ht = HashTable(8)

        hash_table_insert(ht, "key-0", "val-0")
        hash_table_insert(ht, "key-1", "val-1")
        hash_table_insert(ht, "key-2", "val-2")
        hash_table_insert(ht, "key-3", "val-3")
        hash_table_insert(ht, "key-4", "val-4")
        hash_table_insert(ht, "key-5", "val-5")
        hash_table_insert(ht, "key-6", "val-6")
        hash_table_insert(ht, "key-7", "val-7")
        hash_table_insert(ht, "key-8", "val-8")
        hash_table_insert(ht, "key-9", "val-9")

        hash_table_insert(ht, "key-0", "new-val-0")
        hash_table_insert(ht, "key-1", "new-val-1")
        hash_table_insert(ht, "key-2", "new-val-2")
        hash_table_insert(ht, "key-3", "new-val-3")
        hash_table_insert(ht, "key-4", "new-val-4")
        hash_table_insert(ht, "key-5", "new-val-5")
        hash_table_insert(ht, "key-6", "new-val-6")
        hash_table_insert(ht, "key-7", "new-val-7")
        hash_table_insert(ht, "key-8", "new-val-8")
        hash_table_insert(ht, "key-9", "new-val-9")

        return_value = hash_table_retrieve(ht, "key-0")
        self.assertTrue(return_value == "new-val-0")
        return_value = hash_table_retrieve(ht, "key-1")
        self.assertTrue(return_value == "new-val-1")
        return_value = hash_table_retrieve(ht, "key-2")
        self.assertTrue(return_value == "new-val-2")
        return_value = hash_table_retrieve(ht, "key-3")
        self.assertTrue(return_value == "new-val-3")
        return_value = hash_table_retrieve(ht, "key-4")
        self.assertTrue(return_value == "new-val-4")
        return_value = hash_table_retrieve(ht, "key-5")
        self.assertTrue(return_value == "new-val-5")
        return_value = hash_table_retrieve(ht, "key-6")
        self.assertTrue(return_value == "new-val-6")
        return_value = hash_table_retrieve(ht, "key-7")
        self.assertTrue(return_value == "new-val-7")
        return_value = hash_table_retrieve(ht, "key-8")
        self.assertTrue(return_value == "new-val-8")
        return_value = hash_table_retrieve(ht, "key-9")
        self.assertTrue(return_value == "new-val-9")

    # def test_hash_table_removes_correctly(self):
    #     ht = HashTable(8)

    #     hash_table_insert(ht, "key-0", "val-0")
    #     hash_table_insert(ht, "key-1", "val-1")
    #     hash_table_insert(ht, "key-2", "val-2")
    #     hash_table_insert(ht, "key-3", "val-3")
    #     hash_table_insert(ht, "key-4", "val-4")
    #     hash_table_insert(ht, "key-5", "val-5")
    #     hash_table_insert(ht, "key-6", "val-6")
    #     hash_table_insert(ht, "key-7", "val-7")
    #     hash_table_insert(ht, "key-8", "val-8")
    #     hash_table_insert(ht, "key-9", "val-9")

    #     hash_table_remove(ht, "key-9")
    #     hash_table_remove(ht, "key-8")
    #     hash_table_remove(ht, "key-7")
    #     hash_table_remove(ht, "key-6")
    #     hash_table_remove(ht, "key-5")
    #     hash_table_remove(ht, "key-4")
    #     hash_table_remove(ht, "key-3")
    #     hash_table_remove(ht, "key-2")
    #     hash_table_remove(ht, "key-1")
    #     hash_table_remove(ht, "key-0")

    #     return_value = hash_table_retrieve(ht, "key-0")
    #     self.assertTrue(return_value is None)
    #     return_value = hash_table_retrieve(ht, "key-1")
    #     self.assertTrue(return_value is None)
    #     return_value = hash_table_retrieve(ht, "key-2")
    #     self.assertTrue(return_value is None)
    #     return_value = hash_table_retrieve(ht, "key-3")
    #     self.assertTrue(return_value is None)
    #     return_value = hash_table_retrieve(ht, "key-4")
    #     self.assertTrue(return_value is None)
    #     return_value = hash_table_retrieve(ht, "key-5")
    #     self.assertTrue(return_value is None)
    #     return_value = hash_table_retrieve(ht, "key-6")
    #     self.assertTrue(return_value is None)
    #     return_value = hash_table_retrieve(ht, "key-7")
    #     self.assertTrue(return_value is None)
    #     return_value = hash_table_retrieve(ht, "key-8")
    #     self.assertTrue(return_value is None)
    #     return_value = hash_table_retrieve(ht, "key-9")
    #     self.assertTrue(return_value is None)

    # def hash_table_resize(self):
    #     ht = HashTable(8)

    #     hash_table_insert(ht, "key-0", "val-0")
    #     hash_table_insert(ht, "key-1", "val-1")
    #     hash_table_insert(ht, "key-2", "val-2")
    #     hash_table_insert(ht, "key-3", "val-3")
    #     hash_table_insert(ht, "key-4", "val-4")
    #     hash_table_insert(ht, "key-5", "val-5")
    #     hash_table_insert(ht, "key-6", "val-6")
    #     hash_table_insert(ht, "key-7", "val-7")
    #     hash_table_insert(ht, "key-8", "val-8")
    #     hash_table_insert(ht, "key-9", "val-9")

    #     ht = hash_table_resize(ht)

    #     self.assertTrue(len(ht.storage) == 16)

    #     return_value = hash_table_retrieve(ht, "key-0")
    #     self.assertTrue(return_value == "val-0")
    #     return_value = hash_table_retrieve(ht, "key-1")
    #     self.assertTrue(return_value == "val-1")
    #     return_value = hash_table_retrieve(ht, "key-2")
    #     self.assertTrue(return_value == "val-2")
    #     return_value = hash_table_retrieve(ht, "key-3")
    #     self.assertTrue(return_value == "val-3")
    #     return_value = hash_table_retrieve(ht, "key-4")
    #     self.assertTrue(return_value == "val-4")
    #     return_value = hash_table_retrieve(ht, "key-5")
    #     self.assertTrue(return_value == "val-5")
    #     return_value = hash_table_retrieve(ht, "key-6")
    #     self.assertTrue(return_value == "val-6")
    #     return_value = hash_table_retrieve(ht, "key-7")
    #     self.assertTrue(return_value == "val-7")
    #     return_value = hash_table_retrieve(ht, "key-8")
    #     self.assertTrue(return_value == "val-8")
    #     return_value = hash_table_retrieve(ht, "key-9")
    #     self.assertTrue(return_value == "val-9")


if __name__ == '__main__':
    unittest.main()
