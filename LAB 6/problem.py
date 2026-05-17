# Problem 1: List Manipulation

nums = list(map(int, input().split()))

# 1. Remove duplicates
nums = list(set(nums))
print(nums)

# 2. Sort in ascending order
nums.sort()
print(nums)

# 3. Reverse the sorted list
rev_list = nums[::-1]
print(rev_list)

# 4. Find second largest (index 1 in reversed list)
second_largest = rev_list[1]
print(second_largest)

# 5. Sum of elements
total_sum = sum(nums)
print(total_sum)
