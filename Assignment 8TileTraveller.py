

N = "(N)orth"
E = "(E)ast"
S = "(S)outh"
W = "(W)est"

move = ""
x_start = 1
y_start = 1
####
print("halló")

def action(x):
    if x.upper() == "N":
        return x_start, y_start+1
    elif x.upper() == "E":
        return x_start+1, y_start
    elif x.upper() == "S":
        return x_start, y_start-1
    elif x.upper() == "W":
        return x_start-1, y_start


#while (x_start != 4 or x_start != 0) and (y_start != 4 or y_start != 0):
while True:

    if x_start == 1 and y_start == 1:
        print(f"You can travel: {N}.")
        print(x_start)
        print(y_start)
    elif x_start == 1 and y_start == 2:
        print(f"You can travel: {N} or {E} or {S}.")
        print(x_start)
        print(y_start)
    elif x_start == 1 and y_start == 3:
        print(f"You can travel: {E} or {S}.")
    elif x_start == 2 and y_start == 1:
        print(f"You can travel: {N}.")
    elif x_start == 2 and y_start == 2:
        print(f"You can travel: {W} or {S}.")
    elif x_start == 2 and y_start == 3:
        print(f"You can travel: {W} or {E}.")
    elif x_start == 3 and y_start == 3:
        print(f"You can travel: {W} or {S}.")
    elif x_start == 3 and y_start == 2:
        print(f"You can travel: {N} or {S}.")
    elif x_start == 3 and y_start == 1:
        print("Victory")
        break

    move = str(input("Direction: "))
    action(move)

    print(x_start)
    print(y_start)


    