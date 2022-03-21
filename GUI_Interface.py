# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random



WIDTH = 360
HEIGHT = 480
FPS = 30



# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)



# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Absolute")
clock = pygame.time.Clock()

i = 15.0
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление

    # Рендеринг
    screen.fill((17,17,17))

    #monospace Comic Sans MS

    if i > 1.67:
        myfont = pygame.font.SysFont('monospace', 25)
        textsurface = myfont.render('Absolute', False, WHITE)
        screen.blit(textsurface, (WIDTH / 2 - 65, 10))

        picture = pygame.image.load("app.png")
        picture = pygame.transform.scale(picture, (250, 250))
        screen.blit(picture, (WIDTH // 7, HEIGHT // 7))

        myfont = pygame.font.SysFont('Comic Sans MS', 25)
        textsurface = myfont.render('ForceCoin', False, WHITE)
        screen.blit(textsurface, (WIDTH / 2 - 63, 305))




    if i > 1.67:
        pygame.draw.rect(screen, BLUE, (WIDTH // 12, 370, HEIGHT // 1.6, 30))
        pygame.draw.rect(screen, (17, 17, 17), (WIDTH // 10, 375, HEIGHT // 1.67, 20))
        pygame.draw.rect(screen, GREEN, (WIDTH // 10, 375, HEIGHT // i, 20))

    i = i - 0.01


    if i > 1.67:
        myfont = pygame.font.SysFont('monospace', 25)
        textsurface = myfont.render('WITH', False, WHITE)
        screen.blit(textsurface, (WIDTH/2 - 35, HEIGHT/2 + 170))

        myfont = pygame.font.SysFont('monospace', 20)
        textsurface = myfont.render('AnDRoutEa', False, WHITE)
        screen.blit(textsurface, (WIDTH / 2 - 60, HEIGHT / 2 + 200))

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()