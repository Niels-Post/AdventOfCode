import re

if __name__ == '__main__':
    print(
        len(
            list(
                filter(
                    lambda check: ((check[4][int(check[0]) - 1] == check[2]) != (check[4][int(check[1]) - 1] == check[2])),
                    [re.split("[: \-]", line) for line in open("input.txt", "r").read().split("\n")]
                )
            )
        )
    )
