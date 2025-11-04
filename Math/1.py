# You are given a complex z. Your task is to convert it to polar coordinates.
import cmath
z = complex(input())
r,theta=cmath.polar(z)
print(r,theta)