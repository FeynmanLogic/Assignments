def skyline(buildings):
    n = len(buildings)
    if n == 1:
        x1, x2, h = buildings[0]
        return [(x1, h), (x2, 0)]

    mid = n // 2
    left = skyline(buildings[:mid])
    right = skyline(buildings[mid:])
    return merge_skylines(left, right)

def merge_skylines(left, right):
    i, j = 0, 0
    h1, h2 = 0, 0
    merged = []

    while i < len(left) and j < len(right):
        x1, h1 = left[i]
        x2, h2 = right[j]

        if x1 < x2:
            h = max(h1, h2)
            merged.append((x1, h))
            i += 1
        elif x1 > x2:
            h = max(h1, h2)
            merged.append((x2, h))
            j += 1
        else:
            h = max(h1, h2)
            merged.append((x1, h))
            i += 1
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


buildings = [(33, 41, 5), (4, 9, 21), (30, 36, 9), (14, 18, 11), 
             (2, 12, 14), (34, 43, 19), (23, 25, 8), (14, 21, 16), 
             (32, 37, 12), (7, 16, 7), (24, 27, 10)]
result = skyline(buildings)
print(result)
