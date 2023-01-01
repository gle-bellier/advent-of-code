

def parse_input(filename: str) -> list:
    return open(filename, "r").readlines()


def parse_pair(line: str) -> list[list[int]]:

    e1, e2 = line.split(",")
    s1, e1 = e1.split("-")
    s2, e2 = e2.split("-")
    return [[int(s1), int(e1)], [int(s2), int(e2)]] 
    
# def check(range1: list[int], range2: list[int])-> int:


#     start1, end1 = range1
#     start2, end2 = range2
#     if int(start1) <= int(start2) and int(end1) >= int(end2):
#         return 1
#    elif int(start2) <= int(start1) and int(end2) >= int(end1):
#         return 1

#     else:
#         return 0
    

def check_overlap(range1: list[int], range2: list[int])-> int:
    start1, end1 = range1
    start2, end2 = range2

    if end1 < start2:
        return 0
    elif end2 < start1:
        return 0
    else:
        return 1


    # if end1 >= start2 and end1<=end2:
    #     return 1  
    # elif end2 >= start1 and end2<=end1:
    #     return 1  
    # else:
    #     return 0

    








    
lines = parse_input("input.txt")
last_line = lines[-1]
lines = [l[:-1] for l in lines[:-1]]
lines += [last_line]
pairs = [parse_pair(l) for l in lines]

