weightedgraph = {
    "A": {"B": 6, "F": 3},
    "B": {"A": 6, "C": 3, "D": 2},
    "C": {"B": 3, "D": 1, "E": 5},
    "D": {"E": 8, "B": 2},
    "E": {"D": 8, "C": 5, "I": 5, "J": 5},
    "I": {"G": 3, "E": 5, "J": 3, "H": 2},
    "G": {"I": 3, "F": 1},
    "F": {"G": 1, "A": 3},
    "H": {"F": 7, "I": 2},
    "J": {"E": 5, "I": 3}
}

heuristics = {
    "A": 10,
    "B": 8,
    "C": 5,
    "D": 7,
    "E": 3,
    "F": 6,
    "G": 5,
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

    for neighbor, cost in neighbors.items():
        if neighbor not in visited:
            f = total_cost + cost + heuristics[neighbor]
            if f < min_cost:
                min_cost = f
                next_node = neighbor

    if next_node:
        total_cost += weightedgraph[current_node][next_node]
        current_node = next_node
        answer.append(current_node)

print("The order of traversal is:", answer)
print("Total cost obtained is:", total_cost)
