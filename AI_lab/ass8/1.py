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

heuristics = {
    "A": 10,
    "B": 8,
    "C": 5,
    "D": 7,
    "E": 3,
    "F": 32,
    "G": 3,
    "H": 3,
    "I": 1,
    "J": 0
}
current_node = "A"
total_cost = 0
visited = []
answer = []
answer.append(current_node)

while current_node != "J":
    print("Current node is", current_node)
    if current_node not in visited:
        visited.append(current_node)
    neighbors = weightedgraph[current_node]
    min_cost = float('inf')
    next_node = None

    for neighbor in neighbors:
        if neighbor not in visited:
            f = heuristics[neighbor]
            if f < min_cost:
                min_cost = f
                next_node = neighbor

    if next_node:
        
        current_node = next_node
        answer.append(current_node)

print("Order is: ")
print(answer)