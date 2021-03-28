import itertools

if __name__ == '__main__':
    data = [int(number) for number in open("input.txt", "r").read().split("\n")]
    find = 1038347917

    for i in range(len(data)):
        val = 0
        index = i
        while val < find:
            val += data[index]
            index += 1
        if val == find:
            result = data[i:index]


            print(i,index, result, min(result), max(result), min(result) + max(result))

