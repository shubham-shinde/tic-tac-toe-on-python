gap = "                                            "
class Board:
    box = [" "," "," "," "," "," "," "," "," "," ",]
    def play_board(self):
        print(gap+self.box[7] + " | " + self.box[8] + " | " + self.box[9])
        print(gap+"---------")
        print(gap+self.box[4] + " | " + self.box[5] + " | " + self.box[6])
        print(gap+"---------")
        print(gap+self.box[1] + " | " + self.box[2] + " | " + self.box[3])
    def player(self, x, sign):
        if self.box[x]== " ":
           self.box[x] = sign
        else:
            print("you are not allowen to input in box "+ str(x) + "\n\n")
    def winner(self, sign):
        if self.box[7] == self.box[8] and self.box[7] == self.box[9] and self.box[7] != " ":
            print('player "'+sign+'" wins')
            agn = input("To play again (y/n)")
            if agn == "n":
                return 1
            else:
                return 0
        if self.box[4] == self.box[5] and self.box[5] == self.box[6] and self.box[6] != " ":
            print('player "'+sign+'" wins')
            agn = input("To play again (y/n)")
            if agn == "n":
                return 1
            else:
                return 0
        if self.box[1] == self.box[2] and self.box[2] == self.box[3] and self.box[3] != " ":
            print('player "'+sign+'" wins')
            agn = input("To play again (y/n)")
            if agn == "n":
                return 1
            else:
                return 0
        if self.box[7] == self.box[4] and self.box[4] == self.box[1] and self.box[4] != " ":
            print('player "'+sign+'" wins')
            agn = input("To play again (y/n)")
            if agn == "n":
                return 1
            else:
                return 0
        if self.box[5] == self.box[8] and self.box[8] == self.box[2] and self.box[2] != " ":
            print('player "'+sign+'" wins')
            agn = input("To play again (y/n)")
            if agn == "n":
                return 1
            else:
                return 0
        if self.box[3] == self.box[6] and self.box[6] == self.box[9] and self.box[6] != " ":
            print('player "'+sign+'" wins')
            agn = input("To play again (y/n)")
            if agn == "n":
                return 1
            else:
                return 0
        if self.box[7] == self.box[5] and self.box[5] == self.box[3] and self.box[3] != " ":
            print('player "'+sign+'" wins')
            agn = input("To play again (y/n)")
            if agn == "n":
                return 1
            else:
                return 0
        if self.box[5] == self.box[1] and self.box[1] == self.box[9] and self.box[1] != " ":
            print('player "'+sign+'" wins')
            agn = input("To play again (y/n)")
            if agn == "n":
                return 1
            else:
                return 0
        if self.box[1] != " " and self.box[2] != " " and self.box[3] != " " and self.box[4] != " " and self.box[5] != " " and self.box[6] != " " and self.box[7] != " " and self.box[8] != " " and self.box[9] != " ":
            print("!!!!!!!!!DRAW!!!!!!!!!!")
            agn = input("To play again (y/n)")
            if agn == "n":
                return 1
            else:
                return 0
    def clear_board(self):
        for x in range(10):
            self.box[x] = " "
def clear():
    print('\n'*50)
def new_game():
    print("welcome to tik tac toe game \n\n"+gap+" 7 | 8 | 9 \n"+gap+" -------- \n"+gap+" 4 | 5 | 6 \n"+gap+" -------- \n"+gap+" 1 | 2 | 3 ")
new_game()
while True:
    board = Board()
    move = int(input("player 'X' : take a move"+"\n"*20))
    clear()
    board.player( move, "X")
    board.play_board()
    x = board.winner("X")
    if x == 1:
        break
    elif x == 0:
        board.clear_board()
        new_game()
        continue
    move = int(input("player 'O' : take a move"+"\n"*20))
    clear()
    board.player(move, "O")
    board.play_board()
    o = board.winner("O")
    if o == 1:
        break
    elif o == 0:
        board.clear_board()
        new_game()
        continue






