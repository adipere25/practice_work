import math

# Area of a Cicle

radius = float(input("Enter the radius of the circle: "))
area_circle = math.pi * radius ** 2
print(f"The area of the circle with radius {radius} is: {area_circle:.2f}")

print("")  # just a blank line for better readability

# Area of a Triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area_triangle = 0.5 * base * height
print(f"The area of the triangle with base {base} and height {height} is: {area_triangle:.2f}") 

print("")

# Area of a Rectangle
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area_rectangle = length * breadth
print(f"The area of the rectangle with length {length} and breadth {breadth} is: {area_rectangle:.2f}")


#------------------------ Geometry Practice work------------------------------------

# Function of a Rectangle area ---------------

def rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle."""
    return width * height

# Ask user for input
width_input = float(input("Enter the width of the area: "))
height_input = float(input("enter the height of the area: "))

# Call the function
result_area = rectangle_area(width_input, height_input)
print(f"The area of the rectangle is: {result_area:.2f}")

# function of Circle arear ----------------------------------------
def circle_area(radius: float) -> float:
    """Calculate the area of a circle."""
    return math.pi * radius ** 2

# Ash user input
radius_input = float(input("Enter the radius of the circle: "))
# call the function
result_circle_area = circle_area(radius_input)
print(f"The area of the circle is: {result_circle_area:.2f}")

# Function of Triangle area  ----------------------------------------
def triangle_area(base: float, height: float) -> float:
    """Calculate the area of a triangle."""
    return 0.5 * base * height

# Ask user for input
base_input = float(input("Enter the base of the triangle: "))
height_input = float(input("Enter the height of the triangle: "))

# Call the function
result_triangle_area = triangle_area(base_input, height_input)
print(f"The area of the triangle is: {result_triangle_area:.2f}")

# function of square perimeter---------------------------------------

def square_perimeter(side: float) -> float:
    """Return the perimeter of a square."""
    return 4 * side

# Ask user for input
side_input = float(input("Enter the side of the square: "))

# Call the function
result_square_perimeter = square_perimeter(side_input)
print(f"The perimeter of the square is: {result_square_perimeter:.2f}")

# function of circle circumference and area -----------------------

def circle_details(radius: float) -> None:
    """Print thre circumference and aerea of a circle."""
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2
    print("\n--- Circle Details ---")
    print(f"Radius: {radius}")
    print(f"Circumference: {circumference}")
    print(f"Area: {area}")

# Ask user for input
radius_input = float(input("Enter the radius of the circle: "))
# call the function
circle_details(radius_input)

# function that takes the side lenght of a square and the radius of a circle ------------------


def geometry() -> None:
    """
    Compare a square and a circle by perimeter and area using user input.
    The function asks for square side and circle radius, then prints which
    has the larger perimeter/circumference and area.
    """
    print("\n--- Geometry Comparison ---")
    square_side = float(input("Enter the side length of the square: "))
    circle_radius = float(input("Enter the radius of the circle: "))

    # Calculate values
    square_p = square_perimeter(square_side)
    circle_c = 2 * math.pi * circle_radius
    square_a = square_side ** 2
    circle_a = circle_area(circle_radius)

    # Display results
    print("\n--- Results ---")
    print(f"Square Perimeter: {square_p}")
    print(f"Circle Circumference: {circle_c}")
    if square_p > circle_c:
        print("Square has the larger perimeter.")
    elif circle_c > square_p:
        print("Circle has the larger circumference.")
    else:
        print("They have equal perimeters.")

    print(f"\nSquare Area: {square_a}")
    print(f"Circle Area: {circle_a}")
    if square_a > circle_a:
        print("Square has the larger area.")
    elif circle_a > square_a:
        print("Circle has the larger area.")
    else:
        print("They have equal areas.")

# Call the geometry function
geometry()
# print output
print(f"The area of the rectangle with length {length} and breadth {breadth} is: {area_rectangle:.2f}")
