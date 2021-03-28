import itertools

if __name__ == '__main__':
    data = [int(number) for number in open("input.txt", "r").read().split("\n")]
    for i in range(25, len(data)):
        val = data[i]
        for left, right in itertools.combinations(data[i - 25:i], 2):
            if left + right == val:
                break
        else:
            print(val, i)
