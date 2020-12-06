if __name__ == '__main__':

    print(
        (
            lambda lst: next(filter(lambda el : el[1] - lst[el[0]-1] > 1, enumerate(lst)))[1]-1
        )
        (
            (
                lambda find, input:
                sorted(
                    [find(find, instruction[:-3], [i for i in range(128)], "F") * 8 + find(find, instruction[-3:],[i for i in range(8)], "L") for instruction in input]
                )
            )(
                lambda self, string, rows, lower_char: self(
                    self, string[1:],rows[0:int(len(rows) / 2)] if string[0] == lower_char
                    else rows[int(len(rows) / 2):],lower_char) if len(rows) > 1
                    else rows[0],
                    [direction for direction in open("input.txt", "r").read().split("\n")]
            )
        )
    )
