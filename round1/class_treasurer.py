in_file = open("input.txt", "r")
out_file = open("output.txt", "w")

mod = int(1e9+7)
t = int(in_file.readline())

for case_num in range(1, t+1):
    _, k = [int(x) for x in next(in_file).split()]
    votes = [1 if x == 'B' else -1 for x in next(in_file).strip()]

    # updating maximum sum
    cost = 0
    local_cost = 0
    for i in range(len(votes)-1, -1, -1):
        local_cost += votes[i]
        if local_cost > k:
            cost = (cost + pow(2, i+1, mod))
            local_cost -= 2

        local_cost = max(0, local_cost)

    out_file.write("Case #{}: {}\n".format(case_num, cost % mod))
