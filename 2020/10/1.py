if __name__ == '__main__':
    last_diff = 0
    diffs = [0 for i in range(10)]
    diffs[3] = 1
    for jolt in sorted([int(joltage) for joltage in open("input.txt", "r").read().split("\n")]):
        diffs[jolt - last_diff] += 1
        last_diff = jolt
    print(sorted([int(joltage) for joltage in open("input.txt", "r").read().split("\n")]))
    print(diffs)
    print(diffs[1] * diffs[3])