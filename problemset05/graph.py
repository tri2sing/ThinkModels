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
            The sum of the total and sum of outside weights as a tuple.
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

    def DFSShortestDirected(self, start, end, maxTotalDist, maxDistOutdoors, path=[], shortest=None):
        # assumes graph is a Digraph
        # assumes start and end are nodes in graph
        path = path + [start]
        # If the path has one node, the weights we get back are (0.0, 0.0)
        pathTotal, pathOutside = self.getPathWeights(path)
        # print 'maxTotalDist = ', maxTotalDist, ', maxDistOutdoors = ', maxDistOutdoors, ', pathTotal = ', pathTotal, ', = pathOutside', pathOutside
        if pathTotal > maxTotalDist:
            return None
        if pathOutside > maxDistOutdoors:
            return None
        # It is important to consider the path valid if it falls below the thresholds above
        if start == end and (shortest == None or pathTotal < self.getPathWeights(shortest)[0]):
            #print 'Found path = ', path, ' weights = ', self.getPathWeights(path)
            return path
        for node in self.childrenOf(start):
            if node not in path:  # avoid cycles
                if shortest == None or pathTotal < self.getPathWeights(shortest)[0]:
                    newPath = self.DFSShortestDirected(node, end, maxTotalDist, maxDistOutdoors, path, shortest)
                    if newPath != None:
                        shortest = newPath
        return shortest

    def __str__(self):
        '''
        Returns the weights along with the the soure and destination pairs
        '''
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2} {3}\n'.format(res, k, d[0], d[1])
        return res[:-1]
        

def test0():
    na = Node('a')
    nb = Node('b')
    nc = Node('c')
    e1 = WeightedEdge(na, nb, 15, 10)
    print e1
    print e1.getTotalDistance()
    print e1.getOutdoorDistance()
    e2 = WeightedEdge(na, nc, 14, 30)
    e3 = WeightedEdge(nb, nc, 3, 5)
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
    print 'All paths = ', g.DFSAllPaths(na, nc)
    print
    print g.DFSShortestDirected(na, nc, 1000.0, 1000.0)
    print
    print g.DFSShortestDirected(na, nc, 1000.0, 20.0)
    print

def test1():
    print 'test1'
    n1 = Node('1')
    n2 = Node('2')
    n3 = Node('3')
    n4 = Node('4')
    n5 = Node('5')
    
    e1 = WeightedEdge(n1, n2, 5, 2)
    e2 = WeightedEdge(n3, n5, 6, 3)
    e3 = WeightedEdge(n2, n3, 20, 10)
    e4 = WeightedEdge(n2, n4, 10, 5)
    e5 = WeightedEdge(n4, n3, 2, 1)
    e6 = WeightedEdge(n4, n5, 20, 10)
    
    g = WeightedDigraph()
    g.addNode(n1)
    g.addNode(n2)
    g.addNode(n3)
    g.addNode(n4)
    g.addNode(n5)
    g.addEdge(e1)
    g.addEdge(e2)
    g.addEdge(e3)
    g.addEdge(e4)
    g.addEdge(e5)
    g.addEdge(e6)

    print "Expected: ['1', '2', '4', '3']"
    print "My output: ", g.DFSShortestDirected(n1, n3, 100, 100)
    print
    print "Expected: ['1', '2', '4', '3', '5']"
    print "My output: ", g.DFSShortestDirected(n1, n5, 100, 100)
    print
    print "Expected: ['1', '2', '4', '3']"
    print "My output: ", g.DFSShortestDirected(n1, n3, 17, 8)
    print
    print "Expected: ['1', '2', '4', '3', '5']"
    print "My output: ", g.DFSShortestDirected(n1, n5, 23, 11)
    print
    print "Expected: ['4', '3', '5']"
    print "My output: ", g.DFSShortestDirected(n4, n5, 21, 11)
    print
    
def test2():
    print 'test2'
    n1 = Node('1')
    n2 = Node('2')
    n3 = Node('3')
    n4 = Node('4')
    n5 = Node('5')
    
    e1 = WeightedEdge(n1, n2, 5, 2)
    e2 = WeightedEdge(n3, n5, 5, 1)
    e3 = WeightedEdge(n2, n3, 20, 10)
    e4 = WeightedEdge(n2, n4, 10, 5)
    e5 = WeightedEdge(n4, n3, 5, 1)
    e6 = WeightedEdge(n4, n5, 20, 1)
    
    g = WeightedDigraph()
    g.addNode(n1)
    g.addNode(n2)
    g.addNode(n3)
    g.addNode(n4)
    g.addNode(n5)
    g.addEdge(e1)
    g.addEdge(e2)
    g.addEdge(e3)
    g.addEdge(e4)
    g.addEdge(e5)
    g.addEdge(e6)

    result = g.DFSShortestDirected(n1, n5, 100, 100)
    print "Expected: ['1', '2', '4', '5']"
    print "My output: ", result
    print
    print "Expected: ['1', '2', '4', '3']"
    print "My output: ", g.DFSShortestDirected(n1, n3, 100, 100)
    print
    print "Expected: ['1', '2', '4', '5']"
    print "My output: ", g.DFSShortestDirected(n1, n5, 35, 8)
    print
    print "Expected: ['4', '5']"
    print "My output: ", g.DFSShortestDirected(n4, n5, 21, 1)
    print
    print "Expected: ['1', '2', '4', '3', '5']"
    print "My output: ", g.DFSShortestDirected(n1, n5, 35, 9)
    print
    print "Expected: ['4', '3', '5']"
    print "My output: ", g.DFSShortestDirected(n4, n5, 21, 11)
    print
    
if __name__ == '__main__':   
    test1()
    test2() 
    
    
    
