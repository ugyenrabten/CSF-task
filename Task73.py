import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)
def triangle_info(a,b):
    hypotenuse = calculate_hypotenuse(a,b)
    print(f"the length of hypotenuse is: {hypotenuse}")
triangle_info(4,5)