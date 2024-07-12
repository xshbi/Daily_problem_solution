import math

def area_to_volume(area):
    radius = math.sqrt(area / (4 * math.pi))
    volume = (4/3) * math.pi * radius**3
    return volume

# Example usage
area = 113.09733552923255
volume = area_to_volume(area)
print(f"Volume of the sphere with surface area {area} is: {volume}")
