import pygame
import sys
from game_window_class import *
from button_class import *

width = 800
height = 800
background_color = (255,255,255)
FPS = 60
#x, y = 85, 85


# ----------------------- Setting functions -------

def get_events():
	global runing
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runing = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			if mouse_on_grid(mouse_pos):
				click_cell(mouse_pos)
			else:
				for button in buttons:
					button.click()


def update():
	game_window.update()
	for button in buttons:
		button.update(mouse_pos, game_state=state)


def draw():
	window.fill(background_color)
	for button in buttons:
		button.draw()
	game_window.draw()

#-------------------------- Running functions ------

def running_get_events():
	global runing
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runing = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			if mouse_on_grid(mouse_pos):
				click_cell(mouse_pos)
			else:
				for button in buttons:
					button.click()


def running_update():
	game_window.update()
	for button in buttons:
		button.update(mouse_pos, game_state=state)
	if frame_count%(FPS//10) == 0:
		game_window.evaluate()


def running_draw():
	window.fill(background_color)
	for button in buttons:
		button.draw()
	game_window.draw()

#--------------------------- Paused functions -----

def paused_get_events():
	global runing
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runing = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = pygame.mouse.get_pos()
			if mouse_on_grid(mouse_pos):
				click_cell(mouse_pos)
			else:
				for button in buttons:
					button.click()


def paused_update():
	game_window.update()
	for button in buttons:
		button.update(mouse_pos, game_state=state)


def paused_draw():
	window.fill(background_color)
	for button in buttons:
		button.draw()
	game_window.draw()



def mouse_on_grid(pos):

	if pos[0] > 100 and pos[0] < width-100:
		if pos[1] > 100 and pos[1] < height-100:
			return True
	return False

def click_cell(pos):
	#print('click')

	grid_pos = [pos[0] - 100, pos[1]-100]
	grid_pos[0] =grid_pos[0]//20
	grid_pos[1] =grid_pos[1]//20
	if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
		game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
	else:
		game_window.grid[grid_pos[1]][grid_pos[0]].alive=True

def make_buttons():

	buttons = []
	buttons.append(Button(surface=window, x=(width-10)//2 - 50,
	 y= 50,
	 width=90, height=30,
	 text='Run',colour=(107, 193, 214),
	  hover_colour=(135, 201, 169),
	   bold_text=True, function=run_game,
	   state='setting'))
	buttons.append(Button(surface=window, x=(width-10)//2 - 50,
		y= 50,width=90, height=30,
		text='Pause',colour=(18,104,135),
		hover_colour=(51,168,212),
		 bold_text=True, function=pause_game,
		 state='running'))
	buttons.append(Button(surface=window, x=(width-10)//4 - 50,
		y= 50,width=90, height=30,
		text='Reset',colour=(117,14,14),
		hover_colour=(217,54,54),
		 bold_text=True, function=reset_grid,
		 state='paused'))
	buttons.append(Button(surface=window, x=(width-10)//1.3 - 50,
	 y= 50,
	 width=90, height=30,
	 text='Resume',colour=(28,111,81),
	  hover_colour=(107, 193, 214),
	   bold_text=True, function=run_game,
	   state='paused'))


	return buttons

def run_game():
	global state
	state = 'running'
	#print(len(game_window.grid))

def pause_game():
	global state
	state = 'paused'

def reset_grid():
	global state
	state = 'setting'
	#main()
	game_window.reset_grid()
	#get_events()
	#update()
	#print(len(game_window.grid))
	#draw()

pygame.init()
window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
game_window = game_window(window, 100, 100)

buttons = make_buttons()
state= 'setting'
frame_count = 0

runing = True
while runing:
	frame_count += 1
	mouse_pos = pygame.mouse.get_pos()

	if state=='setting':
		get_events()
		update()
		draw()

	if state=='running':
		running_get_events()
		running_update()
		running_draw()

	if state=='paused':
		paused_get_events()
		paused_update()
		paused_draw()

	pygame.display.update()
	clock.tick(FPS)
	#print(state)

pygame.quit()
sys.exit()