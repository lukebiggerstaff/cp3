import random

class MaxHeap:

    def __init__(self, l=None):
        if not l:
            self.data = []
        else:
            self.data = l
            self._build_heap()

    def __repr__(self):
        return f"<MaxHeap: {self.data}>"

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def _build_heap(self):
        n = len(self.data) // 2
        for i in range(n, -1, -1):
            self._heapify(i)

    def _heapify(self, i):
        l = self._left(i)
        r = self._right(i)
        n = len(self.data)
        largest = i
        if l < n and self.data[l] > self.data[i]:
            largest = l
        if r < n and self.data[r] > self.data[largest]:
            largest = r
        if largest != i:
            self._swap(i, largest)
            self._heapify(largest)

    def insert(self, val):
        self.data.append(val)
        i = len(self.data) - 1
        p = i // 2
        while p >= 0 and self.data[i] > self.data[p]:
            self._swap(i, p)
            i = p
            p = i // 2

    def extract_max(self):
        val = self.data[0]
        last = len(self.data)-1
        self.data[0] = self.data[last]
        del self.data[last]
        self._heapify(0)
        return val

def heapsort(lst):
    b = MaxHeap(lst)
    l = []
    while b.data:
        l.append(b.extract_max())
    return l
    
def random_list():
    l = []
    for i in range(20):
        l.append(i)
    random.shuffle(l)
    return l

def is_sorted(lst, l=None, r=None):
    if not l: l = 0
    if not r: r = 1
    if r >= len(lst) - 1: return True
    return lst[l] >= lst[r] and is_sorted(lst, l+1, r+1)



if __name__ == '__main__':
    b = MaxHeap([3, 2, 4, 8, 9, 12, 45, 29, 80])
    print(b)
    b.insert(1)
    assert 1 in b.data

    c = random_list()
    d = heapsort(c)
    print(d)
    assert is_sorted(d) is True