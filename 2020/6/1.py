if __name__ == '__main__':
    print(
        sum(
            [len(set(x.replace("\n", ""))) for x in open("input.txt", "r").read().split("\n\n")]
        )
    )