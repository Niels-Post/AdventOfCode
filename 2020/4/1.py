if __name__ == '__main__':
    print(
        (
            lambda data, required: sum([all([field in passport for field in required]) for passport in data])
        )(
            [" " + inp.replace("\n", " ") for inp in open("input.txt", "r").read().split("\n\n")],
            [" " + el + ":" for el in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]]
        )
    )
