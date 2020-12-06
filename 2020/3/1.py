if __name__ == '__main__':
    print(
        sum(
            (
                lambda data: [1 if data[i][j % len(data[0])] == "#" else 0 for (i, j) in zip(range(1, len(data)), range(3, len(data[0]) * len(data) , 3))]
            )([line.strip() for line in open("input.txt", "r").readlines()])
        )
    )

