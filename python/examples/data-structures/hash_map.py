# Simple implementation of a hash map (also known as a dictionary in Python) using separate chaining for handling collisions:

# The HashMap class implements a basic hash map using separate chaining to handle collisions.
# The _hash method calculates the hash value of a given key and maps it to an index in the hash map.
# The put method inserts a key-value pair into the hash map. If the key already exists, it updates the corresponding value.
# The get method retrieves the value associated with a given key from the hash map.
# The remove method removes a key-value pair from the hash map based on the given key.
# Example usage demonstrates how to use the HashMap class to insert, retrieve, update, and remove key-value pairs.

class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.hash_map = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for pair in self.hash_map[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.hash_map[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.hash_map[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.hash_map[index]):
            if pair[0] == key:
                del self.hash_map[index][i]
                return
        raise KeyError(f"Key '{key}' not found")


# Example usage:
if __name__ == "__main__":
    hashmap = HashMap()

    # Inserting key-value pairs
    hashmap.put("apple", 10)
    hashmap.put("banana", 20)
    hashmap.put("orange", 30)

    # Retrieving values
    print("Value for key 'apple':", hashmap.get("apple"))  # Output: Value for key 'apple': 10
    print("Value for key 'banana':", hashmap.get("banana"))  # Output: Value for key 'banana': 20
    print("Value for key 'orange':", hashmap.get("orange"))  # Output: Value for key 'orange': 30

    # Updating value
    hashmap.put("apple", 15)
    print("Updated value for key 'apple':", hashmap.get("apple"))  # Output: Updated value for key 'apple': 15

    # Removing key-value pair
    hashmap.remove("banana")
    try:
        print("Value for key 'banana':", hashmap.get("banana"))
    except KeyError as e:
        print(e)  # Output: Key 'banana' not found
