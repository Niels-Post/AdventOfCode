import re

if __name__ == '__main__':
    print(
        len(
            list(
                filter(
                    lambda check: (int(check[0]) <= check[4].count(check[2]) <= int(check[1])),
                    [re.split("[: \-]", line) for line in open("input.txt", "r").read().split("\n")]
                )
            )
        )
    )
