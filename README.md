TETRIS



GENERAL THINKING

1.Main.py controls the whole program
2.Functions.py saves game status
3.Screens.py is responsible for drawing the interface
4.Squares.py is responsible for the calculation of squares
5.Events.py is responsible for updating input
6.Settings.py Save Game Settings

Before start, we need to know what we need to do:

1.Computing, letting the computer know what to do next.
2.Control, let the player operate.
3.Interface, for players to see.

COMPUTING

* The calculation of game state (whether the game is active or not)
Create a Status class to store the game status information, save it in functions, use it when the game status needs to be updated, and read the status information when refreshing the interface.

* Storage of all block location information
We can create a Squares class for the box and save it in squares. py.
Create a two-dimensional list and specify that False is square-free and True is square-free.
Create a coordinate curr_sq to save the current active box location.
Create a list curr_shape containing several coordinates to save the position of the box around the current active box (several blocks around the central box). Note that curr_shape coordinates can be relative to curr_sq coordinates, so that curr_sq can be modified only for each fall or move.
Of course, we need to specify the shape of the box, create a Settings class, save it in settings. py, and save the information.

* Horizontal movement, vertical drop and rotation of the current active box

* Determine when the current active box stops and generates a new box

Add valid () to determine whether the movement, fall or rotation conflicts with the existing block. If the conflict rolls back to the previous conflict-free state.

* Computation of output


* Computation of input


CONTROLL


INTERFACE

Create a new screens.py to save the output method.
Add update_screen() to draw the graph.

LAST STEP

Add an infinite loop to main. py, calling check_events () and update_screen () in turn.




