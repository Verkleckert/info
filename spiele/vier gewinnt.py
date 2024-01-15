class Game:
  def __init__(self):
    self.game: list[list[str | None, ...], ...] = [[None for _ in range(6)] for _ in range(7)]
    self.running = True
    self.currentUser = 0
    
  def run(self):
    while(self.running):
      self.printGame()
      input = int(input("Geben sie den Index von 1 - 7 an: ")) -1
      self.move(input)
      self.currentUser = not self.currentUser

  def move(self, index: int):
    pass
  
  def printGame(self):
    print("\n\n\n\n\n\n\n\n\n")
    transposed_array = list(zip(*self.game))
    for row in transposed_array:
      print(row)

game = Game()
game.run()