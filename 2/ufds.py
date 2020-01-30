class Node:
    """
    a node of the union find data structure, stores its
    identity, leader, and rank.
    """

    def __init__(self, val):
        self.val = val
        self.leader = val
        self.rank = 1

    def __repr__(self):
        return f"<Node id={self.val:2} r={self.rank:2} l={self.leader:2}>"


class UnionFind:
    """
    Union Find data structure
    supports find() and union()
    """

    def __init__(self, nodes):
        self.storage = {key: Node(key) for key in nodes}

    def find(self, key):
        node = self.storage[key]
        if node.leader == node.val:
            return node
        return self.find(node.leader)

    def union(self, n1, n2):
        l1 = self.storage[self.find(n1).val]
        l2 = self.storage[self.find(n2).val]
        if l1.rank == l2.rank:
            l2.leader = l1.val
            l1.rank += 1
        elif l1.rank > l2.rank:
            l2.leader = l1.val
        else:
            l1.leader = l2.val

    def num_sets(self):
        total = set()
        for node in self.storage:
            total.add(self.find(node))
        return len(total)

    def size_of_set(self, i):
        total = 0
        s = self.find(i)
        for node in self.storage:
            if self.find(node) == s:
                total += 1
        return total

    def __repr__(self):
        string = ""
        string += "<UFDS {\n"
        for node in self.storage:
            string += f"\t[{self.storage[node]}]" + "\n"
        string += "}>"
        return string


if __name__ == "__main__":
    intuf = UnionFind(list(range(11)))
    assert intuf.find(0) == intuf.storage[0]

    intuf.union(0, 1)
    assert intuf.find(0) == intuf.storage[0]
    assert intuf.storage[0].rank == 2

    intuf.union(0, 2)
    assert intuf.find(2) == intuf.storage[0]
    assert intuf.storage[0].rank == 2

    intuf.union(3, 4)
    intuf.union(3, 5)
    intuf.union(3, 6)
    assert intuf.find(3) == intuf.storage[3]
    assert intuf.storage[3].rank == 2
    assert intuf.find(5) == intuf.storage[3]

    intuf.union(0, 3)
    assert intuf.find(0) == intuf.storage[0]
    assert intuf.find(3) == intuf.storage[0]
    assert intuf.storage[0].rank == 3
    assert intuf.storage[3].rank == 2
    assert intuf.find(5) == intuf.storage[0]
