# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        # Sameer: because we are using strings and
        # not node objects as parameters in ps5
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

# Problem 1 from set 05
class WeightedEdge(Edge):
    '''
    Edge that has two weights associated with it.
    '''
    def __init__(self, src, dest, totalDistance, outdoorDistance):
        self.totalDistance = totalDistance
        self.outdoorDistance = outdoorDistance
        super(WeightedEdge, self).__init__(src, dest)
    def getTotalDistance(self):
        return self.totalDistance
    def getOutdoorDistance(self):
        return self.outdoorDistance
    def __str__(self):
        return '{0} ({1}, {2})'.format(super(WeightedEdge, self).__str__(), str(self.totalDistance), str(self.outdoorDistance))
        
    
class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

# Problem 1 from set 05
class WeightedDigraph(Digraph):
    '''
    A diagraph which handles weighted edges
    '''
    def __init__(self):
        super(WeightedDigraph, self).__init__()
        self.weights = {}
    def addEdge(self, edge):
        '''
        Adds two weights for each edge
        '''
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest, (float(edge.getTotalDistance()), float(edge.getOutdoorDistance()))])
        self.weights[src, dest] = float(edge.getTotalDistance()), float(edge.getOutdoorDistance())
        
    def childrenOf(self, node):
        '''
        Returns only the children and not the weights
        '''
        return [child[0] for child in self.edges[node]]

    def getEdgeWeights(self, src, dest):
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        if not (src, dest) in self.weights:
            raise ValueError('(src, dest) weights not stored')
        return self.weights[src, dest]
        
    def getPathWeights(self, path):
        '''
        Finds the sum of the total and outside weights of the edges along the path
        
        Parameters:
            path: the list of nodes from source to destination
        
        Assumes:
            path contains nodes in the correct sequence of edges
    
        Returns:
            The sum of the total and outside weights
        '''
        pathTotal = 0.0
        pathOutside = 0.0
        for i in range(len(path) - 1):
            # We call the function rather than access the dict for weights
            # because we can to take advantage of the error checking
            edgeTotal, edgeOutSide = self.getEdgeWeights(path[i], path[i + 1])
            pathTotal = pathTotal + edgeTotal
            pathOutside = pathOutside + edgeOutSide
        return pathTotal, pathOutside
        
    def DFSAllPaths(self, start, end, path=[]):
        # assumes graph is a Digraph
        # assumes start and end are nodes in graph
        path = path + [start]
        if start == end:
            return [path]  # recursion stop when you reach destination
        allPaths = []
        for node in self.childrenOf(start):
            if node not in path:  # avoid cycles
                newPaths = self.DFSAllPaths(node, end, path)
                # if child returns paths, return them to the caller
                for newPath in newPaths:
                    allPaths.append(newPath)
        return allPaths  # if no path exists, this is an empty list

    def __str__(self):
        '''
        Returns the weights along with the the soure and destination pairs
        '''
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2} {3}\n'.format(res, k, d[0], d[1])
        return res[:-1]
        

def test():
    na = Node('a')
    nb = Node('b')
    nc = Node('c')
    e1 = WeightedEdge(na, nb, 15, 10)
    print e1
    print e1.getTotalDistance()
    print e1.getOutdoorDistance()
    e2 = WeightedEdge(na, nc, 14, 6)
    e3 = WeightedEdge(nb, nc, 3, 1)
    print e2
    print e3
    
    g = WeightedDigraph()
    g.addNode(na)
    g.addNode(nb)
    g.addNode(nc)
    g.addEdge(e1)
    g.addEdge(e2)
    g.addEdge(e3)
    print g
    print g.childrenOf(na)    
    print g.weights
    print 'na, nb = ', g.getEdgeWeights(na, nb)
    print g.DFSAllPaths(na, nc)
    
if __name__ == '__main__':   
    test() 
    
    
    
