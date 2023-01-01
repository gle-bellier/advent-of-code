


class Stacks:
    def __init__(self) -> None:
        self.stacks = []

    def add_stack(self, stack: list) -> None:
        # add new stack to the stacks.
        self.stacks.append(stack)


    def __repr__(self) -> str:
        return str(self.stacks)


    # def move_crate(self, start: int, destination: int) -> None:

    #     # get crate to move 
    #     crate = self.stacks[start].pop()
    #     # add crate to the right stack
    #     self.stacks[destination] += [crate]    


    # def move(self, number: int, start: int, destination: int) -> None:
    #     for _ in range(number):
    #         self.move_crate(start, destination)


    def move(self, number: int, start: int, destination: int)-> None:

        crates_to_move = self.stacks[start][-number:]
        # update start
        self.stacks[start] = self.stacks[start][:-number]
        self.stacks[destination] += crates_to_move



    @property
    def top_crates(self):
        top = ""
        for stack in self.stacks:
            top += stack[-1]

        return top

def parse_sentence(sentence: str):

    a, b = sentence.split("from")
    _, number = a.split("move")
    start, destination = b.split("to")

    return int(number), int(start) - 1, int(destination) -1


def run_instructions(stacks: Stacks, filename: str) -> Stacks:
    with open(filename, "r") as f:
        line = f.readline()
        while line != "":
            number, start, destination = parse_sentence(line) 
            # apply instructions
            stacks.move(number, start, destination)
            line = f.readline()

        return stacks

        


stacks = Stacks()
stacks.add_stack(["Q", "S", "W", "C", "Z", "V", "F", "T"])
stacks.add_stack(["Q", "R", "B"])
stacks.add_stack(["B", "Z", "T", "Q", "P", "M", "S"])
stacks.add_stack(["D", "V", "F", "R", "Q", "H"])
stacks.add_stack(["J", "G", "L", "D", "B", "S", "T", "P"])
stacks.add_stack(["W", "R", "T", "Z"])
stacks.add_stack(["H", "Q", "M", "N", "S", "F", "R", "J"])
stacks.add_stack(["R", "N", "F", "H", "W"])
stacks.add_stack(["J", "Z", "T", "Q", "P", "R", "B"])

run_instructions(stacks, "instructions.txt")
print(stacks.top_crates)