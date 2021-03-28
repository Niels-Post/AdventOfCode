memoi = [-1 for _ in range(200)]


def find_possibilities(data, index=0):
    if index == len(data)-1:
        return 1

    if memoi[index] != -1:
        return memoi[index]

    first = data[index]

    count = 0

    for i in range(index + 1, min(index + 15, len(data))):
        if data[i] <= first + 3:
            count += find_possibilities(data,  i)
    memoi[index] = count
    return count


if __name__ == '__main__':
    data = sorted([int(joltage) for joltage in open("input.txt", "r").read().split("\n")])
    data = [0,*data,max(data)+3]
    print(find_possibilities(data))
