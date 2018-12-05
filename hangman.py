import random

def hangman():
    wlist = ["dog","snake","bird","car","house","guitar"]
    random_num = random.randint(0,5)
    word = wlist[random_num]
    wrong = 0
    stages =["",
             "_________          ",
             "|                  ",
             "|        |         ",
             "|        0         ",
             "|       /|\        ",
             "|       / \        ",
             "|                  ",
             ]
    rletters = list(word)
    board =["_"] * len(word)
    win = False
    print("ハングマンへようこそ!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予測してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け!正解は　{}.".format(word))

hangman()
