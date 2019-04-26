import random
from collections import namedtuple

Point = namedtuple('Point', 'X Y')      #Named tuple ,named Point coordinate position X Y
Shape = namedtuple('Shape', 'X Y Width Height')
Block = namedtuple('Block', 'template start_pos end_pos name next')

# Up and down, left and right, is actually replacing one figure with another.
# In fact, to achieve this function, you just need to fix the coordinates of the upper left corner.

# S cube
S_BLOCK = [Block(['.OO',
                  'OO.',
                  '...'], Point(0, 0), Point(2, 1), 'S', 1),
           Block(['O..',
                  'OO.',
                  '.O.'], Point(0, 0), Point(1, 2), 'S', 0)]
# z cube
Z_BLOCK = [Block(['OO.',
                  '.OO',
                  '...'], Point(0, 0), Point(2, 1), 'Z', 1),
           Block(['.O.',
                  'OO.',
                  'O..'], Point(0, 0), Point(1, 2), 'Z', 0)]
# I cube
I_BLOCK = [Block(['.O..',
                  '.O..',
                  '.O..',
                  '.O..'], Point(1, 0), Point(1, 3), 'I', 1),
           Block(['....',
                  '....',
                  'OOOO',
                  '....'], Point(0, 2), Point(3, 2), 'I', 0)]
# O cube
O_BLOCK = [Block(['OO',
                  'OO'], Point(0, 0), Point(1, 1), 'O', 0)]
# J cube
J_BLOCK = [Block(['O..',
                  'OOO',
                  '...'], Point(0, 0), Point(2, 1), 'J', 1),
           Block(['.OO',
                  '.O.',
                  '.O.'], Point(1, 0), Point(2, 2), 'J', 2),
           Block(['...',
                  'OOO',
                  '..O'], Point(0, 1), Point(2, 2), 'J', 3),
           Block(['.O.',
                  '.O.',
                  'OO.'], Point(0, 0), Point(1, 2), 'J', 0)]
# L cube
L_BLOCK = [Block(['..O',
                  'OOO',
                  '...'], Point(0, 0), Point(2, 1), 'L', 1),
           Block(['.O.',
                  '.O.',
                  '.OO'], Point(1, 0), Point(2, 2), 'L', 2),
           Block(['...',
                  'OOO',
                  'O..'], Point(0, 1), Point(2, 2), 'L', 3),
           Block(['OO.',
                  '.O.',
                  '.O.'], Point(0, 0), Point(1, 2), 'L', 0)]
# T cube
T_BLOCK = [Block(['.O.',
                  'OOO',
                  '...'], Point(0, 0), Point(2, 1), 'T', 1),
           Block(['.O.',
                  '.OO',
                  '.O.'], Point(1, 0), Point(2, 2), 'T', 2),
           Block(['...',
                  'OOO',
                  '.O.'], Point(0, 1), Point(2, 2), 'T', 3),
           Block(['.O.',
                  'OO.',
                  '.O.'], Point(0, 0), Point(1, 2), 'T', 0)]

BLOCKS = {'O': O_BLOCK,
          'I': I_BLOCK,
          'Z': Z_BLOCK,
          'T': T_BLOCK,
          'L': L_BLOCK,
          'S': S_BLOCK,
          'J': J_BLOCK}


def get_block():
    '''get cube randomly '''
    block_name = random.choice('OIZTLSJ')
    b = BLOCKS[block_name]
    idx = random.randint(0, len(b) - 1)
    # block_color={"O":(200, 20, 20),"I":(20, 200, 20),"Z":(20, 20, 200),"T":(200, 200, 20)
    #     ,"L":(20, 200, 200),"S":(200, 20, 200),"J":(200, 200, 200)}
    return b[idx]

def get_next_block(block):
    '''Obtain the rotated square while rotating'''
    b = BLOCKS[block.name]
    return b[block.next]
