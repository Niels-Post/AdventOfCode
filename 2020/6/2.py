import string
if __name__ == '__main__':
    print(
        sum(
            [
                len(
                    list(
                        filter(
                            lambda letter : all([letter in person for person in group.split("\n")]), string.ascii_lowercase
                        )
                    )
                ) for group in open("input.txt", "r").read().split("\n\n")
            ]
        )
    )
