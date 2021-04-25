'''READ ME

Spicy Clicker game was created by Arthur Lund in 2021.

To run the game:
    1. Install the pygame modules into your preferred Python 3 interpreter
    2. Keep the .py file and the supporting images in the same file directory.
    3. Run the .py file in your interpreter.

Sources:
    https://www.101computing.net/pong-tutorial-using-pygame-adding-a-scoring-system/ (6/4/2021)
    https://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame (6/4/2021)
    https://stackoverflow.com/questions/26002497/how-to-run-a-background-timer-in-python (13/4/2021)
    https://stackoverflow.com/questions/3718657/how-do-you-properly-determine-the-current-script-directory (14/4/2021)
    https://stackoverflow.com/questions/40566585/how-to-change-the-name-of-a-pygame-window (14/4/2021)
'''


'''Import libraries'''
import pygame  # pygame module
import sys  # module to communicate with windows
import random # random module; used to randomly generate target coords
import time  # used to implement the 60 second timer
import os  # used to determine current directory

'''Game setup section; only runs once'''
pygame.init()  # starts the game engine
clock = pygame.time.Clock()  # creates clock to limit frames per second
FPS = 60  # sets max speed (Frames Per Second) of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 1000, 800  # sets size of screen/window
pygame.display.set_caption('Spicy Clicker')  # set game window title
screen = pygame.display.set_mode(SCREENSIZE)  # creates window and game screen
filepath = os.path.dirname(os.path.abspath(__file__))


'''Setup for player1 sprite'''
player1_image = pygame.image.load(filepath + "\\Ooooo.png")  # load image
player1_image_size = [100, 150]  # image scale
player1_image = pygame.transform.scale(player1_image, player1_image_size)  # scale image


'''Setup for target sprite'''
target_image = pygame.image.load(filepath + "\\Target.png") # load iamge
target_image_size = [90, 90]  # image scale
# line below sets initial target coords
target_coords = [random.randint(0, SCREENWIDTH - target_image_size[0]), random.randint(0, SCREENHEIGHT - target_image_size[1])]
target_image = pygame.transform.scale(target_image, target_image_size)  # scale image


'''Setup for background'''
background = pygame.image.load(filepath + "\\background.jpg")  # load image
background = pygame.transform.scale(background, SCREENSIZE)  # scale image


'''Game configurations'''
firelock = False  # initialise variable to stop play from holding down mouse button
font = pygame.font.Font(None, 74) # font for scoreboard
score = 0  # initialise score variable
pygame.mouse.set_visible(False)  # hide cursor
gameState = "running"  # variable that controls the game state
start_time = time.time()  # stores start time
total_time = 60  # number of seconds the game runs for
white = (255, 255, 255)  # sets colour white


while time.time() - start_time < total_time and gameState != 'exit': # Runs game until time is up
    '''Event listener - gets user interaction events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if user has closed the window...
            gameState = "exit"  # exit game loop
        if pygame.mouse.get_pressed()[0] and not firelock:  # if the player left clicks and the firelock is not on...
            if player1.colliderect(target): # if the sprite has collided with the target...
                # line below randomly relocates the target
                target_coords = [random.randint(0, SCREENWIDTH - target_image_size[0]), random.randint(0, SCREENHEIGHT - target_image_size[1])]
                firelock = True  # turn on firelock
                score += 1  # increase score by one
        if event.type == pygame.MOUSEBUTTONUP: # when the player lifts the left mouse button
            firelock = False  # turn off the firelock
    
    '''Event handler'''
    screen.blit(background, (0,0))  # render background
    mousePosition = pygame.mouse.get_pos()  # gets coordinates of cursor
    # line below sets sprite coords so the cursor is in the middle
    player1_coords = [mousePosition[0] - player1_image_size[0] / 2, mousePosition[1] - player1_image_size[1] / 2]
    target = screen.blit(target_image, target_coords)  # render target
    player1 = screen.blit(player1_image, player1_coords)  # render player1
    scoreboard = font.render(("Score: " + str(score)), 1, white)  # creates image of scoreboard
    screen.blit(scoreboard, (10,10))  # renders scoreboard image
    time_remaining = total_time - (time.time() - start_time)  # calculate time remaining
    timer = font.render(("Time remaining: " + str(int(time_remaining))), 1, white)
    screen.blit(timer, (500,10))  # renders timer image
    
    '''System lines'''
    pygame.display.flip()  # transfers build screen to human visable screen
    clock.tick(FPS)  # limits game to frame per second, FPS value
# END GAME LOOP

if gameState != 'exit':  # if the user didn't close the window (i.e. they finished the game)
    font = pygame.font.Font(None, 100) # increase font size
    screen.blit(background, (0,0))  # render background
    final_score_1 = font.render(("YOUR FINAL SCORE..."), 1, white)  # create final results image
    screen.blit(final_score_1, (175,300))  # render final results
    pygame.display.flip()  # display screen
    time.sleep(3)  # 3 second delay
    final_score_2 = font.render(("WAS " + str(score) + "!!!"), 1, white)  # create final results image
    screen.blit(final_score_2, (340,360))  # render final results
    pygame.display.flip()  # display screen
    while time.time() - start_time < (total_time + 13) and gameState != 'exit': # waits for 10 seconds unless user closes window
        continue
print("The game has closed")  # notifies user the game has ended
pygame.quit()   # stops the game engine
sys.exit()  # close window
