in_file = open("input.txt", "r")
out_file = open("output.txt", "w")

t = int(in_file.readline())

for case_num in range(1, t+1):
    n, m = [int(x) for x in next(in_file).split()]
    reqs = [tuple(int(x) for x in next(in_file).split()) for _ in range(m)]

    # make nodes zero-based
    reqs = [(x-1, y-1, z) for x, y, z in reqs]

    # init node "connected-by-requirement" dict
    req_siblings = {}
    for x, y, _ in reqs:
        for p1, p2 in [(x, y), (y, x)]:
            if p1 not in req_siblings:
                req_siblings[p1] = set()
            req_siblings[p1].add(p2)

    # init graph weight matrix
    inf = 1000001
    w_mat = [[inf for _ in range(n)] for _ in range(n)]
    for x, y, z in reqs:
        w_mat[x][y] = z
        w_mat[y][x] = z

    # early exitable floyd-warshall
    def is_possible():
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    detour_w = w_mat[i][k]+w_mat[k][j]
                    if detour_w < w_mat[i][j]:
                        if i in req_siblings[j] or j in req_siblings[i]:
                            return False
                        w_mat[i][j] = detour_w
        return True

    # output generation
    output = "Case #{}: ".format(case_num)
    if is_possible():
        output += "{}\n".format(m)
        for x, y, z in reqs:
            output += "{} {} {}\n".format(x+1, y+1, z)
    else:
        output += "Impossible\n"

    out_file.write(output)
