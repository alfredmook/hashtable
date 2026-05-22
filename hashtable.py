

def _hash_key(key: str, p: int = 53) -> int:
    """Hashes the key using the rolling polynomial algorithm.

    Arguments:
    - key: str
      The key to be hashed.
    - p: int
      A prime number used for the rolling polynomial algorithm

    Returns:
    - the hashed location (int)
    """
    total = 0
    for i, char in enumerate(key):
        total += ord(char) * p**i
    return total


class HashTable:
    """A hashtable without collision resolution.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with

    Attributes:
    - size: int
      The number of slots that the hash table has
    - length: int
      The number of records contained in the hash table
    """

    def __init__(self, size: int):
        self.size = size
        self.length = 0
        # Add your code here
        self.array = [None] * self.size

    def __repr__(self) -> str:
        return f"HashTable(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        self.length += 1
        self.array[_hash_key(key) % self.size] = value 

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        if self.array[_hash_key(key)] == None:
            raise KeyError
        return self.array[_hash_key(key)]

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        if self.array[_hash_key(key) % self.size] == None:
            raise KeyError
        self.array[_hash_key(key) % self.size] = None
        self.length -= 1


class HashTableLinearProbing(HashTable):
    """A hashtable that implements collision resolution using
    linear probing.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with
    """

    def __init__(self, size: int):
        super().__init__(size)
        # Add your code here

        

    def __repr__(self) -> str:
        return f"HashTableLinearProbing(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        index = _hash_key(key) % self.size
        start = index
        while (index + 1) % self.size != start:
            if self.array[index] is None:
                self.array[index] = (key, value)
                self.length += 1
                return
            existing_key, existing_value = self.array[index]
            if key == existing_key:
                self.array[index] = (key, value)
                self.length += 1
                return
            index = (index + 1) % self.size
        raise RuntimeError("Hash table is full!")

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        index = _hash_key(key) % self.size
        start = index
        while (index + 1) % self.size != start:
            if self.array[index] is None:
                raise KeyError(f"key {key} does not exist")
            existing_key, existing_value = self.array[index]
            if key == existing_key:
                return existing_value
            index = (index + 1) % self.size
        raise KeyError(f"key {key} does not exist")
        

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        index = _hash_key(key) % self.size
        start = index
        while (index + 1) % self.size != start:
            if self.array[index] is None:
                raise KeyError(f"key {key} does not exist")
            existing_key, existing_value = self.array[index]
            if key == existing_key:
                self.array[index] = None
                self.length -= 1
                return
            index = (index + 1) % self.size
        raise KeyError(f"key {key} does not exist")


class HashTableSeparateChaining(HashTable):
    """A hashtable that implements collision resolution using
    separate chaining.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with
    """

    def __init__(self, size: int):
        super().__init__(size)
        # Add your code here

    def __repr__(self) -> str:
        return f"HashTableLinearProbing(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        raise NotImplementedError

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        raise NotImplementedError

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        raise NotImplementedError
