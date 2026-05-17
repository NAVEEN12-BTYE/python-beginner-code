limit = int(input("Enter limit: "))
a, b = 0, 1
print("Fibonacci Series:")

while a <= limit:
    print(a, end=" ")
    a, b = b, a + b

