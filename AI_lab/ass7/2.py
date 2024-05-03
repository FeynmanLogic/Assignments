weightedgraph={
    "A":{"B":6,"F":3},
    "B":{"A":6,"C":3,"D":2},
    "C":{"B":3,"D":1,"E":5},
    "D":{"E":8,"B":2},
    "E":{"D":8,"C":5,"I":5,"J":5},
    "I":{"G":3,"E":5,"J":3,"H":2},
    "G":{"I":3,"F":1},
    "F":{"G":1,"A":3},
    "H":{"F":7,"I":2},
    "J":{"E":5,"I":3}
}
node="A"
for node, neighbors in weightedgraph.items():
    print("Distance of each is")
    for neighbor in neighbors:
        print(neighbors[neighbor])