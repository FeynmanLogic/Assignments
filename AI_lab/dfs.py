weightedgraph = {
    "A": ["B", "F"],
    "B": ["A", "C", "D"],
    "C": ["B", "D", "E"],
    "D": ["E", "B"],
    "E": ["D", "C", "I", "J"],
    "I": ["G", "E", "J", "H"],
    "G": ["I", "F"],
    "F": ["G", "A"],
    "H": ["F", "I"],
    "J": ["E", "I"]
}
current_node="A"
visited=[]
stack=["A"]
order=[]
while stack:
    if stack[-1] not in visited:
        current_node=stack[-1]

        visited.append(current_node)
        order.append(current_node)
        for neighbor in weightedgraph[current_node]:
            stack.append(neighbor)
    else:
        stack.pop()

print(visited)

    
