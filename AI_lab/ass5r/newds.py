graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

i = 0
visited = []
stack = []

for node, neighbors in graph.items():
    i = 0
    print("We are at this node:", node)
    print("neighbors of this", neighbors)
    if node not in visited:
        visited.append(node)
        stack.append(node)
        print("Visited array till now", visited)
    for neighbor in neighbors:
        if neighbor not in visited:
            visited.append(neighbor)
            stack.append(neighbor)
            print("Stack ab tak", stack)
            break
        i += 1
    if i == len(neighbors):
        stack.pop()
        if stack:
            node = stack[-1]
    i = 0
    print("visited array after visiting this node is", visited)

print("Final stack", stack)
print("Final visited", visited)
