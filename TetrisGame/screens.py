import pygame
import time
from settings import *
from functions import judge,dock

def print_screen_text(screen, font, x, y, text, fcolor=(255, 255, 255)):
    imgText = font.render(text, True, fcolor)
    screen.blit(imgText, (x, y))

def display_screen(screen,pause,start,font1,font2,font_pos_x,font1_height,gameover_size,game_area,game_over,cur_pos_x,cur_pos_y,last_drop_time,current_block,next_block,block_color,speed,origionSpeed,score):
    # Fill in background color
    screen.fill(BG_COLOR)
    # Draw game area divide lines
    pygame.draw.line(screen, BORDER_COLOR,
                     (SIZE * BLOCK_WIDTH + BORDER_WIDTH // 2, 0),
                     (SIZE * BLOCK_WIDTH + BORDER_WIDTH // 2, SCREEN_HEIGHT), BORDER_WIDTH)

    # Draw existing squares
    if game_area:
        for i, row in enumerate(game_area):
            for j, cell in enumerate(row):
                if cell != '.':
                    pygame.draw.rect(screen, block_color, (j * SIZE, i * SIZE, SIZE, SIZE), 0)

    # Draw grid lines (vertical lines
    for x in range(BLOCK_WIDTH):
        pygame.draw.line(screen, BLACK, (x * SIZE, 0), (x * SIZE, SCREEN_HEIGHT), 1)
    # Draw grid lines (horizontal lines
    for y in range(BLOCK_HEIGHT):
        pygame.draw.line(screen, BLACK, (0, y * SIZE), (BLOCK_WIDTH * SIZE, y * SIZE), 1)

    if not game_over:
        cur_drop_time = time.time()
        if cur_drop_time - last_drop_time > speed:
            if not pause:
                # We shouldn't judge whether it's falling to the end or not. When we play Tetris, the moment the Tetris fall to the end can move left and right.
                if not judge(cur_pos_x, cur_pos_y + 1, current_block, game_area):
                    current_block, next_block, cur_pos_x, cur_pos_y, game_over, score,speed,origionSpeed = dock(current_block, next_block,
                                                                                             game_area, cur_pos_x,
                                                                                             cur_pos_y, game_over,
                                                                                             score, speed, origionSpeed)
                else:
                    last_drop_time = cur_drop_time
                    cur_pos_y += 1
    else:
        if start:
            print_screen_text(screen, font2,
                              (SCREEN_WIDTH - gameover_size[0]) // 2, (SCREEN_HEIGHT - gameover_size[1]) // 2,
                              'GAME OVER', RED)

    # draw the crrent falling cube
    if current_block:
        for i in range(current_block.start_pos.Y, current_block.end_pos.Y + 1):
            for j in range(current_block.start_pos.X, current_block.end_pos.X + 1):
                if current_block.template[i][j] != '.':
                    pygame.draw.rect(screen, block_color,
                                     ((cur_pos_x + j) * SIZE, (cur_pos_y + i) * SIZE, SIZE, SIZE), 0)

    print_screen_text(screen, font1, font_pos_x, 10, f'Scores: ')
    print_screen_text(screen, font1, font_pos_x, 10 + font1_height + 6, f'{score}')
    print_screen_text(screen, font1, font_pos_x, 20 + (font1_height + 6) * 2, f'speed: ')
    print_screen_text(screen, font1, font_pos_x, 20 + (font1_height + 6) * 3, f'{score // 1000}')
    print_screen_text(screen, font1, font_pos_x, 30 + (font1_height + 6) * 4, f'Next：')

    if next_block:
        _h = 30 + (font1_height + 6) * 5
        for i in range(next_block.start_pos.Y, next_block.end_pos.Y + 1):
            for j in range(next_block.start_pos.X, next_block.end_pos.X + 1):
                if next_block.template[i][j] != '.':
                    pygame.draw.rect(screen, block_color, (font_pos_x + j * SIZE, _h + i * SIZE, SIZE, SIZE), 0)

    pygame.display.flip()  # Display update