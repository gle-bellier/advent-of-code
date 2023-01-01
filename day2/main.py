
class Shape:
    def __init__(self) -> None:
        self.value = None
        self.inf = None
        self.sup = None

    def run_fight(self, adv) -> int:
        if isinstance(adv, self.inf):
            return 6
        if isinstance(adv, self.sup):
            return 0 
        else: 
            return 3        

    def fight(self, adv)-> int:
        return self.run_fight(adv) + self.value

    
class Scissors(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.value = 3
        self.inf = Paper
        self.sup = Rock


class Paper(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.value = 2
        self.inf = Rock
        self.sup = Scissors


class Rock(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.value = 1 
        self.inf = Scissors
        self.sup = Paper


# class Round:

#     def __init__(self, adv: str, me: str) -> None:
#         self.adv = self.shape_handler(adv)
#         self.me = self.shape_handler(me)

#     def shape_handler(self, shape: str) -> Shape:
#         if shape == "A" or shape == "X":
#             return Rock()

#         elif shape == "B" or shape == "Y":
#             return Paper()
        
#         else:
#             return Scissors()

#     @property
#     def score(self) -> int:
#         return  self.me.fight(self.adv)



class Round2:

    def __init__(self, adv: str, order: str) -> None:
        self.adv = self.shape_handler(adv)
        self.me = self.select_shape(order)


    def select_shape(self, order:str) -> Shape:
        if order == "Z":
            return self.adv.sup()
        elif order == "X":
            return self.adv.inf()
        else:
            return self.adv
 

    def shape_handler(self, shape: str) -> Shape:
        if shape == "A" or shape == "X":
            return Rock()

        elif shape == "B" or shape == "Y":
            return Paper()
        
        else:
            return Scissors()

    @property
    def score(self) -> int:
        return self.me.fight(self.adv)



def get_score(filename: str) -> list[Round2]:

    lines = open(filename, "r").readlines()
    last_line = lines[-1] 
    lines = [l[:-1] for l in lines[:-1]]
    lines += [last_line] 

    score = 0
    for l in lines:
        adv, me = l.split(" ")
        score += Round2(adv, me).score

    return score


print(get_score("input.txt"))