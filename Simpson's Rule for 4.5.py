def simpsons_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Number of subintervals n must be even.")

    h = (b - a) / n
    x = a
    integral = f(a) + f(b)

    for i in range(1, n):
        x += h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)

    integral *= h / 3
    return integral

# Example usage:
import math

# Define the function to integrate
def f(B):
    xPrime = (3.29/120)*math.pi*math.cos(2*B) + (2.51/240)*math.pi*math.sin(B) - (math.pi/480)*math.cos(B)
    yPrime = (23.45/180)*math.pi*math.cos(B)
    arcLengthCombine = math.sqrt((xPrime**2) + (yPrime**2))
    return arcLengthCombine

# Set integration limits and number of subintervals
a = 0
b = 2*math.pi
n = int(input("n= "))

# Calculate the integral
result = simpsons_rule(f, a, b, n)
print(f"Perimeter = {result}")
