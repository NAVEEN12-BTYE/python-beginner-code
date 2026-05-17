n = int(input("Enter number of terms: "))
term = 0
total = 0

for i in range(1, n + 1):
    term = term * 10 + 2
    total += term

print("Sum of series =", total)

