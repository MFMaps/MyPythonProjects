import math

apvsa = input("What shape do you want to get? ")

if apvsa == "circle":
    circlepa = input("Perimeter or Area: ")
    if circlepa == "area":
        radius = float(input('Enter in a number: '))
        circle_area = math.pi * radius * radius
        print("The area of the circle is:", circle_area)
    elif circlepa == "perimeter":
        radius = float(input('Enter in a number: '))
        circle_perimeter = 2 * math.pi * radius
        print("The perimeter of the circle is:", circle_perimeter)
    else:
        print("Try again.")
elif apvsa == "cube":
    cubevsaa = input("Volume, Surface Area, or Area: ")
    if cubevsaa == "surface area":
        cube_sides = float(input("Enter in the length of the sides: "))
        cube_surface_area = 6 * (cube_sides * cube_sides)
        print("The surface area of the cube is:", cube_surface_area)
    elif cubevsaa == "volume":
        cube_sides = float(input("Enter in the length of the sides: "))
        cube_volume = cube_sides ** 3
        print("The volume of the cube is:", cube_volume)
    elif cubevsaa == "area":
        cube_sides = float(input("Enter in the length of the sides: "))
        cube_area = 6 * (cube_sides ** 2)
        print("The area of the cube is:", cube_area)
    else:
        print("Try again.")
elif apvsa == "rectangle":
    rectanglepa = input("Perimeter or Area: ")
    if rectanglepa == "area":
        rectangle_width = float(input("Enter in the width: "))
        rectangle_height = float(input("Enter in the height: "))
        rectangle_area = rectangle_width * rectangle_height
        print("The area of the rectangle is:", rectangle_area)
    elif rectanglepa == "perimeter":
        rectangle_width = float(input("Enter in the width: "))
        rectangle_height = float(input("Enter in the height: "))
        rectangle_perimeter = rectangle_height * 2 + rectangle_width * 2
        print("The perimeter of the rectangle is:", rectangle_perimeter)
    else:
        print("Try again.")
elif apvsa == "sphere":
    spherevsa = input("Volume or Surface Area: ")
    if spherevsa == "volume":
        sphere_radius = float(input("Enter in a radius: "))
        sphere_volume = (4/3 * (math.pi * (sphere_radius ** 3)))
        print("The volume of the sphere is:", sphere_volume)
    elif spherevsa == "surface area":
        sphere_radius = float(input("Enter in a radius: "))
        sphere_surface_area = (4 * (math.pi * (sphere_radius ** 2)))
        print("The surface area of the sphere is:", sphere_surface_area)
    else:
        print("Try again.")
elif apvsa == "square":
    squarepa = input("Perimeter or Area: ")
    if squarepa == "perimeter":
        square_sides = float(input("Enter in the length of the sides: "))
        square_perimeter = square_sides + square_sides + square_sides + square_sides
        print("The perimeter of the square is", square_perimeter)
    elif squarepa == "area":
        square_sides = float(input("Enter in the length of the sides: "))
        square_area = square_sides ** 2
        print("The area of the square is", square_area)
    else:
        print("Try again.")
elif apvsa == "triangle":
    trianglea = input("Area? (y/n) ")
    if trianglea == "y":
        triangle_base = float(input("Enter in the base: "))
        triangle_height = float(input("Enter in the height: "))
        triangle_area = 0.5 * triangle_base * triangle_height
        print("The area of the triangle is:", triangle_area)
    elif trianglea == "n":
        print("Oh sad.")
    else:
        print("Try again.")
else:
    print("Either not a shape or hasn't been added yet.")