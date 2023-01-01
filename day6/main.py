def is_marker(win: str) -> bool:
    for i in range(len(win) - 1):
        for j in range(i + 1, len(win)):
            if win[i] == win[j]:
                return False

    return True


def marker_index(txt: str) -> int | None:
    index = 0
    while index < len(txt) - 1:
        win = txt[index : index + 14]
        if is_marker(win):
            return index + 14

        index += 1

    return None


filename = "input.txt"
txt = open(filename, "r").readline()

print(marker_index(txt))
