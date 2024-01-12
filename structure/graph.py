class Graphs:
    
    def __init__(self):
        self.nodesCount = 0
        self.adjacentNodes = {}
    
    def __len__(self):
        return len(self.adjacentNodes)
    
    def addNode(self, node):
        self.nodesCount+=1
        self.adjacentNodes[node] = []

    def addEdge(self, node1, node2):
        self.adjacentNodes[node1].append(node2)
        self.adjacentNodes[node2].append(node1)
    
    def showConnections(self):
        return self.adjacentNodes.items()