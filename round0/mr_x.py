in_file = open("input.txt", "r")
out_file = open("output.txt", "w")

t = in_file.readline()  # unused

vars = set(['x', 'X'])
consts = set(['1', '0'])
terms = vars.union(consts)
ops = set(['&', '|', '^'])
neg_map = {
    'x': 'X',
    'X': 'x',
    '1': '0',
    '0': '1'
}

for i, line in enumerate(in_file, 1):
    term_stack = []
    op_stack = []

    for j, ch in enumerate(line):
        if ch in terms:
            term_stack.append(ch)
        elif ch in ops:
            op_stack.append(ch)
        elif ch == ')':
            t2 = term_stack.pop(-1)
            t1 = term_stack.pop(-1)
            op = op_stack.pop(-1)

            if t1 in consts or t2 in consts:
                (ct, ot) = (t1, t2) if t1 in consts else (t2, t1)

                one_present = ct == '1'
                if op == '&':
                    res = ot if one_present else ct
                elif op == '|':
                    res = ct if one_present else ot
                else:
                    res = neg_map[ot] if one_present else ot
            else:
                terms_match = t1 == t2
                if op == '&':
                    res = t1 if terms_match else '0'
                elif op == '|':
                    res = t1 if terms_match else '1'
                else:
                    res = '0' if terms_match else '1'

            term_stack.append(res)

    assert len(term_stack) == 1 and len(op_stack) == 0
    n_changes = 1 if term_stack[0] in vars else 0

    out_file.write("Case #{}: {}\n".format(i, n_changes))
