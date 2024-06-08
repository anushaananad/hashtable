from hash_table import HashTable

def main():
    hash_table = HashTable()

    #insert
    hash_table.insert("apple", 1)
    hash_table.insert("banana", 2)
    hash_table.insert("orange", 3)
    hash_table.insert("abnana", 4)

    print("Hash table:", hash_table)

    #search
    print("Searching for apple:",hash_table.search("apple"))
    print("Searching for grape:",hash_table.search("grape"))

    #delete
    hash_table.delete("orange")
    print("After deletion, Searching for orange:",hash_table.search("orange"))

    print("Hash table:", hash_table)

if __name__ == "__main__":
    main()