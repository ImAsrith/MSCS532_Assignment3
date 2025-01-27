import random
import time

# Standard QuickSort implementation with first element pivot
def classic_quicksort(sequence, start, end):
    if start < end:
        # Get division point using first element
        split_point = classic_divide(sequence, start, end)
        classic_quicksort(sequence, start, split_point - 1)  # Handle left segment
        classic_quicksort(sequence, split_point + 1, end)    # Handle right segment

def classic_divide(sequence, start, end):
    anchor = sequence[start]  # Choose first element
    left_ptr = start + 1     # Track elements larger than pivot
    right_ptr = end          # Track elements smaller than pivot
    
    while True:
        while left_ptr <= right_ptr and sequence[left_ptr] <= anchor:
            left_ptr += 1
        while left_ptr <= right_ptr and sequence[right_ptr] > anchor:
            right_ptr -= 1
        if left_ptr <= right_ptr:
            sequence[left_ptr], sequence[right_ptr] = sequence[right_ptr], sequence[left_ptr]
        else:
            break
    
    sequence[start], sequence[right_ptr] = sequence[right_ptr], sequence[start]
    return right_ptr

# Random QuickSort with random pivot selection
def random_quicksort(sequence, start, end):
    if start < end:
        # Use random pivot for better average performance
        split_point = random_divide(sequence, start, end)
        random_quicksort(sequence, start, split_point - 1)  # Process left portion
        random_quicksort(sequence, split_point + 1, end)    # Process right portion

def random_divide(sequence, start, end):
    # Select random pivot for improved performance
    random_idx = random.randint(start, end)
    sequence[start], sequence[random_idx] = sequence[random_idx], sequence[start]
    return classic_divide(sequence, start, end)

# Performance evaluation framework
def compare_quicksorts():
    # Test scenarios
    test_cases = {
        "Random Sequence": [random.randint(0, 1000) for _ in range(100)],
        "Ascending Sequence": list(range(100)),
        "Descending Sequence": list(range(100, 0, -1)),
        "Uniform Sequence": [42] * 100,
        "Singleton Sequence": [1],
        "Empty Sequence": [],
    }
    
    print("Performance Analysis: Random vs Classic QuickSort\n")
    
    for scenario, data in test_cases.items():
        print(f"Test Case: {scenario}")
        
        # Prepare separate copies for testing
        random_data = data.copy()
        classic_data = data.copy()
        
        # Measure random version
        start = time.time()
        random_quicksort(random_data, 0, len(random_data) - 1)
        random_duration = time.time() - start
        
        # Measure classic version
        start = time.time()
        classic_quicksort(classic_data, 0, len(classic_data) - 1)
        classic_duration = time.time() - start
        
        # Output timing results
        print(f"  Random Version: {random_duration:.6f} seconds")
        print(f"  Classic Version: {classic_duration:.6f} seconds")
        
        # Verify sorting accuracy
        assert random_data == sorted(data), "Random version failed!"
        assert classic_data == sorted(data), "Classic version failed!"
        print("  Status: Both implementations sorted correctly!\n")

if __name__ == "__main__":
    compare_quicksorts()