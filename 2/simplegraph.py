def create_am(n, edges):
    matrix = [[0 for _ in range(n)] for _ in range(n)]  # initialize matrix to size VxV
    for i in range(n):
        for j in edges[i]:
            matrix[i][
                j
            ] = 1  # set location in matrix of vertex i to vertex j to weight 1
    return matrix


def create_adjlist(n, edges):
    adj = []
    for row in edges:
        adj.append(row)  # append each edge to the start vertex
    return adj


def create_edgelist(n, edges):
    elist = []
    for i in range(n):
        for j in edges[i]:
            elist.append((i, j))  # append tuple for each edge
    return elist


def am_al(am):
    al = []
    n = len(am)
    for i in range(n):
        al.append([])
        for j in range(n):
            if am[i][j] != 0:
                al[i].append(j)
    return al


def am_el(am):
    el = []
    n = len(am)
    for i in range(n):
        for j in range(n):
            if am[i][j] != 0:  # check value and append index
                el.append((i, j))
    return el


def al_am(al):
    am = [[0 for _ in range(len(al))] for _ in range(len(al))]
    for i in range(len(al)):
        for j in al[i]:
            am[i][j] = 1
    return am


def al_el(al):
    el = []
    for i in range(len(al)):
        for j in al[i]:
            el.append((i, j))
    return el


def el_am(el):
    v = set()  # create set to find all unique nodes in list
    for i, j in el:
        v.add(i)
        v.add(j)
    am = [[0 for _ in range(len(v))] for _ in range(len(v))]
    for i, j in el:
        am[i][j] = 1
    return am


def el_al(el):
    v = set()
    for i, j in el:
        v.add(i)
        v.add(j)
    al = [[] for _ in range(len(v))]
    for i, j in el:
        al[i].append(j)
    return al


def create_wam(n, wedges):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j, w in wedges[i]:
            matrix[i][j] = w
    return matrix


def create_wadjlist(n, wedges):
    adj = []
    for i in range(n):
        adj.append([])
        for j, w in wedges[i]:
            adj[i].append((j, w))
    return adj


def create_wedgel(n, wedges):
    welist = []
    for i in range(n):
        for j, w in wedges[i]:
            welist.append((i, (j, w)))
    return sorted(welist, key=lambda tup: (tup[1][1], tup[1][0]))


if __name__ == "__main__":
    n = 3
    edges = [[1, 2], [2, 0], [1, 0]]
    am = create_am(n, edges)
    al = create_adjlist(n, edges)
    el = create_edgelist(n, edges)
    print("### am ###")
    for line in am:
        print(line)
    amel = am_el(am)
    print(amel)
    amal = am_al(am)
    print(amal)
    print("###########")

    print("### adjlist ###")
    print(al)
    alam = al_am(al)
    assert alam == am
    for line in alam:
        print(line)
    alel = al_el(al)
    print(alel)
    print("###############")

    print("### edgelist ###")
    print(el)
    elal = el_al(el)
    print(elal)
    elam = el_am(el)
    assert elam == am
    for line in elam:
        print(line)
    print("################")

    # all exercises done for weighted graphs below
    n = 3
    wedges = [
        [(1,3),(2,2)],
        [(2,1),(0,8)],
        [(1,2),(0,7)],
    ]
    i = create_wam(n, wedges)
    print('wam')
    for line in i:
        print(line)
    j = create_wadjlist(n, wedges)
    print('wadjlist')
    for line in j:
        print(line)
    k = create_wedgel(n, wedges)
    print('wedgelist')
    for line in k:
        print(line)
