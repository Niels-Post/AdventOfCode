def find(data, currentbag):
    count = 1
    for bag in data:
        if bag[0][1] == currentbag[1] and bag[0][2] == currentbag[2]:
            for subbag in bag[1]:
                if not subbag[0] == "no":
                    count += int(subbag[0]) * find(data, subbag)
    return count


if __name__ == '__main__':
    print(find([(["1", *line.split("contain")[0].split(" ")],
                 [bag.split(" ")[1:] for bag in line.split("contain")[1].split(",")]) for line in
                open('input.txt', 'r').read().split("\n")]
          , ["1", "shiny", "gold", "bag"]))

    print((
        lambda find_recursive, data, currentbag: find_recursive(find_recursive, data, currentbag)
    )(
        lambda find_recursive, data, currentbag:
        [[[currentbag[0] * sum(find_recursive(find_recursive, data, newbag)) for newbag in bag[1]] for bag in data if
          bag[0][1] == currentbag[1] and bag[0][2] == currentbag[2]] if currentbag[0] != "no" else 1],

        [(["1", *line.split("contain")[0].split(" ")],
          [bag.split(" ")[1:] for bag in line.split("contain")[1].split(",")]) for line in
         open('input.txt', 'r').read().split("\n")],

        ["1", "shiny", "gold", "bag"]
    ))
