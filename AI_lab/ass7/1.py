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

distance = 0
func = 2 ** 100

heuristic = 0
current_node = "A"
total_cost = 0
visited = []
answer = []

for node, neighbors in weightedgraph.items():
    print("Current node is", node)
    if node == "J":
        print("The order of traversal is: ", answer)
        print("Total cost obtained is: ", total_cost)
    for neighbor in neighbors:
        if neighbor not in visited:
            print("Currently traversing this neighbor:", neighbor)
            visited.append(neighbor)
            distance = neighbors[neighbor]
            heuristic = heuristics[neighbor]
            f = distance + heuristic
            print("F for the given neighbor is:", f)
            if f < func:
                func = f
                total_cost = total_cost + func
                answer.append(node)  # Add the current node to the answer list
                print("node will change to:", neighbor)
    if node == "J":
        print("Total cost obtained is: ", total_cost)
