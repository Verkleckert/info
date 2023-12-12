import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up window dimensions
width, height = 800, 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
block_color = (150, 150, 150)

# Set up block dimensions
block_width_1, block_height_1 = 200, 50
block_width_2, block_height_2 = 20, 50
block_width_3, block_height_3 = 150, 50


# Create the Pygame window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Scratch Blocks Example")

class CodingBlock:
  def __init__(self, x, y, type, scalable):
    if (scalable):
      self.rect_1 = pygame.Rect(x, y, block_width_1, block_height_1)
      self.rect_2 = pygame.Rect(x, y + block_height_1, block_width_2, block_height_2)
      self.rect_3 = pygame.Rect(x, y + block_height_1 + block_height_2, block_width_3, block_height_3)
    else:
      self.rect_1 = pygame.Rect(x, y, block_width_1, block_height_1)
    self.title = type
    self.dragging = False
    self.snapped_children = []
    self.scalable = scalable

  def draw(self):
    if (self.scalable):
      pygame.draw.rect(screen, block_color, self.rect_1)
      pygame.draw.rect(screen, block_color, self.rect_2)
      pygame.draw.rect(screen, block_color, self.rect_3)
      font = pygame.font.Font(None, 36)
      text = font.render(self.title, True, black)
      screen.blit(text, (self.rect_1.x + 10, self.rect_1.y + 10))
    else:
      pygame.draw.rect(screen, block_color, self.rect_1)
      font = pygame.font.Font(None, 36)
      text = font.render(self.title, True, black)
      screen.blit(text, (self.rect_1.x + 10, self.rect_1.y + 10))


blocks = [CodingBlock(50, 50, "test", False),
          CodingBlock(50, 150, "jmp", False),
          CodingBlock(50, 250, "inc", False),
          CodingBlock(50, 350, "dec", False),
          CodingBlock(350, 50, "dec", True)
          ]

def get_distance(block1, block2) -> int:
  distance_x = abs(block1.rect_1.left - block2.rect_1.left)
  distance_y = abs(block1.rect_1.top - block2.rect_1.top)
  distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
  return int(distance)

def snap_blocks(block1, block2):
  # block1 draggable true, block 2 nearest
  if (abs(block1.rect_1.left - block2.rect_1.left) < 15 and
      abs(block1.rect_1.top - block2.rect_1.bottom) < 15):
    block1.rect_1.left = block2.rect_1.left
    block1.rect_1.top = block2.rect_1.bottom


# Main game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      for block in blocks:
        if block.rect_1.collidepoint(event.pos):
          block.dragging = True
          offset_x, offset_y = block.rect_1.x - event.pos[0], block.rect_1.y - event.pos[1]
    elif event.type == pygame.MOUSEBUTTONUP:
      for block in blocks:
        block.dragging = False

    screen.fill(white)

    for block in blocks:
      if block.dragging:
        if block.scalable:
          block.rect_1.x, block.rect_1.y = event.pos[0] + offset_x, event.pos[1] + offset_y
          block.rect_2.x, block.rect_2.y = event.pos[0] + offset_x, event.pos[1] + offset_y
          block.rect_3.x, block.rect_3.y = event.pos[0] + offset_x, event.pos[1] + offset_y
        else:
          block.rect.x, block.rect.y = event.pos[0] + offset_x, event.pos[1] + offset_y
        nearest_block = []
        
        # Get nearestblock to the currentlyy clicked
        for block_index in range(0, len(blocks)):
          dist = get_distance(block, blocks[block_index])
          if (len(nearest_block) == 0 or dist < nearest_block[1]) and block != blocks[block_index]:
            nearest_block = [block_index, dist]
            print(nearest_block)
        
        snap_blocks(block, blocks[nearest_block[0]])
        print(f"{nearest_block} | {block.rect_1}")
        
      block.draw()

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
