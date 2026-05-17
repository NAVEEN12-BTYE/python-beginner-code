# Problem 2: Tuple Operations

t = tuple(map(int, input().split()))

# 1. Minimum and Maximum
mn = min(t)
mx = max(t)
print(f"Minimum: {mn}, Maximum: {mx}")

# 2. Convert tuple → list and add new element
lst = list(t)
new_element = int(input())   # user input for element to add
lst.append(new_element)

# 3. Convert list → tuple
t_final = tuple(lst)
print(t_final)
