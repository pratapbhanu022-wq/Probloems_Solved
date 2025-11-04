def productExceptSelf(nums):
    n = len(nums)                 # n = 5 (since nums = [10, 3, 5, 6, 2])
    res = [1] * n                 # res = [1, 1, 1, 1, 1]
    
    prefix = 1                    # prefix starts as 1

    # ---------- 1st Loop (Left to Right) ----------
    # Store product of elements to the left of each index
    for i in range(n):
        res[i] = prefix           # Step 1: place the product of all elements before index i
        prefix *= nums[i]         # Step 2: include nums[i] for the next iteration
        
        # Print state after each iteration
        print(f"i={i}, res={res}, prefix={prefix}")

    # After loop:
    # res = [1, 10, 30, 150, 900]
    # prefix = 1800 (product of all elements)

    suffix = 1                    # suffix starts as 1

    # ---------- 2nd Loop (Right to Left) ----------
    # Multiply with product of elements to the right
    for i in range(n-1, -1, -1):
        res[i] *= suffix          # Step 1: multiply left product with right product
        suffix *= nums[i]         # Step 2: include nums[i] for next (left) iteration

        # Print state after each iteration
        print(f"i={i}, res={res}, suffix={suffix}")

    return res
print(productExceptSelf([10,3,5,6,2]))