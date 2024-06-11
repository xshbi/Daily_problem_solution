from math import pi

radius = float(input("Enter the radius: "))

if radius > 0:
    area = pi * (radius ** 2)
    print("Area of the circle:", area)

    circumference = 2 * pi * radius
    print("Circumference of the circle:", circumference)
else:
    print("Invalid input. Please enter a positive radius.")
