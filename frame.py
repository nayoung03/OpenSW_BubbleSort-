import pygame

pygame.init()
screen_width = 448  # 가로 크기
screen_height = 720 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Puzzle Bubble") # 게임 이름
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)  # FPS 60 으로 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 게임 종료
            running = False

pygame.quit()