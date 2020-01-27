import random
import heapq
from collections import deque
    

class MinHeap:

    def __init__(self, list=None):
        if not list:
            self.heap = []
        else:
            self.heap = list
            heapq.heapify(self.heap)
        
    def __repr__(self):
        return f"<MinHeap: {self.heap}>"

    def __bool__(self):
        return bool(self.heap)

    def push(self, val):
        heapq.heappush(self.heap, val)

    def extract_min(self):
        return heapq.heappop(self.heap)


class Edge:

    def __init__(self, source, dest, weight=0):
        self.source = source
        self.dest = dest
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __repr__(self):
        return f"<Edge: d->{self.dest} w: {self.weight}>"


class Vertex:

    def __init__(self, id):
        self.id = id
        self.edges = []

    def __repr__(self):
        return f"<Vertex: {self.id} {self.edges}>"

    def add_edge(self, dest, weight=0):
        self.edges.append(Edge(self.id, dest, weight))

    def get_edges(self):
        return self.edges

    def __iter__(self):
        for edge in self.edges:
            yield edge


class Graph:

    def __init__(self):
        self.vertices = dict()

    def __repr__(self):
        b = "<Graph: {\n"
        m = ''
        for vertex in self.vertices.values():
            m += "  " + f"{vertex}," + '\n'
        e = "}>"
        return b+m+e

    def add_vertex(self, id):
        if id in self.vertices:
            raise KeyError(f"vertex {id} is already in graph!")
        self.vertices[id] = Vertex(id)

    def add_edge_to_vertex(self, id, dest, weight=0):
        if id not in self.vertices:
            raise KeyError(f"vertex {id} not found in graph!")
        if dest not in self.vertices:
            raise KeyError(f"vertex {dest} not found in graph!")
        self.vertices[id].add_edge(dest, weight)
        return self.vertices[id]
    
    def __getitem__(self, id):
        if id not in self.vertices:
            raise KeyError(f"vertex {id} not found in graph!")
        return self.vertices[id]

    def __iter__(self):
        for vertex in self.vertices:
            yield vertex

def random_graph_gen(n):
    g = Graph()
    for i in range(n):
        g.add_vertex(i)
    for i in range(n):
        for j in range(random.randint(0,n-1)):
            k = random.randint(0,n-1)
            if k != i:
                g.add_edge_to_vertex(i, k)
    return g

def dag_gen(n):
    g = Graph()
    l = [x for x in range(n)]
    random.shuffle(l)
    for i in range(len(l)):
        if not (i-1 > -1):
            g.add_vertex(l[i])
        else:
            g.add_vertex(l[i])
            g.add_edge_to_vertex(l[i-1], l[i])
    return g, l



def bfs(g, s):
    q = deque([s])
    visited = set()
    while q:
        v = q.popleft()
        print(f"{v} ->[", end="")
        edges = g[v]
        for dest in edges:
            if dest not in visited:
                q.append(dest)
                visited.add(dest)
                print(f"{dest},", end='')
        print("]")
        visited.add(v)

def dsearch(graph, start, visited):
    stack = list()
    stack.append(start)
    while stack:
        node = stack.pop()
        print(f"{node} ->[", end="")
        for dest in g[node]:
            print(f"{dest},", end="")
            if dest not in visited:
                stack.append(dest)
                visited.add(dest)
        print(f"]")

def dfs(g, s, stack, visited):
    visited.add(s)
    for dest in g[s]:
        if dest not in visited:
            visited.add(dest) 
            dfs(g, dest, stack, visited)
    stack.append(s)

def topological_sort(g):
    visited = set()
    stack = list()
    nodes = [x for x in g]
    for node in nodes:
        if node not in visited:
            dfs(g, node, stack, visited)
    return stack


def dijkstra(g, s, d):
    dist = {x:10**20 for x in g}
    dist[s] = 0
    prev = dict()
    visited = set()
    heap = MinHeap([Edge(s, s, 0)])
    while heap:
        edge = heap.extract_min()
        if edge.dest not in visited:
            visited.add(edge.dest)
            for e in g[edge.dest]: 
                heap.push(e)
                tdist = dist[e.source] + e.weight
                if tdist < dist[e.dest]:
                    dist[e.dest] = tdist
                    prev[e.dest] = e.source
    return dist, prev


if __name__ == '__main__':
    g, l = dag_gen(8)
    v = topological_sort(g)
    print(g)
    print(l)
    print(v)
    g = Graph()
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_edge_to_vertex(1,2,1)
    g.add_edge_to_vertex(2,3,1)
    g.add_edge_to_vertex(1,3,5)
    d, p = dijkstra(g, 1, 3)
    print(d)
    print(p)