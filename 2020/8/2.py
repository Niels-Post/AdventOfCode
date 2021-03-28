if __name__ == '__main__':
    operations = [(line.split(" ")[0],int(line.split(" ")[1])) for line in open("input.txt", "r").read().split("\n")]


    for i in range(len(operations)):
        op_index = 0
        accumul = 0
        visited_ops = []
        while op_index not in visited_ops and op_index < len(operations):
            visited_ops.append(op_index)

            op = operations[op_index]
            op_name = op[0]

            if op_index == i and (op_name == "nop" or op_name == "jmp"):
                op_name = "nop" if op_name == "jmp" else "jmp"

            if op_name == "acc":
                accumul += op[1]
            elif op_name == "jmp":
                op_index += op[1]
                continue

            op_index += 1
        # print("-", visited_ops)
        if op_index >= len(operations):
            print("yah")
            print(accumul)
            print(op_index)
            print("------------")

    print(accumul)


