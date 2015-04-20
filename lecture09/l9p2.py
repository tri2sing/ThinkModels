'''
Created on Apr 17, 2015

@author: Sameer Adhikari
'''

from lecture09.graph import Node
from lecture09.graph import Edge
from lecture09.graph import Graph

def adjacentNames(inStr):
    '''
    '''
    for i in range(len(inStr) - 1):
        outStr = inStr[:i] + inStr[i+1] + inStr[i] + inStr[i+2:]
        yield outStr 


'''
inStr = 'ABC'
print inStr
for permStr in adjacentNames(inStr):
    print permStr
'''
            
nodes = []
nameToNodeMap = {}
node = Node("ABC")
nodes.append(node) # nodes[0]
nameToNodeMap["ABC"] = node

node = Node("ACB")
nodes.append(node) # nodes[1]
nameToNodeMap["ACB"] = node

node = Node("BAC")
nodes.append(node) # nodes[2]
nameToNodeMap["BAC"] = node

node = Node("BCA")
nodes.append(node) # nodes[3]
nameToNodeMap["BCA"] = node

node = Node("CAB")
nodes.append(node) # nodes[4]
nameToNodeMap["CAB"] = node

node = Node("CBA")
nodes.append(node) # nodes[5]
nameToNodeMap["CBA"] = node

names = [node.getName() for node in nodes]
print names

print nameToNodeMap

g = Graph()

for n in nodes:
    g.addNode(n)

for n in nodes:
    name = n.getName()
    for adjacent in adjacentNames(name):
        print 'Node = ', name, 'Adjacent = ', adjacent
        if adjacent in names:
            g.addEdge(Edge(n, nameToNodeMap[str(adjacent)]))
    print g
    
