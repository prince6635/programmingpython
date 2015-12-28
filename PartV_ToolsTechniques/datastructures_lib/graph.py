# Each Graph object only has one node and its corresponding edges
class Graph:
    "build graph with objects that know how to search"
    def __init__(self, label):
        self.name = label
        self.edges = []

    def search(self, goal):
        Graph.solutions = []
        self.doSearch([self], goal) # (from, to)
        Graph.solutions.sort(key=lambda x : len(x))
        return Graph.solutions

    def doSearch(self, curPath, goal):
        if self == goal:
            Graph.solutions.append(curPath)
        else:
            for edge in self.edges:
                if edge not in curPath:
                    edge.doSearch(curPath + [edge], goal)

    def __repr__(self):
        return self.name

def testGraph():
    for name in "ABCDEFG":
        exec("%s = Graph('%s')" % (name, name))

    A.edges = [B, E, G]
    B.edges = [C]
    C.edges = [D, E]
    D.edges = [F]
    E.edges = [C, F, G]
    G.edges = [A]

    print(A.search(G))
    for (start, stop) in [(E,D), (A,G), (G,F), (B,A), (D,A)]:
        print(start.search(stop))

# Common implementation, the whole graph includes multiple nodes and all the edges between them
class GraphFinal:
    def __init__(self, graphInDict={}):
        self.graph = graphInDict

    def search(self, start, goal):
        solutions = []
        self.doSearch([start], goal, solutions)
        solutions.sort(key=lambda x : len(x))
        return solutions

    def doSearch(self, curPath, goal, solutions):
        state = curPath[-1]
        if state == goal:
            solutions.append(curPath)
        else:
            for edge in self.graph[state]:
                if edge not in curPath:
                    self.doSearch(curPath + [edge], goal, solutions)

    # No recursion, use paths stack instead
    def searchWihoutRecursion(self, start, goal):
        solutions = []
        paths = ([start], []) # use a tuple-stack
        while paths:
            front, paths = paths # pop the top path
            state = front[-1]
            if state == goal:
                solutions.append(front)
            else:
                for edge in self.graph[state]:
                    if edge not in front:
                        paths = (front + [edge]), paths
        return solutions


def testGraphFinal():
    g = GraphFinal({
        'A': ['B', 'E', 'G'],
        'B': ['C'],
        'C': ['D', 'E'],
        'D': ['F'],
        'E': ['C', 'F', 'G'],
        'F': [],
        'G': ['A'],
    })

    # print(g.search('E', 'D'))
    print(g.searchWihoutRecursion('E', 'D'))
    print("All paths:")
    for x in ['AG', 'GF', 'BA', 'DA']:
        # print(x, g.search(x[0], x[1]))
        print(x, g.searchWihoutRecursion(x[0], x[1]))

