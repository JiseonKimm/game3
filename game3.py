import sys
import pygame
from pygame.locals import *
import random, time

pygame.init()

## 컬러 세팅 ##
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
SEAGREEN = (60, 179, 113)
VIOLET = (204, 153, 255)
PINK = (255, 153, 153)
ORANGE = (255, 153, 51)


#2. 게임창 설정
GameDisplay = pygame.display.set_mode((630, 630))
GameDisplay.fill(WHITE)
pygame.display.set_caption("mamas's 3rd organize")

clock = pygame.time.Clock()

font = pygame.font.SysFont('Tahoma', 60)
small_font = pygame.font.SysFont('Malgun Gothic', 20)
game_over = font.render("정리 좀 해 이 가시내야!!!", True, BLACK)  # 게임 종료시 문구

def create_rect():
    rect = pygame.Rect(0, 0, 200, 30)
    return rect

def draw_rect(rect, x, y, color):
    pygame.draw.rect(GameDisplay, color, rect.move(x, y))

def move_rect(rect_list):
    for rect, color in rect_list:
        rect.move_ip(0, 35)


def game_loop():
    rect_list = []
    time_counter = 0
    is_game_running = False
    is_selecting = False
    selected_column = 1
    cursor_x = 210
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if is_game_running:
                        is_game_running = False
                        rect_list.clear()
                    else:
                        is_game_running = True
                elif event.key == K_LEFT:
                    if is_selecting:
                        selected_column = max(selected_column - 1, 0)
                        cursor_x = selected_column * 210
                elif event.key == K_RIGHT:
                    if is_selecting:
                        selected_column = min(selected_column + 1, 2)
                        cursor_x = selected_column * 210

        if is_game_running:
            time_counter += clock.get_time()
            if time_counter >= 5000:  # 5초마다
                time_counter = 0
                for _ in range(3):  # 새로운 직사각형 3개 생성하여 rect_list에 추가
                    rect_list.append((create_rect(), random.choice([BLUE, RED, GREEN, BLACK, WHITE, SEAGREEN, VIOLET, PINK, ORANGE])))

            move_rect(rect_list)  # 직사각형들을 아래로 이동시킵니다.
            for i, (rect, color) in enumerate(rect_list):
                draw_rect(rect, i * 210, 0, color)  # 왼쪽, 중간, 오른쪽 3열로 그립니다.

            if is_selecting:
                pygame.draw.rect(GameDisplay, BLACK, (cursor_x, 0, 200, 30), 2)

        pygame.display.update()
        clock.tick(60)

game_loop()