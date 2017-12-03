def calculatearea(radius = 0):
    return (22/7)*radius*radius

radius = float(input("Enter the radius of a circle "))

print("Area of circle with radius {0} is {1:.3f} ".format(radius,calculatearea(radius)))