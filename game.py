import pygame
import random
import sys

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOR = (0,0,0)
ENEMY_SPEED = 10

# INITIALLY DEFINE PLAYER
player_size = 50
player_pos = [SCREEN_WIDTH/2, SCREEN_HEIGHT-2*player_size]
player_x_coord = player_pos[0]
player_y_coord = player_pos[1]

# INITIALLY DEFINE ENEMY
enemy_size = 50
enemy_pos = [random.randint(0, SCREEN_WIDTH - enemy_size), 0]
enemy_x_coord = enemy_pos[0]
enemy_y_coord = enemy_pos[1]
enemy_list = [enemy_pos]

# DEFINE SCREEN
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# FUNCTIONS
def drop_enemies(enemy_list):
  if len(enemy_list) < 10:
    x_pos = random.randint(0, SCREEN_WIDTH - enemy_size)
    y_pos = 0
    enemy_list.append([x_pos, y_pos])

def draw_enemies(enemy_list):
  for enemy_pos in enemy_list:
      enemy_x_coord = enemy_pos[0]
      enemy_y_coord = enemy_pos[1]
      pygame.draw.rect(screen, BLUE, (enemy_x_coord, enemy_y_coord, enemy_size, enemy_size))

def update_enemy_positions(enemy_list):
  for idx, enemy_pos in enumerate(enemy_list):
    enemy_x_coord = enemy_pos[0]
    enemy_y_coord = enemy_pos[1]
    if enemy_y_coord >= 0 and enemy_y_coord < SCREEN_HEIGHT:
      enemy_y_coord += ENEMY_SPEED
    else:
      enemy_list.pop(idx)

def collision_check(enemy_list, player_pos):
  player_x_coord = player_pos[0]
  player_y_coord = player_pos[1]
  player_x_coord = int(player_x_coord)
  player_y_coord = int(player_y_coord)
  for enemy_pos in enemy_list:
    enemy_x_coord = enemy_pos[0]
    enemy_y_coord = enemy_pos[1]
    enemy_x_coord = int(enemy_x_coord)
    enemy_y_coord = int(enemy_y_coord)

    if detect_collision(player_x_coord, player_y_coord, enemy_x_coord, enemy_y_coord):
      return True
  return False

def detect_collision(player_x_coord, player_y_coord, enemy_x_coord, enemy_y_coord):
  player_x_coord = int(player_x_coord)
  player_y_coord = int(player_y_coord)
  enemy_x_coord = int(enemy_x_coord)
  enemy_y_coord = int(enemy_y_coord)

  player_x_space = range(player_x_coord, player_x_coord + player_size)
  player_y_space = range(player_y_coord, player_y_coord + player_size)

  enemy_x_space = range(enemy_x_coord, enemy_x_coord + enemy_size)
  enemy_y_space = range(enemy_y_coord, enemy_y_coord + enemy_size)

  player_x_set = set(player_x_space)
  enemy_x_set = set(enemy_x_space)
  x_set_result = player_x_set.intersection(enemy_x_set)

  player_y_set = set(player_y_space)
  enemy_y_set = set(enemy_y_space)
  y_set_result = player_y_set.intersection(enemy_y_set)

  if x_set_result and y_set_result != set():
    print("GAME OVER")
    return True
  else:
    print("game not over")
    return False

# GAME LOOP
game_over = False
while not game_over:
  for event in pygame.event.get():
    # print(event)
    if event.type == pygame.QUIT:
      sys.exit()

  # PLAYER BLOCK MOVEMENT
    if event.type == pygame.KEYDOWN:

      if event.key == pygame.K_LEFT:
        player_x_coord -= (player_size * .5)

      elif event.key == pygame.K_RIGHT:
        player_x_coord += (player_size * .5)

      player_pos[0] = player_x_coord

  # PAINT BACKGROUND
  screen.fill(BACKGROUND_COLOR)

  # ENEMY IMAGE DROP and DRAW
  drop_enemies(enemy_list)

  update_enemy_positions(enemy_list)

  if collision_check(enemy_list, player_pos):
    game_over = True

  draw_enemies(enemy_list)

  # PLAYER IMAGE DRAW
  pygame.draw.rect(screen, RED, (player_x_coord, player_y_coord, player_size, player_size))

  # UPDATE SCREEN
  clock.tick(30)
  pygame.display.update()