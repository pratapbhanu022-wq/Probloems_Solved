import math

AB = int(input())
BC = int(input())

angle_rad = math.atan2(AB,BC) # atan2(y, x) =atan(y / x)
angle_deg = math.degrees(angle_rad)
result = round(angle_deg)

print(f"{result}{chr(176)}") # chr{176}= sign of degree 