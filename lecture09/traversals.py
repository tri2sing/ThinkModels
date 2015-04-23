'''
Created on Apr 21, 2015

@author: Sameer Adhikari
'''

from lecture09.graph import *

def DFS(graph, start, end, path = []):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    #print 'Current dfs path:', printPath(path)
    if start == end:
        return path # recursion stop when you reach destination
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = DFS(graph,node,end,path)
            if newPath != None:
                return newPath # if child returned a path, return it to caller
    return None # if no path exists

def DFSAllPaths(graph, start, end, path = []):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    #print 'Current dfs path:', printPath(path)
    if start == end:
        return [path] # recursion stop when you reach destination
    allPaths = []
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPaths = DFSAllPaths(graph,node,end,path)
            # if child returns paths, return them to the caller
            for newPath in newPaths:
                allPaths.append(newPath)
    return allPaths # if no path exists, this is an empty list

def DFSShortest(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print 'Current shortest dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                newPath = DFSShortest(graph,node,end,path,shortest)
                if newPath != None:
                    shortest = newPath
    return shortest

def BFS(graph, start, end, q = []):
    initPath = [start]
    q.append(initPath)
    while len(q) != 0:
        tmpPath = q.pop(0)
        lastNode = tmpPath[len(tmpPath) - 1]
        print 'Current dequeued path:', printPath(tmpPath)
        if lastNode == end:
            return tmpPath
        for linkNode in graph.childrenOf(lastNode):
            if linkNode not in tmpPath:
                newPath = tmpPath + [linkNode]
                q.append(newPath)
    return None

def test():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    pathDFS = DFS(g, nodes[0], nodes[5])
    print 'Path found by DFS:', printPath(pathDFS)
    print
    allPaths = DFSAllPaths(g, nodes[0], nodes[5])
    for path in allPaths:
        print 'Path found by DFS All Paths:', printPath(path)
#     shortest = DFSShortest(g, nodes[0], nodes[5])
#     print 'Path found by DFS shortest:', printPath(shortest)
#     print
#     pathBFS = BFS(g, nodes[0], nodes[5])
#     print 'Path found by BFS:', printPath(pathBFS)

    
if __name__ == '__main__':   
    test() 


    
    