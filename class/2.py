import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Points(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Points(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def absolute(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

if __name__ == '__main__':
    points = [Points(*map(float, input().split())) for _ in range(4)]
    a, b, c, d = points

    # Vectors AB and BC
    ab = b - a
    bc = c - b
    # Vectors BC and CD
    bc_ = c - b
    cd = d - c

    # Normal vectors to the planes
    normal_abc = ab.cross(bc)
    normal_bcd = bc_.cross(cd)

    # Calculating the angle between the two normal vectors
    cosine_angle = normal_abc.dot(normal_bcd) / (normal_abc.absolute() * normal_bcd.absolute())
    angle = math.acos(cosine_angle)

    # Output the angle in degrees
    print(f"{math.degrees(angle):.2f}")
