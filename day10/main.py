

def parse_input(filename: str) -> list[str]:
    lines = open(filename, "r").readlines()
    lines = [l[:-1] for l in lines]
    return lines
    




def run(commands: list[str], indexes: list[int]) -> int:

    cursor = 1
    buffer = [cursor]
    for c in commands:
        elts = c.split(" ")
        if len(elts) == 1:
            buffer.append(cursor)
        else:
            cursor += int(elts[1])
            buffer += [cursor, cursor]

    s = 0
    for i in indexes:
        product = (i+1) * buffer[i]
        print(f"Time {i} -> {buffer[i]}, product = {product}")
        s += product

    return s

def question2(commands: list[str]) -> str:

    cursor = 1
    buffer = [cursor]
    for c in commands:
        elts = c.split(" ")
        if len(elts) == 1:
            buffer.append(cursor)
        else:
            cursor += int(elts[1])
            buffer += [cursor, cursor]

    s = ""
    for x in range(len(buffer)):
        print(f"CTR {x%40}, buffer {buffer[x]-1}-{buffer[x]+1}.") 
        if x % 40 == 0:
            s+="\n"
            
        if x%40 >= buffer[x]-1 and x%40 <= buffer[x]+1:
            s+="#"
            print("Mark")
        else:
            s+="."

    return s


commands = parse_input("example.txt")
s = question2(commands)
print(s)
        
            
