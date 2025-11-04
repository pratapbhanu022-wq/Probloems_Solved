def smallest_interval(face1, face2):
    distance = abs(face1 - face2)
    return min(distance, 12 - distance)
print(smallest_interval(3, 9))  # Output: 6