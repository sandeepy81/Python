def calculate_area(dimension1,dimension2,shape="triangle"):
    '''
    :param dimension1: In case of triangle it is "base". For rectangle it is "length".
    :param dimension2: In case of triangle it is "height". For rectangle it is "width".
    :param shape: Either "triangle" or "rectangle"
    :return: Area of a shape
    '''
    if shape=="triangle":
        area=1/2*(dimension1*dimension2) # Triangle area is : 1/2(Base*Height)
    elif shape=="rectangle":
        area=dimension1*dimension2 # Rectangle area is: Length*Width
    else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area=None # If user didn't supply "triangle" or "rectangle" as shape then return None
    return area


# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# ```
# area = (1/2)*base*height
# ```
#
# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# ```
# rectangle area=length*width
# ```
# If no shape is supplied then it should take triangle as a default shape

# Calculate area of triangle whose base is 10 and height is 5
base=10
height=5
triangle_area=calculate_area(base,height,"triangle")
print("Area of triangle is:",triangle_area)

# Calculate area of a rectangle whose length is 20 and width is 30
length=20
width=30
rectangle_area=calculate_area(length,width,"rectangle")
print("Area of rectangle is:",rectangle_area)

# Calculate area of a triangle without supplying shape argument in a function call
triangle_area=calculate_area(base,height) # Here third argument is missing
print("Area of triangle with no shape supplied: ",triangle_area)

