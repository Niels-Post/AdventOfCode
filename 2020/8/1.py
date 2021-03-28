if __name__ == '__main__':
    operations = [(line.split(" ")[0],int(line.split(" ")[1])) for line in open("input.txt", "r").read().split("\n")]

    op_index = 0
    accumul = 0

    visited_ops = []
    while op_index not in visited_ops:
        visited_ops.append(op_index)

        op = operations[op_index]
        if op[0] == "acc":
            accumul += op[1]
        elif op[0] == "jmp":
            op_index += op[1]
            continue

        op_index += 1

    print(accumul)