from math_operations import calculator
from math_operations import geometry

# Calculator tests
print("5 + 3 =", calculator.add(5, 3))
print("10 - 4 =", calculator.subtract(10, 4))
print("6 × 7 =", calculator.multiply(6, 7))
print("20 ÷ 5 =", calculator.divide(20, 5))
print("5 ÷ 0 =", calculator.divide(5, 0))

# Geometry tests
print("\nCircle area (radius=5):", geometry.circle_area(5))
print("Rectangle area (6×8):", geometry.rectangle_area(6, 8))
print("Triangle area (base=4, height=3):", geometry.triangle_area(4, 3))