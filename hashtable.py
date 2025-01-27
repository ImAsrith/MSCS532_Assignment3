class HashTable:
    def __init__(self, initial_size=10):
        """
        Creates a new hash table with specified initial capacity.
        Implements collision handling through chaining method.
        """
        self.max_size = initial_size
        self.element_count = 0
        self.buckets = [[] for _ in range(initial_size)]

    def _get_index(self, key):
        """
        Generates bucket index for a given key.
        Utilizes Python's hash function with size-based normalization.
        """
        return hash(key) % self.max_size

    def add(self, key, value):
        """
        Adds or updates an entry in the hash table.
        Automatically expands table when load threshold is reached.
        """
        bucket_idx = self._get_index(key)
        
        # Update existing key if found
        for item in self.buckets[bucket_idx]:
            if item[0] == key:
                item[1] = value
                return

        # Add new entry
        self.buckets[bucket_idx].append([key, value])
        self.element_count += 1

        # Expand table if load factor exceeds threshold
        if self.element_count / self.max_size > 0.7:
            self._expand_table()

    def get(self, key):
        """
        Retrieves value associated with given key.
        Returns None if key doesn't exist.
        """
        bucket_idx = self._get_index(key)
        for item in self.buckets[bucket_idx]:
            if item[0] == key:
                return item[1]
        return None

    def remove(self, key):
        """
        Removes entry with specified key.
        Returns True if removed, False if not found.
        """
        bucket_idx = self._get_index(key)
        for item in self.buckets[bucket_idx]:
            if item[0] == key:
                self.buckets[bucket_idx].remove(item)
                self.element_count -= 1
                return True
        return False

    def _expand_table(self):
        """
        Expands table capacity and redistributes entries.
        Maintains performance by keeping load factor balanced.
        """
        expanded_size = self.max_size * 2
        new_buckets = [[] for _ in range(expanded_size)]
        
        # Redistribute existing entries
        for chain in self.buckets:
            for key, value in chain:
                new_idx = hash(key) % expanded_size
                new_buckets[new_idx].append([key, value])
        
        self.max_size = expanded_size
        self.buckets = new_buckets

    def print_table(self):
        """
        Outputs current table state for debugging.
        Shows contents of each bucket.
        """
        for idx, chain in enumerate(self.buckets):
            print(f"Bucket {idx}: {chain}")


if __name__ == "__main__":
    # Demo implementation
    hash_map = HashTable()
    
    # Populate table
    test_data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4,
        "elderberry": 5,
        "fig": 6
    }
    
    for k, v in test_data.items():
        hash_map.add(k, v)
    
    print("Initial table state:")
    hash_map.print_table()
    
    # Demonstrate lookups
    print("\nLookup results:")
    for item in ["apple", "fig", "grape"]:
        print(f"Looking up '{item}': {hash_map.get(item)}")
    
    # Demonstrate deletions
    print("\nRemoving items:")
    for item in ["banana", "grape"]:
        print(f"Removing '{item}': {hash_map.remove(item)}")
    
    print("\nFinal table state:")
    hash_map.print_table()