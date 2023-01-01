

lines = open("input.txt", "r").readlines()
lines[-1] = lines[-1] + "\n"


# max_cal = 0
# current = 0
# for line in lines:


#     if line == "\n":

#         if current > max_cal:
#             max_cal = current
        
#         current = 0
    
#     else:
#         current += int(line[:-1])


# print(max_cal)



elves_cal = []
current = 0
for line in lines:

    if line == "\n":
        elves_cal += [current]
        current = 0

    else:
        current += int(line[:-1])


total = sum(sorted(elves_cal)[-3:])
print(total)

print("Hello this is a quick test")



