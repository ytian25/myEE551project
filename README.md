TETRIS



GENERAL THINKING

It can be roughly divided into: the definition of interface and cube, the left, right, down movement, rotation, to judge whether touch the side or not, stopping(or docking),  and finally to judge the end of the game.


1 main.py is the main program to control the whole program
2 Functions.py mainly writes several frequently called functions
3 Screens.py is responsible for screen display
4 Squares. py will customize Tetris
5 Events.py handles the left and right buttons
6 Settings are mainly the interface parameters of the game.


Enter: Game Start
Pause: space pause
Keyboard button up: rotation
Keyboard button down left and right: position change
(ATTENTION:Due to technical reasons, the drop function needs to be realized by pressing the down key constantly. It can't automatically drop. Sorry.)

Interface:

The whole interface of Russian Tetris is divided into two parts, the game area on the left and the display area on the right, showing scores, speed, the next block style, etc.
The game area is made up of small squares. In order to see it intuitively, I deliberately drew a grid line. Interface parameters can be modified within settings.py.

Cube:

There are seven species named O, I, Z, T, L, S and J.
The named tuple in collections module is used to define the blocks.
Get_block method to get blocks
Get_next_block method to get the next box
Directly define a square in a two-dimensional array, with dots. empty and 0 solid. (Use. to express empty space is to see intuitively, if you use blank space will not see clearly.

Rotation:

For example, type I, there are two forms: horizontal and vertical. The so-called rotation, on the surface, is to rotate the square clockwise by 90 degrees.
But in practice, we do not really need to achieve this "rotation" effect.
At the end of the implementation, these graphics are painted on the interface, and every time they are refreshed,
Everything on the interface will be emptied and redrawn, so the rotation is just drawing the current square instead of drawing the previous shape.
It's about drawing the shape after rotation. On the other hand, in some cases it is impossible to rotate.
For example, type I vertical bar can not rotate when it is close to the left and right border.

The game_area variable:

Represents the entire game area, using a two-dimensional array, when the interior is empty, using points.
Update the part of the game_area area to 0 when a box arrives to prevent the next box from overlapping with the previous one and ensure that it is stacked together.

Stop(dock):
When a square falls to the end or meets another square, it cannot fall.
First of all, we need to determine whether we can stop. After the stop happens, we draw the non-empty dots of the current box onto the game area. To put it bluntly, copy the non-empty point of current_block into game_area according to its corresponding position.
It also calculates whether a row is fully filled, and if it is fully filled, it will be eliminated.





