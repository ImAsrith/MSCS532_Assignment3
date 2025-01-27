# Analysis on Randomized Quicksort and Hash Table

## Part 1: Randomized Quicksort

### Overview
Implementation and comparison of two QuickSort variations:
- Classic QuickSort (first element as pivot)
- Enhanced QuickSort (random pivot selection)

### Running QuickSort Demo
```python
python quicksort.py
```

### Key Findings
The performance analysis revealed:
- Enhanced QuickSort showed better performance on already sorted and reverse-sorted arrays
- Both implementations performed similarly on random data
- Random pivot selection helped avoid worst-case scenarios (O(n²)) that occur with sorted arrays in classic QuickSort
- Classic QuickSort showed slightly better performance on small arrays due to less overhead

---

## Part 2: Hash Table Implementation

### Overview
A Python implementation of a hash table using separate chaining for collision resolution. The table automatically resizes when the load factor exceeds 0.7 to maintain efficient operations.

### Key Features
- Separate chaining for collision handling
- Dynamic resizing
- Basic operations: add, remove, search
- Built-in visualization method

### Implementation Summary
The hash table implementation shows several interesting findings:
1. Performance remains consistent with load factor management:
   - Operations maintain O(1) average time complexity
   - Automatic resizing prevents performance degradation

2. Collision handling:
   - Separate chaining effectively manages hash collisions
   - Each bucket can grow independently as needed

3. Memory usage:
   - Scales dynamically with data volume
   - Trade-off between memory usage and collision prevention

### Usage Example
```python
# Create and use hash table
hash_map = HashTable()
hash_map.add("apple", 1)
hash_map.add("banana", 2)

# Retrieve values
value = hash_map.get("apple")  # Returns 1

# Remove entries
hash_map.remove("banana")

# Display current state
hash_map.print_table()
```

### Running Hash Table Demo
```bash
python hash_table.py
```