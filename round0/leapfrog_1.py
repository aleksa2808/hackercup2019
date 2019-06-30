in_file = open("input.txt", "r")
out_file = open("output.txt", "w")

t = in_file.readline()  # unused

for i, line in enumerate(in_file, 1):
    empty_pads = line.count(".")
    betas = line.count("B")

    possible = "N" if empty_pads == 0 or betas-empty_pads < 0 else "Y"

    out_file.write("Case #{}: {}\n".format(i, possible))
