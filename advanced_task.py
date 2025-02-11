import cmath  # cmath handles both real and complex square roots

# Input values
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Calculate the roots using cmath to handle both real and complex roots
x1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
x2 = (-b + cmath.sqrt(discriminant)) / (2 * a)

# Output the results, format them for complex results too
print(f"The value of x1 is {x1:.2f} and x2 is {x2:.2f}")