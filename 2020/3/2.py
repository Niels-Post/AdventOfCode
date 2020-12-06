import functools
import operator

if __name__ == '__main__':
    print(
        functools.reduce(operator.mul,
                         (lambda data:
                          [sum([1 if data[i][j % len(data[0])] == "#" else 0
                           for (i, j) in zip(range(down, len(data), down), range(right, len(data[0]) * 10000, right))])
                           for (right, down) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
                          )([line.strip() for line in open("input.txt", "r").readlines()])
                         )
    )
