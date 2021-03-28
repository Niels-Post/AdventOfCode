import sys

def flatten(something: list):
    lst = []
    for item in something:
        if type(item) is tuple:
            lst.append(item)
        else:
            lst.extend(flatten(item))
    return lst

if __name__ == '__main__':
    print(
        [(line.split("contain")[0].split(" "), [bag.split(" ")[2:] for bag in line.split("contain")[1].split(",")]) for
         line in
         open('input.txt', 'r').read().split("\n")])
    print(len(set(flatten((
        lambda find_recursive, data,currentbag: find_recursive(find_recursive,data,currentbag)
    ) (
    lambda find_recursive, data, currentbag: [[*find_recursive(find_recursive, data, new_bag[0]), tuple(new_bag[0])]
                                              for new_bag in data if
                                              any(currentbag[0] == test_child_bag[0] and currentbag[1] == test_child_bag[1] for test_child_bag in new_bag[1])],
        [(line.split("contain")[0].split(" "), [bag.split(" ")[2:] for bag in line.split("contain")[1].split(",")]) for
         line in
         open('input.txt', 'r').read().split("\n")],
        ["shiny", "gold", "bag"]
    )))))


