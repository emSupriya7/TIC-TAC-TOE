import pygame
import sys
import random
import time
from pygame import mixer
import numpy as np
pygame.init()
mixer.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
WINNING_LINE_WIDTH = 15
BACKGROUND_CLR = (197, 118, 236)
LINE_COLOR = (255, 255, 255)
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CIRCLE_COLOR = (246, 246, 100)
CROSS_SYMBOL_WIDTH = 25
SPACE = 55
CROSS_SYMBOL_COLOR = (204, 0, 0)
font_style = pygame.font.SysFont("autobus", 105) #
bg_music = pygame.mixer.music.load("bg_audio.mp3")
pygame.mixer.music.play(-1)
SQUARE_SIZE = 200

width_screen = 500
heigth_screen = 500
screen = pygame.display.set_mode((width_screen,heigth_screen))
pygame.display.set_caption("tic tac toe")
pygame.display.update()


font_style1 = pygame.font.SysFont("Arial Black",23)
image = pygame.image.load('image.png')
screen.blit(image,(0,0))
pygame.display.update()
start = font_style1.render("Hit space bar to START",True,(255, 255, 255))
screen.blit(start,(100 ,450))
pygame.display.update()



#Main Game loop

def main_loop():
	BACKGROUND_CLR = (197, 118, 236)
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("TIC TAC TOE")
	screen.fill(BACKGROUND_CLR)
	board = np.zeros((BOARD_ROWS, BOARD_COLS))
	font_style = pygame.font.SysFont("autobus", 105)
	bg_music = pygame.mixer.music.load("bg_audio.mp3")
	pygame.mixer.music.play(-1)
	

	def drawing_lines():
		#this function is used to draw grid lines
		#									 start_pt   end_pt
		pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
		pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
		pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
		pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)
	def mark_square(row, col, player):
		board[row][col] = player
	def available_squares(row, col):
		return board[row][col] == 0
	def is_board_full():
		for row in range(BOARD_ROWS):
			for col in range(BOARD_COLS):
				if board[row][col] == 0:
					return False
		return True
	pygame.display.update()
	drawing_lines()

	def draw_figures():
		for row in range(BOARD_ROWS):
			for col in range(BOARD_COLS):
				if board[row][col] == 1:        
					pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
				elif board[row][col] == 2:     
					pygame.draw.line( screen, CROSS_SYMBOL_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_SYMBOL_WIDTH )	
					pygame.draw.line( screen, CROSS_SYMBOL_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_SYMBOL_WIDTH )
	pygame.display.update()
	def check_win(player):
		for col in range(BOARD_COLS):
			if board[0][col] == player and board[1][col] == player and board[2][col] == player:
				draw_vertical_winning_line(col, player)
				return True

		for row in range(BOARD_ROWS):
			if board[row][0] == player and board[row][1] == player and board[row][2] == player:
				draw_horizontal_winning_line(row, player)
				return True

		if board[2][0] == player and board[1][1] == player and board[0][2] == player:
			draw_asc_diagonal(player)
			return True

		if board[0][0] == player and board[1][1] == player and board[2][2] == player:
			draw_desc_diagonal(player)
			return True

		return False
		pygame.display.update()	

	def draw_vertical_winning_line(col, player):
		posX = col * SQUARE_SIZE + SQUARE_SIZE//2

		if player == 1:
			color = CIRCLE_COLOR
		elif player == 2:
			color = CROSS_SYMBOL_COLOR

		pygame.draw.line( screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )
		pygame.display.update()

	def draw_horizontal_winning_line(row, player):
		posY = row * SQUARE_SIZE + SQUARE_SIZE//2

		if player == 1:
			color = CIRCLE_COLOR
		elif player == 2:
			color = CROSS_SYMBOL_COLOR

		pygame.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), WINNING_LINE_WIDTH)
		pygame.display.update()

	def draw_asc_diagonal(player):
		if player == 1:
			color = CIRCLE_COLOR
		elif player == 2:
			color = CROSS_SYMBOL_COLOR

		pygame.draw.line( screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WINNING_LINE_WIDTH )
		pygame.display.update()
		
	def draw_desc_diagonal(player):
		if player == 1:
			color = CIRCLE_COLOR
		elif player == 2:
			color = CROSS_SYMBOL_COLOR

		pygame.draw.line( screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WINNING_LINE_WIDTH )
		pygame.display.update()

	def restart():
		screen.fill(BACKGROUND_CLR)
		drawing_lines()
		for row in range(BOARD_ROWS):
			for col in range(BOARD_COLS):
				board[row][col] = 0

	drawing_lines()
	pygame.display.update()

	player = 1
	end_game = False

	while not end_game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			if event.type == pygame.MOUSEBUTTONDOWN and not end_game:

				mouseX = event.pos[0] 
				mouseY = event.pos[1] 

				clicked_row = int(mouseY // SQUARE_SIZE)
				clicked_col = int(mouseX // SQUARE_SIZE)

				if available_squares( clicked_row, clicked_col ):

					mark_square( clicked_row, clicked_col, player )
					if check_win( player ):
						end_game = True
					player = player % 2 + 1

					draw_figures()
					pygame.display.update()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					restart()
					player = 1
					end_game = False

	pygame.display.update()
	game_over = font_style.render("GAME OVER", True, (0, 0, 0))
	screen.blit(game_over, (95, 260))
	pygame.display.update()
	time.sleep(1)		

	pygame.display.update()
	
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				main_loop()

