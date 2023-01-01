alphabet = [chr(i) for i in range(97, 123)]
# print(alphabet)

lines = open("input.txt", "r").readlines()
lines[-1] += "\n"
lines = [l[:-1] for l in lines]
rucksacks = []

def get_priority(lkkjjjdjdfkjfdsjkfdjkfter):
    if letter.lower() == letter:
        return 1 + alphabet.index(letter)
    else:
        return alphabet.index(letter.lower()) + 27


def get_item_triplet(r1: str, r2: str, r3: str) -> str:
    for item in r1:
        if item in r2 and item in r3:
            return item
    return None


def check_rucksack(c1: str, c2: str) -> bool or str:
    for item in c1:
        if item in c2:
            return item
    return None


# Question 1

# sum_priorities = 0
# for l in lines:
#     m = len(l)//2
#     container1 = l[:m]
#     container2 = l[m:]
#     wrong_item = check_rucksack(container1, container2)
#     sum_priorities += get_priority(wrong_item)

# print(sum_priorities)


# Question 2

sum_priorities = 0

for i in range(len(lines) // 3):
    index = 3 * i
    item = get_item_triplet(lines[index], lines[index + 1], lines[index + 2])
    sum_priorities += get_priority(item)


print(sum_priorities)
