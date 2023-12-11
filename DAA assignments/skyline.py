import heapq

buildings = [(1, 3, 3), (2, 4, 4), (5, 7, 2), (6, 8, 3)]

# sort buildings based on their left coordinate
buildings.sort(key=lambda x: x[0])

# initialize priority queue and maximum height
queue = []
max_height = 0
output = []

# iterate through buildings
for building in buildings:
    # remove buildings that end before the current building starts
    while queue and queue[0][1] < building[0]:
        _, end, height = heapq.heappop(queue)
        if height == max_height:
            # if the removed building had the maximum height, update the maximum height
            max_height = queue[0][2] if queue else 0
    
    # add the current building to the queue
    heapq.heappush(queue, (-building[2], building[1], building[2]))
    if building[2] > max_height:
        # if the current building is taller than the maximum height, add a point to the output skyline
        max_height = building[2]
        output.append((building[0], max_height))

# sort output points by x-coordinate
output.sort()

# print output points
for point in output:
    print(point, end=' ')
print()
