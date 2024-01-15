import sys

game: list = [None, None, None, None, None, None, None, None, None]
current_player = "X"

def place_at(index: int, string: str) -> bool:
  try:
    if game[index] is None:
      game[index] = string
      return True
    else:
      print(f"This cell is already occupied by {game[index]} you dumbass {string}", file=sys.stdout)
      return False
  except IndexError:
    print("Index out of range.", file=sys.stderr)

def place_x_at(index: int):
  return place_at(index, "X")

def place_o_at(index: int):
  return place_at(index, "O")

def detect_win() -> str | None:
  # Columns
  for i in range(3):
    if (game[i] == game[i + 3] == game[i + 6]) and game[i] != None:
      return game[i]

  # Rows
  for i in range(3):
    if (game[i*3] == game[i*3 + 1] == game[i*3 + 2]) and game[i*3] != None:
      return game[i]

  # Diagonals
  if (game[0] == game[4] == game[8]) and game[0] != None:
    return game[0]
  if (game[2] == game[4] == game[6]) and game[2] != None:
    return game[2]

def get_current_player() -> str:
  return current_player

def get_game_state() -> list[str | None]:
  return game
  
def print_game():
  state = ['/' if element is None else element for element in get_game_state()]
  
  print("┌───┬───┬───┐")
  print(f"│ {state[0]} │ {state[1]} │ {state[2]} │")
  print("├───┼───┼───┤")
  print(f"│ {state[3]} │ {state[4]} │ {state[5]} │")
  print("├───┼───┼───┤")
  print(f"│ {state[6]} │ {state[7]} │ {state[8]} │")
  print("└───┴───┴───┘")
  
def change_player():
  if (current_player == "X" ):
    current_player = "O"
  elif (current_player == "O" ):
    current_player = "X"
  
def run():
  while( not detect_win()):
    print_game()
    if (current_player == "X" ):
      input_ = int(input("Player X: ")) - 1
      while not place_x_at(input_):
        input_ = int(input("Player X: ")) - 1

    if (current_player == "O" ):
      input_ = int(input("Player O: ")) - 1
      while not place_o_at(input_):
        input_ = int(input("Player O: ")) - 1
    change_player()
  print_game()
  print(f"{game.detect_win()} wins.")


if __name__ == "__main__":
  # 1 2 3
  # 4 5 6
  # 7 8 9
  run()