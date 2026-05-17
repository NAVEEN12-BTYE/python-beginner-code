import math

# 1. Add two numbers
def add_two_numbers(a, b):
    return a + b


# 2. Area of a circle
def area_of_circle(r):
    return math.pi * r * r


# 3. Add all numbers (arbitrary arguments)
def add_all_nums(*nums):
    total = 0
    for n in nums:
        if not isinstance(n, (int, float)):
            return "Error: All items must be numbers."
        total += n
    return total


# 4. Convert Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


# 5. Check season by month
def check_season(month):
    month = month.lower()
    
    if month in ["september", "october", "november"]:
        return "Autumn"
    elif month in ["december", "january", "february"]:
        return "Winter"
    elif month in ["march", "april", "may"]:
        return "Spring"
    elif month in ["june", "july", "august"]:
        return "Summer"
    else:
        return "Invalid month"


# 6. Calculate slope of linear line
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        return "Slope is undefined"
    return (y2 - y1) / (x2 - x1)


# 7. Solve quadratic equation ax² + bx + c = 0
def solve_quadratic_eqn(a, b, c):
    d = b*b - 4*a*c   # Discriminant
    
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return (x1, x2)
    elif d == 0:
        x = -b / (2*a)
        return (x,)
    else:
        return "No real solutions"


# 8. Print each element of a list
def print_list(lst):
    for item in lst:
        print(item)


# 9. Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 10. Factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
