# Problem 3: Basic List Operations

nums = list(map(int, input().split()))
target = int(input())  # number to count

largest = max(nums)
smallest = min(nums)
count = nums.count(target)

print(f"Largest: {largest}, Smallest: {smallest}")
print(f"Count of {target}: {count}")
