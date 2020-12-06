import string


def main():
    print(
        (
            lambda data, validation: sum(
                [
                    all(
                        [
                            field in passport and valid(passport.split(field)[1].split(" ")[0])
                            for field, valid in validation
                        ]
                    )
                    for passport in data]
            )
        )
        (
            [" " + inp.replace("\n", " ") for inp in open("input.txt", "r").read().split("\n\n")],
            [
                (" byr:", lambda val: val.isdigit() and 1920 <= int(val) <= 2002),
                (" iyr:", lambda val: val.isdigit() and 2010 <= int(val) <= 2020),
                (" eyr:", lambda val: val.isdigit() and 2020 <= int(val) <= 2030),
                (" hgt:", lambda val: 59 <= int(val[:-2]) <= 76 if val[-2:] == "in" else 150 <= int(val[:-2]) <= 193 if val[-2:] == "cm" else False),
                (" hcl:",lambda val: val[0] == "#" and all(char in string.hexdigits for char in val[1:]) and len(val) == 7),
                (" ecl:", lambda val: any(val == allowed for allowed in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])),
                (" pid:", lambda val: len(val) == 9 and val.isdigit())
             ]
        )
    )


if __name__ == '__main__':
    main()
