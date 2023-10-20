def calculate_area(length, width):
    area = length * width
def calculate_perimeter(length, width):
    return 2 * (length + width)
def rectangle_info(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    print(f"The area of the rectangle is:", {area})
    print(f"The perimeter of the rectangle is:",{perimeter})
rectangle_info(4,5)