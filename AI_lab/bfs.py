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
queue=["A"]
order="A"
while queue:
    if queue[0] not in visited:
        current_node = queue.pop(0)

        visited.append(current_node)
        for neighbors in weightedgraph[current_node]:
            queue.append(neighbors)

    else:
        queue=queue[1:]
print(visited)

    