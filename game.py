
"""
This is a python implementation of a basic Tic Tac Toe game. Have fun!
Author: Israel Marinho
Contact: ilm.eletrica@gmail.com
"""

class TicTacToe():
    """Implement a Tic Tac Toe board game"""

    def __init__(self):
        self.board_temp = """
        {}  |  {}  |  {}
        --------------
        {}  |  {}  |  {}
        --------------
        {}  |  {}  |  {}
        """
        self.positions = None
        self.input_cnt = 0
        self.turn = "p1"
        self.players = dict()

    def get_user_input(self, askMsg: str) -> str:
        return input(askMsg)

    def get_user_position(self) -> int:
        """Get player's insertion choice"""
        pos = 0
        while True:
            try:
                pos = int(self.get_user_input("Enter the position (1-9, from letf to right, up to bottom) or 0 to leave: "))
                if pos not in range(0, 10):
                    print("Invalid entry. Please, try again.")
                    continue
                break
            except:
                print("Invalid entry. Please, try again.")
        return pos

    def display_board(self):
        """Print the board with current marks"""
        print(self.board_temp.format(*self.positions))

    def get_started(self):
        """Initialize game's variables"""

        self.turn = "p1"
        self.input_cnt = 0
        self.positions = [" "," ", " ", " ", " ", " ", " ", " ", " "]

        while True:
            player1 = self.get_user_input("Dou you want to be X or O: ").upper()
            if player1 == 'X':
                self.players["p1"] = 'X'
                self.players["p2"] = 'O'
                break
            elif player1 == 'O':
                self.players["p2"] = 'X'
                self.players["p1"] = 'O'
                break
            else:
                print("Invalid option. Please, try again.")

    def change_turn(self, player: str) -> str:
        """Change player turn"""

        if player == "p1":
            return "p2"
        else:
            return "p1"

    def check_win(self, pos):
        """Brute force check of the winner"""

        if self.positions[0] == self.positions[1] == self.positions[2] == self.positions[pos-1] or \
           self.positions[3] == self.positions[4] == self.positions[5] == self.positions[pos-1] or \
           self.positions[6] == self.positions[7] == self.positions[8] == self.positions[pos-1] or \
           self.positions[0] == self.positions[3] == self.positions[6] == self.positions[pos-1] or \
           self.positions[1] == self.positions[4] == self.positions[7] == self.positions[pos-1] or \
           self.positions[2] == self.positions[5] == self.positions[8] == self.positions[pos-1] or \
           self.positions[0] == self.positions[4] == self.positions[8] == self.positions[pos-1] or \
           self.positions[2] == self.positions[4] == self.positions[6] == self.positions[pos-1] :
            return True
        return False

    def check_replay(self):
        """Check if the game should cotinue"""

        option = self.get_user_input("Enter 1 to play again, anything else to leave: ")
        if int(option) == 1:
            self.get_started()
            return True
        else:
            return False

    def start_game(self):
        """Start the game"""

        self.get_started()
        while True:
            pos = self.get_user_position()
            if pos == 0:
                break
            if self.positions[pos-1] != " ":
                print("invalid position. Please, try again.")
                continue

            self.positions[pos-1] = self.players[self.turn]
            self.input_cnt += 1
            self.display_board()

            if self.check_win(pos):
                print("Congrats, you've won!")

                if self.check_replay():
                    continue
                else:
                    break
            else:
                if self.input_cnt >= 9:
                    print("Nobody won!")
                    if self.check_replay():
                        continue
                    else:
                        break

                self.turn = self.change_turn(self.turn)



if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()