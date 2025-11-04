def longest_fibonacci_subset(arr):
    n = len(arr)
    if n < 3:
        return []
    
    arr.sort()
    s = set(arr)
    longest = []
    
    for i in range(n):
        for j in range(i + 1, n):
            subset = [arr[i], arr[j]]
            a, b = arr[i], arr[j]
            
            # Keep extending the Fibonacci sequence
            while a + b in s:
                subset.append(a + b)
                a, b = b, a + b
            
            # Update longest if current subset is longer
            if len(subset) > len(longest):
                longest = subset
    
    # Return empty list if no Fibonacci subset found
    return longest if len(longest) >= 3 else []
print(longest_fibonacci_subset([1,2,3,4,5,6]))

# method 2
def fibonacci_subset(numbers):
    max_num = max(numbers)
    fib = [0, 1]
    while fib[-1] + fib[-2] <= max_num:
        fib.append(fib[-1] + fib[-2])
    return [n for n in numbers if n in fib]
print(fibonacci_subset([1,2,3,4,5,6]))


