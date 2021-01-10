#from operator import itemgetter
#
#class Graph():
#    def __init__(self, n):
#        self.n = n
#        self.connections = []
#
#    def connect(self, x, y):
#        edge = [x, y] if x < y else [y, x]
#        if edge not in self.connections:
#            self.connections.append(edge)
#    
#    def find_all_distances(self, s):
#        def get_to_check(c_node):
#            connectors = lambda x : x[0] == c_node or x[1] == c_node
#            return list(filter(connectors, conns))
#
#        conns = sorted(self.connections, key=itemgetter(0, 1))
#
#        results = self.n*[-1]
#        results[s] = 0
#        connected = [s]
#
#        while connected:
#            c_node = connected.pop(0)
#            to_check = get_to_check(c_node)
#
#            for elem in to_check:
#                conns.remove(elem)
#
#                if c_node != elem[0]:
#                    elem.reverse()
#
#                connected.append(elem[1])
#
#                if results[elem[1]] == -1:
#                    results[elem[1]] = results[elem[0]] + 6
#
#        results.remove(0) 
#        print(*results) 
            


from operator import itemgetter
from collections import defaultdict

class Graph():
    def __init__(self, n):
        self.n = n
        self.connections = defaultdict(set)

    def connect(self, x, y):
        self.connections[x].add(y)
        self.connections[y].add(x)
    
    def find_all_distances(self, s):
        def get_to_check(c_node):
            connectors = lambda x : x[0] == c_node or x[1] == c_node
            return list(filter(connectors, conns))

        results = self.n*[-1]
        results[s] = 0
        connected = [s]
        checked_nodes = set()

        while connected:
            c_node = connected.pop(0)
            checked_nodes.add(c_node)
            to_check = self.connections[c_node] - checked_nodes
            connected += list(to_check)

            for elem in to_check:
                if results[elem] == -1:
                    results[elem] = results[c_node] + 6

        results.remove(0) 
        print(*results) 
            
        
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)

    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)
