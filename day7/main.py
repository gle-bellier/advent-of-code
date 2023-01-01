from __future__ import annotations





class Dir:
    def __init__(self, name: str,  parent: Dir | None) -> None:
        self.parent = parent 
        self.name = name
        self.childs = []
        self.size = 0
        
    def __repr__(self) -> str:
        return f"Dir {self.name}"

class File:
    def __init__(self, name: str, parent: Dir, size: int) -> None:
        self.parent = parent
        self.size = size
        self.name = name
    
    def __repr__(self) -> str:
        return f"File {self.name}"

class TreeBuilder:
    def __init__(self, commands: list[Command]) -> None:
        self.commands = commands
        self.root = Dir(name="/", parent=None)
        self.current = self.root 


    def run(self) -> None:
        for c in self.commands:
            self.run_command(c) 


    def create_dir(self, name:str) -> None:
        # create new dir
        new_dir = Dir(name=name, parent=self.current)
        self.current.childs += [new_dir]
        print("Create Dir ", name)

    def create_file(self, name: str, size: int ) -> None:
        # create new file
        new_file = File(name=name, parent=self.current, size=size) 
        self.current.childs += [new_file]
        
        # update folders sizes
        self.update_dir_size(self.current, size)
        

    def update_dir_size(self, dir: Dir, size: int) -> None:
        dir.size += size
        if dir.parent is not None:
            self.update_dir_size(dir.parent, size)

    def change_directory(self, command: Cd) -> None:
        if command.dir == "..":
            # if it is not the root dir
            if self.current.parent is not None:
                self.current = self.current.parent

        # look at childs of the current dir
        for child in self.current.childs:
            if isinstance(child, Dir) and child.name == command.dir:
                # update current
                print(f"{self.current.name} -> {child.name}")
                self.current = child

    def run_command(self, command: Command) -> None:
       
        if isinstance(command, Ls):
            for elt in command.rslt:

                pre, suf = elt.split(" ")
                
                if pre == "dir":
                    self.create_dir(name=suf)

                else:
                    self.create_file(size=int(pre), name=suf)

        elif isinstance(command, Cd):
            self.change_directory(command=command)



class TreeAnalyzer:
    def __init__(self, root: Dir) -> None:
        self.root = root


    def get_sum_over_100k(self) -> int:
        return self.sum_over_100k(self.root)

    def sum_over_100k(self, dir: Dir) -> int:
        s = 0
        if dir.size < 100_000:
            # nothing to add
            s += dir.size
        
        for c in dir.childs:
            if isinstance(c, Dir):
                s += self.sum_over_100k(c)
        return s


    def min_size_dir_above_threshold(self, dir: Dir, threshold: int) -> int:
        if dir.size < threshold:
            return float("inf")
        else:
            sizes = [dir.size]
            for c in dir.childs:
                if isinstance(c, Dir):
                    sizes += [self.min_size_dir_above_threshold(c, threshold)]
            return min(sizes) 



    def free_space(self, space: int, needed_space: int) -> int:

        space_to_find = needed_space - (space - self.root.size)
        
        return self.min_size_dir_above_threshold(self.root, threshold=space_to_find)

        
            


class Command:
    pass

class Cd(Command):
    def __init__(self, dir: "str") -> None:
        self.dir = dir
        

    def __repr__(self) -> str:
        return f"Change directory to: {self.dir}"
        


class Ls(Command):
    def __init__(self, rslt: list[str]) -> None:
        self.rslt = rslt
        
    def __repr__(self) -> str:
        rp = "ls \n"
        for elt in self.rslt:
            rp += f"- {elt}\n"
        return rp 
            

def parse_input(filename: str) -> list:
    l_command = []
    buffer_ls = []
    is_ls = False
    with open(filename, "r") as file:
        while True: 
            line = file.readline()
            if line == "":
                # end of the file
                # check the buffer
                if is_ls:
                    l_command += [Ls(rslt=buffer_ls)]
                return l_command[1:]
            else:
                # remove the \n
                line = line[:-1]
                elts = line.split(" ")
                # test if its a command line
                if elts[0] == "$":
                    # this is a command so we have to empty the buffer
                    if is_ls:
                        l_command += [Ls(rslt=buffer_ls)]
                        # reset buffer
                        buffer_ls = []
                        is_ls = False
                    
                    if elts[1]=="cd":
                        l_command += [Cd(dir=elts[2])]            
                        
                    else: 
                        # ls command
                        is_ls = True
                else:
                    # this is not a command:
                    buffer_ls += [line]

# parse input
commands = parse_input("input.txt")

# build tree
tb = TreeBuilder(commands = commands)
tb.run()

# analyse tree
ta = TreeAnalyzer(root = tb.root)
print(ta.get_sum_over_100k())
print(ta.free_space(space=70_000_000, needed_space=30_000_000))

