class Node:

    def __init__(self, val):
        self.val = val
        self.leader = val
        self.rank = 1

    def __repr__(self):
        return f"<Node {self.val} -> {self.leader}>"

class UFDS:

    def __init__(self, nlist):
        self.storage = {key: Node(key) for key in nlist}

    def find(self, key):
        node = self.storage[key]
        if node.leader == node.val:
            return node
        return self.find(node.leader)

    def union(self, n1, n2):
        l1 = self.find(n1)
        l2 = self.find(n2)
        if l1.rank == l2.rank:
            l2.leader = l1.val
            l1.rank += 1
        elif l1.rank > l2.rank:
            l2.leader = l1.val
        else:
            l1.leader = l2.val

    def same_set(self, n1, n2):
        return self.find(n1) == self.find(n2)
    
    def __repr__(self):
        return str(self.storage)

def kruskal(elist):
    # sort edge list by increasing weight
    slist = sorted(elist, key=lambda tup: tup[2])
    # create set n to capture all vertices in edge list
    n = set()
    for u, v, _ in slist:
        n.update([u, v])
    # intiialize ufds with all vertices from edgelist
    u = UFDS(range(len(n)))
    min_cost = 0
    for edge in slist:
        source, dest, weight = edge
        if not u.same_set(source, dest):
            min_cost += weight
            u.union(source, dest)
    return min_cost

if __name__ == "__main__":
    elist = [
        (0, 1, 4),
        (0, 2, 4),
        (0, 3, 6),
        (0, 4, 6),
        (1, 0, 4),
        (1, 2, 2),
        (2, 0, 4),
        (2, 1, 2),
        (2, 3, 8),
        (3, 0, 6),
        (3, 2, 8),
        (3, 4, 9),
        (4, 0, 6),
        (4, 3, 9)
        ]
    res = kruskal(elist)
    ans = 18
    assert res == ans




