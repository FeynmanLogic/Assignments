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

startnode="A"
currentnode=startnode
visited=[]
queue=[]
queue.append(startnode)
visited.append(currentnode)
i=0
while queue:
    neighbors=weightedgraph[currentnode]
    print(neighbors)
    for neighbor in neighbors:
        if neighbor not in visited:
            visited.append(neighbor)
            print(visited)
            queue.append(neighbor)
        
    currentnode=queue[0]
    if currentnode in visited:
        queue=queue[1:]
        currentnode=queue[0]
    if len(visited)==10:
        break
print("Order of traversal is:",visited)