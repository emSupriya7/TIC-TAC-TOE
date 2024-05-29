import pygame, sys
import numpy as np
import time
pygame.init()
WIDTH = 500
HEIGHT = 500
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
LINE_WIDTH = 15
BOARD_ROWS = 5
BOARD_COLS = 5
WINNING_LINE_WIDTH = 15
BACKGROUND_CLR = (197, 120, 236)
LINE_COLOR = (255, 255, 255)
CIRCLE_RADIUS = 30
CIRCLE_WIDTH = 10
CIRCLE_COLOR = (246, 246, 100)
CROSS_SYMBOL_WIDTH = 15
SPACE = 25
CROSS_SYMBOL_COLOR = (204, 0, 0)
font_style = pygame.font.SysFont("autobus", 85)
bg_music = pygame.mixer.music.load("bg_audio.mp3")
pygame.mixer.music.play(-1)

SQUARE_SIZE = 100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BACKGROUND_CLR)
board = np.zeros((BOARD_ROWS, BOARD_COLS))


def draw_lines():
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (500, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (500, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 300), (500, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (500, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 500), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 500), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (300, 0), (300, 500), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 500), LINE_WIDTH)

    
def drawing_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 100 + 100 / 2 ), int(row * 100 + 50)), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_SYMBOL_COLOR, (col * 100 + SPACE, row * 100 + 100 - SPACE), (col * 100 + 100 - SPACE, row * 100 + SPACE), CROSS_SYMBOL_WIDTH )
                pygame.draw.line(screen, CROSS_SYMBOL_COLOR, (col * 100 + SPACE, row * 100 + SPACE), (col * 100 + 100 - SPACE, row * 100 + 100 - SPACE), CROSS_SYMBOL_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    for col in range(BOARD_COLS):   # vertical win check
        if board[0][col] == player and board[1][col] == player and board[2][col] == player and board[3][col] == player and board[4][col] == player:
            draw_vertical_win_line(col, player)
            return True

    for row in range(BOARD_ROWS):   # horizontal win check
        if board[row][0] == player and board[row][1] ==player and board[row][2] == player and board[row][3] == player and board[row][4] == player:
            draw_horizontal_win_line(row, player)
            return True

    if board[4][0] == player and board[3][1] == player and board[2][2] == player and board[1][3] == player and board[0][4] == player:       # Ascening diagonal win check 
        draw_asc_diagonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player and board[3][3] == player and board[4][4] == player:     # Descending diagonal win check 
        draw_desc_diagonal(player)    
        return True

    return False   


def draw_vertical_win_line(col, player):
    posX = col * 100 + 50

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_SYMBOL_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), 15 )

def draw_horizontal_win_line(row, player):
    posY = row * 100 + 50
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_SYMBOL_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), 15 )

    
def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_SYMBOL_COLOR
    
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15 )

def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_SYMBOL_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15 )    

def restart():
	screen.fill( BACKGROUND_CLR )
	draw_lines()
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			board[row][col] = 0

draw_lines()


player = 1
end_game = False

while not end_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN and not end_game:
        positionX = event.pos[0]
        positionY = event.pos[1]
        clickedRow = int(positionY // SQUARE_SIZE)
        clickedCol = int(positionX //SQUARE_SIZE)
        if available_square(clickedRow, clickedCol):
                mark_square(clickedRow, clickedCol, player)
                if check_win(player):
                    end_game = True
                player = player % 2 + 1
                drawing_figures()    
        pygame.display.update()       


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()         

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player = 1
                end_game = False

    pygame.display.update()    
game_over = font_style.render("GAME OVER", True, (0, 0, 0))
screen.blit(game_over, (75, 260))
pygame.display.update()
time.sleep(5)
pygame.quit()    



