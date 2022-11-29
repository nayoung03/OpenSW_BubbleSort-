# 배경 이미지 설정
import os
import pygame

pygame.init()
screen_width = 448  # 가로 크기
screen_height = 720 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Puzzle Bubble") # 게임 이름
clock = pygame.time.Clock()

# background image load
current_path = os.path.dirname(__file__)    # 파일 경로를 받아오기
background = pygame.image.load(os.path.join(current_path, "background.png"))

running = True
while running:
    clock.tick(60)  # FPS 60 으로 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 게임 종료
            running = False

    screen.blit(background, (0, 0)) # 배경 이미지 위치(0, 0) 조정
    pygame.display.update() # 화면 업데이트

pygame.quit()