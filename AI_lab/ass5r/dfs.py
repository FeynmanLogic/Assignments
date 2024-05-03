#basically saare nodes ka ek stack hoga, wha se node by node explore karna, jab sare nodes explored honge to pop karna
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
    print("------Running node is:   ", node)
    i = 0
    print("We are at this node:", node)
    print("neighbors of this", neighbors)
    
    if node not in visited:
        visited.append(node)
        stack.append(node)

    while stack:
        current_node = stack[-1]
        current_neighbors = graph[current_node]

        for neighbor in current_neighbors:
            if neighbor not in visited:
                visited.append(neighbor)
                stack.append(neighbor)

                if current_node == 'D' and neighbor == 'B':
                    print("Checking if for D,B it reaching here or not")

                break

        if neighbor == current_neighbors[-1]:
            stack.pop()

        print("node we will go to next is,", stack[-1] if stack else None)
        print("visited array after visiting this node is", visited)
        print("stack after visiting this node", stack)

print("Final stack", stack)
print("Final visited", visited)
