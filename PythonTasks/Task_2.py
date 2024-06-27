#Task 2 : Write a Python program which accepts the radius of a circle from the user and compute the area

import math
radius = float(input ("Please input the radius in m to calculate the area of the circle \n"))
area = round (radius**2 *math.pi,2)
print(f"The Area = {area} m2")
