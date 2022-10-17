from collections import defaultdict


class Graph(object):
    def __init__(self, nodes):
        self.graph = defaultdict(set)
        self.vertices = set()
        self.add_nodes(nodes)
        self.marks = {}

    def add_nodes(self, nodes):
        for node1, node2 in nodes:
            self.add(node1, node2)

    def add(self, node1, node2):
        if node2 not in self.graph[node1] and node1 != node2:
            self.graph[node1].add(node2)
            self.vertices.add(node1)
            self.vertices.add(node2)
            return
        # print('unable to add vertex')    

    def is_cyclic(self):
        for v in self.vertices:
            self.marks[v] = False
        try:
            for v in self.vertices:
                if not self.marks[v]:
                    self.dfs(v)
        except RecursionError:
            return True
        else:
            return False

    def dfs(self, v):
        for u in self.graph[v]:
            if not self.marks[u]:
                self.dfs(u)
        self.marks[v] = True

    def __str__(self):
        return 'Graph({})'.format(dict(self.graph))

def test_util():
    g = Graph([])
    print(g)
    edges = [('A', 'B'), ('B', 'C')]
    g.add_nodes(edges)
    print(g)
    # g.add('J', 'K')
    # print(g)
    # g.add('A', 'C')
    # print(g)
    # g.add('A', 'C')
    # print(g)
    # g.add('A', 'A')
    print(g)
    print(g.is_cyclic())
    print(g.vertices)

if __name__ == '__main__':
    test_util()