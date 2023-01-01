import numpy as np



class Board:

    def __init__(self) -> None:
        self.H = (0, 0)
        self.T = (0, 0)
        self.H_buffer = self.H
        self.visited_T = [(0, 0)]

    @property
    def ht_distance(self) -> int:
        return max(abs(self.H[0] - self.T[0]), abs(self.H[1] - self.T[1]))

    @property
    def nb_visited_T(self) -> int:
        return len(self.visited_T)

    def move(self, direction: str) -> None:
        i, j = self.H
        if direction == "U":
            i -= 1
        elif direction == "D":
            i += 1
        elif direction == "L":
            j -= 1
        else:
            j += 1

        self.H_buffer = self.H
        self.H = (i, j)
        if self.ht_distance > 1:
            self.move_tail()


    def move_tail(self) -> None:
        print(f"{self.T} -> {self.H_buffer}\n")
        self.T = self.H_buffer
        if not self.T in self.visited_T:
            self.visited_T.append(self.T)
            
            
            
    def __repr__(self) -> str:
        size = 10_000
        m = np.zeros((size, size))
        m[self.T[0]+size//2, self.T[1]+size//2] = 2
        m[self.H[0] + size//2, self.H[1]+size//2] = 1
        s = f"{self.H_buffer}\n"
        for line in m:
            for elt in line:
                if elt == 1:
                    s+="H"
                elif elt == 2:
                    s+="T"
                else:
                    s+="."
            s+="\n"
        return s
        

def parse_input(filename: str) -> str:
    lines = open(filename, "r").readlines() 
    lines = [l[:-1] for l in lines]
    s = ""
    for l in lines:
       direction, number = l.split(" ") 
       s += direction * int(number)
    return s

def run(commands: str):
    b = Board()
    for direction in commands:
        b.move(direction)
        
    print("Result: ")
    print(b.nb_visited_T)
    print(b)

commands = parse_input("input.txt")
print(len(commands))
run(commands)

