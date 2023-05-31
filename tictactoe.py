import random 


class board: 
    start_board = {x: x for x in range(1, 10)}
    previous_board = {}
    current_board = {x: f"[ {x} ]" for x in range(1, 10)}
    open_locations = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def check_for_winner(self, color, player):
        winning_combos = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 5, 9],
            [3, 5, 7]
        ]
        for x in winning_combos:
            a, b, c = x
# unpacking^^^
            if self.current_board[a] == color and self.current_board[b] == color and self.current_board[c] == color:
                print(f"*{player.upper()} IS THE WINNER!!!*")
                print("Thanks for playing tic-tac-Buffalo-buffalo")
                print(f"You won the game in {9-len(self.open_locations)} moves")
                print()
                return True
        return False

    def view_board(self):
        print()
        print(self.current_board[1], self.current_board[2], self.current_board[3])
        print(self.current_board[4], self.current_board[5], self.current_board[6])
        print(self.current_board[7], self.current_board[8], self.current_board[9])
        print()

    def update_board(self, color):
        self.previous_board = self.current_board.copy()
        try:
            x = input(f"{color.capitalize()}, which square do you want to play? ")
            x = int(x)
        except Exception:
            print(f"{x} is not a valid number of a spot. Try again")
            return self.update_board(color)
        if x in self.open_locations:
            self.current_board[x] = color
            self.open_locations.remove(x)
        else:
            print(f"{x} is not an available spot, try again")
            return self.update_board(color)
        self.view_board()

    def undo(self):    
        self.current_board = self.previous_board

    def play_game(self):
        player_one = input("Player One - what is your name? \n")
        player_two = input("Player Two - what is your name? \n")
        players = [player_one, player_two]
        random.shuffle(players)
        print(f"\nOkay. We have {player_one} vs {player_two}! Let's begin.")
        white, black = players
        #unpacking ^^^
        print(f"{white} has been randomly selected to go first. {white} will use white")
        while True:
            self.update_board("white")
            if (self.check_for_winner("white", white)):
                break 
            self.update_board("black")
            if (self.check_for_winner("black", black)):
                break


new_game = board()
new_game.play_game()


#whose turn is it
#randomize who starts
#ask for input
#validation can oinly choose 1-9, no repeats
#label boxes 1-9
#how many moves it takes**
#choose own color/name
#cant overwrite a move
#undo a move
#print when there is a winner
# printing - abstract the board
    #def undo():

#building a random spot selector from random in open_spots
#play againsyt computer