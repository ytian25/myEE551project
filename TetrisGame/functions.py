from settings import *
import squares

def dock(current_block, next_block, game_area, cur_pos_x, cur_pos_y, game_over, score, speed,origionSpeed):
    '''
    The last problem is docking. When the square falls to the end or meets another square, it can't fall.
    I call this "docking" and it's convenient to have a name.
    First of all, we need to judge whether we can park. After the parking happens, we draw the non-empty dots of the current box onto the game area and make it clear.
    That is to copy the non-empty point of current_block into game_area according to the corresponding position.
    It also calculates whether a row is fully filled, and if it is fully filled, it will be eliminated.
    '''
    for _i in range(current_block.start_pos.Y, current_block.end_pos.Y + 1):
        for _j in range(current_block.start_pos.X, current_block.end_pos.X + 1):
            if current_block.template[_i][_j] != '.':
                game_area[cur_pos_y + _i][cur_pos_x + _j] = '0'
    if cur_pos_y + current_block.start_pos.Y <= 0:
        game_over = True
    else:
        # calculate the elimination
        remove_idxs = []
        for _i in range(current_block.start_pos.Y, current_block.end_pos.Y + 1):
            if all(_x == '0' for _x in game_area[cur_pos_y + _i]):
                remove_idxs.append(cur_pos_y + _i)
        if remove_idxs:
            # calculate score
            remove_count = len(remove_idxs)
            if remove_count == 1:
                score += 10
            elif remove_count == 2:
                score += 30
            elif remove_count == 3:
                score += 70
            elif remove_count == 4:
                score += 150
            speed = origionSpeed - 0.03 * (score // 10000)
            # elimanate
            _i = _j = remove_idxs[-1]
            while _i >= 0:
                while _j in remove_idxs:
                    _j -= 1
                if _j < 0:
                    game_area[_i] = ['.'] * BLOCK_WIDTH
                else:
                    game_area[_i] = game_area[_j]
                _i -= 1
                _j -= 1
        current_block = next_block
        next_block = squares.get_block()
        cur_pos_x, cur_pos_y = (BLOCK_WIDTH - current_block.end_pos.X - 1) // 2, -1 - current_block.end_pos.Y

    return current_block,next_block,cur_pos_x,cur_pos_y,game_over,score,speed,origionSpeed

def judge(position_x, position_y, block,game_area):
    '''The method of judging whether it can rotate, fall and move is also easy to realize.'''
    for _i in range(block.start_pos.Y, block.end_pos.Y + 1):
        if position_y + block.end_pos.Y >= BLOCK_HEIGHT:
            return False
        for _j in range(block.start_pos.X, block.end_pos.X + 1):
            if position_y + _i >= 0 and block.template[_i][_j] != '.' and game_area[position_y + _i][position_x + _j] != '.':
                return False
    return True