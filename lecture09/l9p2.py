'''
Created on Apr 17, 2015

@author: Sameer Adhikari
'''

from lecture09.graph import Node
from lecture09.graph import Edge
from lecture09.graph import Graph



# Preconditions for the assignment on node and graph construction            
nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]

# Preconditions for the assignment on node and graph construction            
g = Graph()
for n in nodes:
    g.addNode(n)

# Function to generate adjacent node names for a given node
def adjacentNames(inStr):
    '''
    '''
    for i in range(len(inStr) - 1):
        outStr = inStr[:i] + inStr[i + 1] + inStr[i] + inStr[i + 2:]
        yield outStr 

# List to track by name (not reference) whether a node automatically 
# generated while adding edges is part of the original node list. 
nodeNames = [node.getName() for node in nodes]
# Map between node names and the reference to the node to use
# later in auto-creation of edges for the graph
nodeTracker = {node.getName(): node for node in nodes}

# Map to track whether a node is already in the graph.
# This is to prevent adding duplicates during auto generation.
edgeTracker = {}

# print nodeNames
# print nodeTracker

# Auto generate and add edges based on nodes
for n in nodes:
    name = n.getName()
    for adjacent in adjacentNames(name):
        # print 'Node = ', name, 'Adjacent = ', adjacent
        if adjacent in nodeNames:
            if (str(name), str(adjacent)) not in edgeTracker:
                g.addEdge(Edge(n, nodeTracker[str(adjacent)]))
                # We add both edges to our tracker as the graph add
                # inserts edge and its reverse to the graph
                edgeTracker[str(name), str(adjacent)] = True
                edgeTracker[str(adjacent), str(name)] = True

print g
    
