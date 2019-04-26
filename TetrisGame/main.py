#-*- coding:utf-8 -*-
'''
game instruction：
enter: game start
pause: game stop
↑：rotate
other direction buttons：change the location
'''
import sys
import time
import pygame
from pygame.locals import *
import squares
from settings import *
from screens import display_screen
from functions import judge
from events import set_x_y_left_right_down_up

def main():
    pygame.init()          #Initialization of hardware devices
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    #Set window size
    pygame.display.set_caption('Teris Game')

    font1 = pygame.font.SysFont('SimHei', 24)  # set characters, Font boldface 24
    font2 = pygame.font.Font(None, 72)  # GAME OVER's characters
    font_pos_x = BLOCK_WIDTH * SIZE + BORDER_WIDTH + 10  #The X coordinates of the font position in the right information display area
    gameover_size = font2.size('GAME OVER')
    font1_height = int(font1.size('Scores')[1])

    current_block = None   # current dropping cube
    next_block = None  # next cube
    block_color = (200, 200, 200)  #cube's colour
    cur_pos_x, cur_pos_y = 0, 0   #current cube's location

    game_area = None    # whole game area
    game_over = True    #end judgement
    start = False       # Whether to start, GAME OVER is displayed when start = True, game_over = True
    score = 0           # get score
    origionSpeed = 0.5      # original speed
    speed = origionSpeed    # current speed
    pause = False          # pause
    last_drop_time = None   # Last landing time
    last_press_time = None  # Last key time

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:   #quit
                sys.exit()
            elif event.type == KEYDOWN:   #down
                if event.key == K_RETURN:  #enter start the game
                    if game_over:
                        start = True
                        game_over = False
                        score = 0
                        last_drop_time = time.time()
                        last_press_time = time.time()
                        game_area = [['.'] * BLOCK_WIDTH for _ in range(BLOCK_HEIGHT)]
                        current_block = squares.get_block()
                        next_block = squares.get_block()
                        cur_pos_x, cur_pos_y = (BLOCK_WIDTH - current_block.end_pos.X - 1) // 2, -1 - current_block.end_pos.Y
                elif event.key == K_SPACE:   #pause the game
                    if not game_over:
                        pause = not pause
                elif event.key in (K_w, K_UP):
                    # rotate
                    # Whether this can be rotated on the right side or not, I tried the Russian square on the internet, it can't rotate, here we can't rotate.
                    # We do a lot of blanks in shape design, so we only need to specify that the whole shape, including the blank part, can rotate in the game area.
                    if 0 <= cur_pos_x <= BLOCK_WIDTH - len(current_block.template[0]):
                        _next_block = squares.get_next_block(current_block)
                        if judge(cur_pos_x, cur_pos_y, _next_block,game_area):
                            current_block = _next_block

        #Up, down, left and right update functions
        game_over, pause, last_press_time, last_drop_time, \
        cur_pos_x, cur_pos_y, current_block, game_area, next_block,\
        score, speed, origionSpeed = set_x_y_left_right_down_up(event, game_over, pause,
                    last_press_time, last_drop_time, cur_pos_x, cur_pos_y,
                    current_block, game_area, BLOCK_WIDTH, next_block, score, speed, origionSpeed)

        #Display screen function
        display_screen(screen, pause, start, font1, font2, font_pos_x, font1_height, gameover_size, game_area,
                       game_over, cur_pos_x, cur_pos_y, last_drop_time, current_block, next_block, block_color, speed,origionSpeed,score)


if __name__ == '__main__':
    main()