'''
def cargo_fit(box_dimensions, cargo_volume):
    s=1
    for i in box_dimensions:
        s*=i
    if cargo_volume<=s:
        return True
    else:
        return False
print(cargo_fit([1,2,3],6))
'''
def cargo_fit(box_dimensions, cargo_volume):
    box_volume = box_dimensions[0] * box_dimensions[1] * box_dimensions[2]
    return cargo_volume <= box_volume
print(cargo_fit([1,2,3],6))

