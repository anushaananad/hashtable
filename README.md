# hashtable
Hash Table using Arrays in python

## About Hash Tables:
HashTable:
- A hash table is a type of data structure in which the index value of the key (pair(key, vlaue)) is generated from a hash function.
- Time complexity of O(1) for search, insertion, and deletion operations.

Hash Function: 
- A function that takes an input (key) and returns an index in the array.

Array (Bucket Array): 
- An array where the hash table stores key-value pairs. Each index in the array is called a bucket.

Chaining: 
- Each bucket contains a list of all elements that hash to the same index.


## Explanation of the Implementation:
Initialization:
- The HashTable class is initialized with a specified size (default 5).
- The table is an array of empty lists, each representing a bucket for chaining.

Hash Function:
- Sums the ASCII values of the characters in the key and takes the modulo with the table size to determine the index.

Insert Method:
- Computes the index using the hash function.
- Checks if the key already exists in the chain; if so, updates the value. - If the key does not exist, appends the new key-value pair to the list at the index.

Search Method:
- Computes the index using the hash function.
- Iterates through the list at the computed index to find the key and return its value.
- Returns None if the key is not found.

Delete Method:
- Computes the index using the hash function.
- Iterates through the list at the computed index to find the key and remove the key-value pair.

String Representation:
- Provides a string representation of the hash table for debugging.

## Requirements
- Python 3.6+
- `pytest` (for running tests)
