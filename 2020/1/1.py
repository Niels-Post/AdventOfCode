import itertools

if __name__ == '__main__':
    print(
        next(
            (*el, el[0] * el[1]) for el in filter(
                lambda el: el[0] + el[1] == 2020,
                itertools.combinations([int(line.strip()) for line in open("input.txt", "r").readlines()], 2)
            )
        )
    )
