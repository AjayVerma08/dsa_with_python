from time import time

def power_set_recursive(nums):
    start = time()
    result = []
    def backtrack(start, current):
        result.append(current[:])  # copy current subset
        for i in range(start, len(nums)):
            current.append(nums[i])  # include nums[i]
            backtrack(i + 1, current)  # move forward
            current.pop()  # backtrack (remove last)

    backtrack(0, [])
    end = time()
    print(end - start)
    return result

def power_set_iterative(nums):
    start = time()
    result = [[]]
    for num in nums:
        new_subsets = []
        for subset in result:
            new_subsets.append(subset + [num])  # add num to each existing subset
        result.extend(new_subsets)
    end = time()
    print(end - start)
    return result

def power_set_bitmask(nums):
    start = time()
    n = len(nums)
    result = []
    for i in range(1 << n):  # 2^n combinations
        subset = []
        for j in range(n):
            if i & (1 << j):  # if jth bit of i is 1, include nums[j]
                subset.append(nums[j])
        result.append(subset)
    end = time()
    print(end - start)
    return result

print(power_set_recursive([1, 2, 3]))
print(power_set_iterative([1, 2, 3]))
print(power_set_bitmask([1, 2, 3]))
