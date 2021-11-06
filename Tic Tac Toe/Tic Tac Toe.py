print("1 2 3")
print("4 5 6")
print("7 8 9")
lmain = [" "," "," "," "," "," "," "," "," "]
def input_manipulation(le):
    pos = int(input("where to mark:"))
    if pos == 1:
        if le[0] == " ":
            le[0] = "O"
    elif pos == 2:
        if le[1] == " ":
            le[1] = "O"
    elif pos == 3:
        if le[2] == " ":
            le[2] = "O"
    elif pos == 4:
        if le[3] == " ":
            le[3] = "O"
    elif pos == 5:
        if le[4] == " ":
            le[4] = "O"
    elif pos == 6:
        if le[5] == " ":
            le[5] = "O"
    elif pos == 7:
        if le[6] == " ":
            le[6] = "O"
    elif pos == 8:
        if le[7] == " ":
            le[7] = "O"
    elif pos == 9:
        if le[8] == " ":
            le[8] = "O"
    else:
        print("Wrong position")
        return False
    return le
from random import randint
def comp_play(li):
    r = randint(0,8)
    if li[r] == " ":
        li[r] = "X"
        return li
    else:
        return False
def decision(lf):
    if (lf[0] == "O") and (lf[4] == "O") and (lf[8] == "O"):
        print("You win")
    elif (lf[0] == "O") and (lf[3] == "O") and (lf[6] == "O"):
        print("You win")
    elif (lf[0] == "O") and (lf[1] == "O") and (lf[2] == "O"):
        print("You win")
    elif (lf[2] == "O") and (lf[4] == "O") and (lf[6] == "O"):
        print("You win")
    elif (lf[0] == "O") and (lf[3] == "O") and (lf[6] == "O"):
        print("You win")
    elif (lf[2] == "O") and (lf[5] == "O") and (lf[8] == "O"):
        print("You win")
    elif (lf[1] == "O") and (lf[4] == "O") and (lf[7] == "O"):
        print("You win")
    elif (lf[3] == "O") and (lf[4] == "O") and (lf[5] == "O"):
        print("You win")
    elif (lf[6] == "O") and (lf[7] == "O") and (lf[8] == "O"):
        print("You win")
    elif (lf[0] == "X") and (lf[4] == "X") and (lf[8] == "X"):
        print("You lose")
    elif (lf[0] == "X") and (lf[3] == "X") and (lf[6] == "X"):
        print("You lose")
    elif (lf[0] == "X") and (lf[1] == "X") and (lf[2] == "X"):
        print("You lose")
    elif (lf[2] == "X") and (lf[4] == "X") and (lf[6] == "X"):
        print("You lose")
    elif (lf[0] == "X") and (lf[3] == "X") and (lf[6] == "X"):
        print("You lose")
    elif (lf[2] == "X") and (lf[5] == "X") and (lf[8] == "X"):
        print("You lose")
    elif (lf[1] == "X") and (lf[4] == "X") and (lf[7] == "X"):
        print("You lose")
    elif (lf[3] == "X") and (lf[4] == "X") and (lf[5] == "X"):
        print("You lose")
    elif (lf[6] == "X") and (lf[7] == "X") and (lf[8] == "X"):
        print("You lose")
    else:
        return False
    return True
end = False
while end == False:
    l4 = False
    while l4 == False:
        l4 = input_manipulation(lmain)
    lmain = l4
    l5 = False
    while l5 == False:
        l5 = comp_play(lmain)
    lmain = l5
    print(lmain[0:3])
    print(lmain[3:6])
    print(lmain[6:])
    end = decision(lmain)