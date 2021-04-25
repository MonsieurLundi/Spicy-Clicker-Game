# Spicy Clicker Technical Documentation
Spicy Clicker is a simple mouse game created in Python where the aim is to click on the chilli pepper as many times as possible in one minute.
The modules used in the code include pygame, sys, random, time and os.
The base template came from Blackboard.


## Revision History
31/3/2021 - Created basic game functionality, including:<br />
      •	a red dot as a target<br />
      •	an image of Shaquille O’Neal’s face as the cursor<br />
      •	target relocates when clicked<br />
      •	a firelock to prevent the player from holding left click<br />
6/4/2021<br />
      •	Changed target sprite to a spicy chilli<br />
      •	Added fire background<br />
      •	Added score counter that increments when target is clicked<br />
13/4/2021<br />
      •	Added timer<br />
      •	Added display final score<br />
      •	Removed unnecessary colours<br />
14/4/2021<br />
      •	Fixed exiting delay bug<br />
      •	Changed game window title to ‘Spicy Clicker’


## Design Goals
I wanted my game to be a simple clicking game with a points counter that goes up every time you click on the target with the cursor, testing the player’s reflexes.
The score counter was simple to implement- I simply created a variable called score that increased when the target was clicked and used pygame’s font, render and blit functions to create a scoreboard in the top left of the screen screen.
The target would relocate to a random location every time it was clicked, which was achieved by generating random coordinates within the boundaries of the 1000 by 800 window. I also had to take into account the dimensions of the target, because if it relocated to the very edge of the window it would be it impossible for the player to see.
To prevent the user from simply holding down left click and wiping their cursor all over the window, I implemented a firelock that made the lift the left mouse button if they wanted to ‘shoot’ again.
To give purpose to the game, I implemented a 60-second timer in the top right of the screen. It uses the imported time module to store the time the game started, and every game loop it checks the time elapsed by subtracting the start time from the current time.


## Requirements
To play the game it is necessary to have Python3 installed (download from https://www.python.org/downloads/) as well as the module for pygame (type pip install pygame in command prompt). The other modules come built-in with Python. The accompanying images that make up the background and sprites should be in the same directory as the .py run file. The hardware required is very minimal, as it only uses about 24MB of RAM.
Once these requirements are fulfilled, simply run the game file in your preferred Python interpreter (e.g. Thonny, Pycharm, Visual Studio Code, IDLE).


## Pseudo Code
set frames per second to 60<br />
set game windows size 1000 x 800<br />
create game window

load player1 image<br />
scale player1 image to 100x150

load target image<br />
scale target image to 90x90<br />
target_coords  randomX, randomY

load background image<br />
scale background image to 1000x800

firelock <-- False <br />
score <-- 0<br />
set mouse to invisible<br />
start_time  current_time<br />
total_time = 60 

WHILE current_time - start_time < total_time DO<br />
START EVENT MONITOR<br />
IF user_has_quit = True THEN<br />
		Quit<br />
	END IF<br />
	IF left_mouse_button_down = True AND firelock = False THEN<br />
		IF player1 collides with target THEN<br />
			target_coords  randomX, randomY<br />
score <-- score + 1<br />
firelock <-- True<br />
END IF<br />
END IF<br />
IF left_mouse_button_up = True THEN<br />
	Firelock <-- FALSE<br />
END IF<br />
END OF EVENT MONITOR<br />
	
BEGIN EVENT HANDLER<br />
	render background at 0,0<br />
	load mouse_coords<br />
	render player1 at mouse_coords<br />
	render target at randomX, randomY<br />
	render score at 10,10<br />
	time_remaining  total_time – (current_time – start_time)<br />
	render time_remaining at 700,10<br />
END EVENT HANDLER<br />
	
display screen<br />
END WHILE

render background at 0,0<br />
render (“Final score is”, score) at 400,350<br />
close game window


## Running the game
    1. Install the pygame modules into your preferred Python 3 interpreter
    2. Keep the .py file and the supporting images in the same file directory.
    3. Run the .py file in your interpreter.

## Sources
    https://www.101computing.net/pong-tutorial-using-pygame-adding-a-scoring-system/ (6/4/2021)
    https://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame (6/4/2021)
    https://stackoverflow.com/questions/26002497/how-to-run-a-background-timer-in-python (13/4/2021)
    https://stackoverflow.com/questions/3718657/how-do-you-properly-determine-the-current-script-directory (14/4/2021)
    https://stackoverflow.com/questions/40566585/how-to-change-the-name-of-a-pygame-window (14/4/2021)
