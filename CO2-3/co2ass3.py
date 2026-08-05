import math
def closest_pair(points):
    min_dist = float('inf')
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            dist = math.sqrt(
                (x1 - x2) ** 2 + (y1 - y2) ** 2
            )
            if dist < min_dist:
                min_dist = dist
    return min_dist
points = [(1, 2), (2, 3), (10, 12)]
result = closest_pair(points)
print("Minimum distance:", result)
