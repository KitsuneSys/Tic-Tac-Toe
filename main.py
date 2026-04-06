import random
import time


board = [[1,2 ,3],
         [4,'X',6],
         [7,8,9]]


def display_board(board):

    line1 = "+-------+-------+-------+"
    line2 = "|       |       |       |"

    for row in board:
        print(line1)
        print(line2)
        print("|   " + "   |   ".join(str(c) for c in row) + "   |")
        print(line2)
    print(line1)


def enter_move(board):
    while True:

        try:
            time.sleep(1)
            u = int(input("\nPlace your move, human: "))
            time.sleep(1)
            print("\nYou chose: ", u)
            

            if u<=0 or u>=10:
                time.sleep(1)
                print("\nYou must enter a number between 1 and 9")
                time.sleep(1)
                print("\nTry again. \n")
                continue


            pos = u - 1
            fila = pos // 3
            colum = pos % 3

            if board[fila][colum] == "O" or board[fila][colum] == "X":
                 time.sleep(1)
                 print("\nCurrent value: ",board[fila][colum])
                 time.sleep(1)
                 print("\nYou must choose an empty square")
                 time.sleep(1)
                 print("\nTry again")
                 time.sleep(1)
                 continue

            else:
                time.sleep(1)
                print("\nPosition: ", "[" ,fila, "]", "[" ,colum, "]")
                board[fila][colum] = "O"
                time.sleep(1)
                print("\nMove placed: ", board[fila][colum])
                time.sleep(1)
                break
    
        except ValueError:
            print("\nOnly integer numbers are allowed.")
            continue
    
        except:
            print("\nSomething went wrong, try again.")
            continue
    
    display_board(board)


def make_list_of_free_fields(board):

    free = []

    for i in range(3):
        for j in range(3):
            if type(board[i][j]) == int:
                free.append((i,j))
    

    return free


def victory_for(board, sign):

    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True

    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    
    elif board[2][0] == sign and board[1][1] == sign and board[0][2] == sign:
        return True

    else:
        return False


def draw_move(board):

    free_fields = make_list_of_free_fields(board)

    m = random.randrange(len(free_fields))

    i, j = free_fields[m]

    board[i][j] = "X"


def loading_points():
        
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        print("\n")


def ai_thinking():
        
        print("\nThinking", end="", flush=True)
    
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(1)
        print("\n")


def play_game(board):

    print("\nWelcome to Tic Tac Toe\n")
    time.sleep(1)
    print("Drawing board")
    loading_points()
    print("\n")

    while True:
        
        display_board(board)
        loading_points()

        print("\nHuman turn: ")
        enter_move(board)

        if victory_for(board, "O"):
            loading_points()
            display_board(board)
            print("\nYou win")
            break

        print("\nEvil AI turn: ")
        ai_thinking()
        
        draw_move(board)

        if victory_for(board, "X"):
            loading_points()
            display_board(board)
            print("\nYou lose")
            break

        if make_list_of_free_fields(board) == []:
            loading_points()
            print("\nIt's a draw")
            break

    print("\nThank you for playing\n")


play_game(board)
