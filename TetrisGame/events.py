import time
import pygame
from functions import dock,judge

def set_x_y_left_right_down_up(event,game_over,pause,last_press_time,last_drop_time,cur_pos_x,cur_pos_y,
                               current_block,game_area,BLOCK_WIDTH
                               ,next_block,score, speed, origionSpeed):
    '''
    function：for down, left, right three movement
    :param event: event down ,left, right
    :param game_over: End sign
    :param pause: pause
    :param last_press_time: last key time
    :param last_drop_time: last drop time
    :param cur_pos_x: X position of the current block
    :param cur_pos_y: Y position of current block
    :param current_block: current cube
    :param game_area: game area
    :param BLOCK_WIDTH: width of the cube
    :param next_block: next block
    :param score: score
    :param speed: speed
    :param orispeed: priginal speed
    :return:
    '''
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if not game_over and not pause:
                if time.time() - last_press_time > 0.1:
                    last_press_time = time.time()
                    if cur_pos_x > - current_block.start_pos.X:
                        if judge(cur_pos_x - 1, cur_pos_y, current_block, game_area):
                            cur_pos_x -= 1
        if event.key == pygame.K_RIGHT:
            if not game_over and not pause:
                if time.time() - last_press_time > 0.1:
                    last_press_time = time.time()
                    # Can't remove the right border
                    if cur_pos_x + current_block.end_pos.X + 1 < BLOCK_WIDTH:
                        if judge(cur_pos_x + 1, cur_pos_y, current_block, game_area):
                            cur_pos_x += 1
        if event.key == pygame.K_DOWN:
            if not game_over and not pause:
                if time.time() - last_press_time > 0.1:
                    last_press_time = time.time()
                    if not judge(cur_pos_x, cur_pos_y + 1, current_block, game_area):
                        current_block, next_block, cur_pos_x, cur_pos_y,game_over,score,speed,origionSpeed = dock(current_block, next_block, game_area, cur_pos_x,
                                                                           cur_pos_y, game_over, score, speed, origionSpeed)
                    else:
                        last_drop_time = time.time()
                        cur_pos_y += 1

    return game_over,pause,last_press_time,last_drop_time,cur_pos_x,cur_pos_y,current_block,game_area,next_block,score, speed, origionSpeed