print("WELCOME TO TIC-TAC-TOE")

c_player = "X"


board = ["1","2","3",
        "4","5","6",
        "7","8","9"
        ]


def display_b():
        print(board[0]+"|"+board[1]+"|"+board[2])
        print(board[3]+"|"+board[4]+"|"+board[5])
        print(board[6]+"|"+board[7]+"|"+board[8])


def current_player():
    global c_player
    if c_player == "X":
        c_player = "O"
        return c_player
    else:
        c_player = "X"
        return c_player


display_b()


def row_win():
    if board[0]==board[1]==board[2]:
        print("ROW 1 MATCHED")
        print("PLAYER "+cp+" WON")
        return 1
    if board[3]==board[4]==board[5]:
        print("ROW 2 MATCHED")
        print("PLAYER "+cp+" WON")
        return 1
    if board[6]==board[7]==board[8]:
        print("ROW 3 MATCHED")
        print("PLAYER "+cp+" WON")
        return 1




def col_win():
    if board[0]==board[3]==board[6]:
        print("COL 1 MATCHED")
        print("PLAYER "+cp+" WON")
        return 1
    if board[1]==board[4]==board[7]:
        print("COL 2 MATCHED")
        print("PLAYER "+cp+" WON")
        return 1
    if board[2]==board[5]==board[8]:
        print("COL 3 MATCHED")
        print("PLAYER "+cp+" WON")
        return 1


def diagonal_win():
    if board[2]==board[4]==board[6]:
        print("DIAGONAL 1 MATCHED")
        print("PLAYER "+cp+" WON")
        return 1
    if board[0]==board[4]==board[8]:
        print("ROW 2 MATCHED")
        print("PLAYER "+cp+" WON")
        return 1


while(True):
    print("\n")
    cp =current_player()
    print("Current Player",cp)
    print("CHOOSE A PLACE FROM 1-9")
    usr_input = int(input(">>  "))
    board[usr_input-1] = cp
    display_b()
    if col_win() == 1:
        display_b()
        break
    elif row_win() == 1:
        display_b()
        break
    elif diagonal_win() == 1:
        display_b()
        break






       