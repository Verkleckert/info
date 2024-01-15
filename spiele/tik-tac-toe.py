import sys

class Game(object):
    def __init__(self) -> None:
        self.game: list[str | None, ...] = [None for _ in range(9)]
        self.current_player = "X"

    def place_at(self, index: int, string: str) -> bool:
        try:
            if self.game[index] is None:
                self.game[index] = string
                return True
            else:
                print(f"This cell is already occupied by {self.game[index]} you dumbass {string}", file=sys.stdout)
                return False
        except IndexError:
            print("Index out of range.", file=sys.stderr)

    def place_x_at(self, index: int):
        return self.place_at(index, "X")

    def place_o_at(self, index: int):
        return self.place_at(index, "O")

    def detect_win(self) -> str | None:
        # Columns
        for i in range(3):
            if (self.game[i] == self.game[i + 3] == self.game[i + 6]) and self.game[i] != None:
                return self.game[i]

        # Rows
        for i in range(3):
            if (self.game[i*3] == self.game[i*3 + 1] == self.game[i*3 + 2]) and self.game[i*3] != None:
                return self.game[i]

        # Diagonals
        if (self.game[0] == self.game[4] == self.game[8]) and self.game[0] != None:
            return self.game[0]
        if (self.game[2] == self.game[4] == self.game[6]) and self.game[2] != None:
            return self.game[2]

    def get_current_player(self) -> str:
        return self.current_player

    def get_game_state(self) -> list[str | None, ...]:
        return self.game
    
    def print_game(self):
        state = ['/' if element is None else element for element in game.get_game_state()]
        
        print("┌───┬───┬───┐")
        print(f"│ {state[0]} │ {state[1]} │ {state[2]} │")
        print("├───┼───┼───┤")
        print(f"│ {state[3]} │ {state[4]} │ {state[5]} │")
        print("├───┼───┼───┤")
        print(f"│ {state[6]} │ {state[7]} │ {state[8]} │")
        print("└───┴───┴───┘")
    
    def change_player(self):
        if (self.current_player == "X" ):
            self.current_player = "O"
        elif (self.current_player == "O" ):
            self.current_player = "X"
    
    def run(self):
        while( not self.detect_win()):
            self.print_game()
            if (self.current_player == "X" ):
                input_ = int(input("Player X: ")) - 1
                while not self.place_x_at(input_):
                    input_ = int(input("Player X: ")) - 1

            if (self.current_player == "O" ):
                input_ = int(input("Player O: ")) - 1
                while not self.place_o_at(input_):
                    input_ = int(input("Player O: ")) - 1
            self.change_player()
        self.print_game()
        print(f"{game.detect_win()} wins.")


if __name__ == "__main__":
    # 1 2 3
    # 4 5 6
    # 7 8 9
    game = Game()
    game.run()