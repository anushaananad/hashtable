import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashTable()

    def test_insert_and_search(self):
        self.hash_table.insert("apple", 1)
        self.assertEqual(self.hash_table.search("apple"), 1)
    
    def test_update_value(self):
        self.hash_table.insert("apple", 1)
        self.hash_table.insert("apple", 2)
        self.assertEqual(self.hash_table.search("apple"), 2)

    def test_delete(self):
        self.hash_table.insert("apple", 1)
        self.hash_table.delete("apple")
        self.assertIsNone(self.hash_table.search("apple"))

    def test_collision_handling(self):
        self.hash_table.insert("abc", 1)
        self.hash_table.insert("acb", 2)  # These keys should collide
        self.assertEqual(self.hash_table.search("abc"), 1)
        self.assertEqual(self.hash_table.search("acb"), 2)

if __name__ == "__main__":
    unittest.main()
