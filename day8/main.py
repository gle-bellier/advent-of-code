import numpy as np


def parse_input(filename: str) -> np.ndarray:

    lines = open(filename, "r").readlines()
    lines = [l[:-1] for l in lines]
    lines = [np.array([int(i) for i in l]) for l in lines]
    return np.stack(lines)

class Tree:
    def __init__(self, height: int) -> None:
        self.height = height
        # UP, DOWN, LEFT, RIGHT
        self.visible = [True, True, True, True]
    
    @property
    def is_visible(self) -> bool:
        for v in self.visible:
            if v:
                return True
        return False

        
    def visible_str(self) -> str:
        s = ""
        for v in self.visible:
            if v:
                s+="o"
            else:
                s+="x"
        return s


    def __repr__(self) -> str:
        return f"(h: {self.height})-{self.visible_str()}."
        


class Forest:
    def __init__(self, height: np.ndarray) -> None:
        self.height = height
        self.forest = self.get_forest(self.height)

    
    def scan_rows(self, i: int) -> None:
        
        max_height = self.forest[i, 0].height
        # from left to right
        for j in range(1, self.forest.shape[1]):
            tree = self.forest[i, j]
            
            if tree.height > max_height:
                max_height = tree.height
            else:
                tree.visible[2] = False
            

        max_height = self.forest[i, -1].height
        for j in range(self.forest.shape[1]-2, -1, -1):
            tree = self.forest[i, j]
            if tree.height > max_height:
                max_height = tree.height
            else:
                tree.visible[3] = False
                    
    def scan_columns(self, j: int) -> None:
        
        max_height = self.forest[0, j].height
        # from left to right
        for i in range(1, self.forest.shape[1]):
            tree = self.forest[i, j]
            
            if tree.height > max_height:
                max_height = tree.height
            else:
                tree.visible[0] = False

        max_height = self.forest[-1, j].height
        for i in range(self.forest.shape[1]-2, -1, -1):
            tree = self.forest[i, j]
            if tree.height > max_height:
                max_height = tree.height
            else:
                tree.visible[1] = False

    def scan(self) -> None:
        for i in range(self.forest.shape[0]):
            self.scan_rows(i)
        
        for j in range(self.forest.shape[1]):
            self.scan_columns(j)

            

    @property
    def nb_visible_tree(self) -> int:
        
        visible_trees = []
        for i in range(self.forest.shape[0]):
            for j in range(self.forest.shape[1]):
                t = self.forest[i, j]
                if t.is_visible:
                    visible_trees += [t] 
        return len(visible_trees)
                


    
    def distance_down(self, i: int, j: int) -> int:
        start = {"i": i, "j": j, "h": self.height[i, j]}
        return self.run_down(i, j, start)
         
    def run_down(self, x: int, y: int, start: dict) -> int:
        # if border 
        if x == self.height.shape[0]:
            return 0
        # if starting point
        elif (x, y) == (start["i"], start["j"]):
            return self.run_down(x+1, y, start)
        
        elif self.height[x, y] >= start["h"] and x != start["i"]:
            return 1
        else:
            return 1 + self.run_down(x+1, y, start) 
            
            
    def distance_up(self, i: int, j: int) -> int:
        start = {"i": i, "j": j, "h": self.height[i, j]}
        return self.run_up(i, j, start)
         
    def run_up(self, x: int, y: int, start: dict) -> int:
        # if border 
        if x == -1:
            return 0
        # if starting point
        elif (x, y) == (start["i"], start["j"]):
            return self.run_up(x-1, y, start)
        elif self.height[x, y] >= start["h"] and x != start["i"]:
            return 1
        else:
            return 1 + self.run_up(x-1, y, start) 


    def distance_left(self, i: int, j: int) -> int:
        start = {"i": i, "j": j, "h": self.height[i, j]}
        return self.run_left(i, j, start)
         
    def run_left(self, x: int, y: int, start: dict) -> int:
        # if border 
        if y == -1:
            return 0
        # if starting point
        elif (x, y) == (start["i"], start["j"]):
            return self.run_left(x, y-1, start)
        elif self.height[x, y] >= start["h"] and y != start["j"]:
            return 1
        else:
            return 1 + self.run_left(x, y-1, start) 
    
    def distance_right(self, i: int, j: int) -> int:
        start = {"i": i, "j": j, "h": self.height[i, j]}
        return self.run_right(i, j, start)
         
    def run_right(self, x: int, y: int, start: dict) -> int:
        # if border 
        if y == self.height.shape[1]:
            return 0
        # if starting point
        elif (x, y) == (start["i"], start["j"]):
            return self.run_right(x, y+1, start)
        elif self.height[x, y] >= start["h"] and y != start["j"]:
            return 1
        else:
            return 1 + self.run_right(x, y+1, start) 

        
    def scenic_score(self, i: int, j: int) -> int:
        du =  self.distance_up(i, j) 
        dd = self.distance_down(i, j) 
        dl = self.distance_left(i, j)
        dr = self.distance_right(i, j)
        return du * dd * dl * dr

    @property
    def highest_scenic_score(self) -> int:
        M = 0
        for i in range(self.height.shape[0]):
            for j in range(self.height.shape[1]):
                sc = self.scenic_score(i, j) 
                if sc > M:
                    M = sc 
        return M

            

    def get_forest(self, matrix: np.ndarray) -> np.ndarray:
        forest = np.empty(matrix.shape, dtype=Tree)
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                forest[i, j] = Tree(height = matrix[i, j])
        return forest
    
    
height = parse_input("input.txt") 
f = Forest(height=height) 
f.scan()
print(f.highest_scenic_score)
