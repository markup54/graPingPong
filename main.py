import pygame
from pygame.examples.go_over_there import clock, running

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
running = True

x_ball = 10
y_ball = 10
move_ball_x = 3
move_ball_y = 3

x_rocket = 10
y_rocket = 30



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y_rocket = y_rocket - 5
    if keys[pygame.K_s]:
        y_rocket = y_rocket +5
    x_ball = x_ball + move_ball_x
    y_ball = y_ball + move_ball_y
    if y_ball > screen.get_height():
        move_ball_y = -move_ball_y

    if y_ball< 0:
        move_ball_y = -move_ball_y

    if x_ball>screen.get_width():
        move_ball_x = - move_ball_x
    if x_ball<0:
        move_ball_x = - move_ball_x
    screen.fill("green")
    pygame.draw.circle(screen,"white",(x_ball,y_ball),10)

    pygame.draw.rect(screen,"black",(x_rocket,y_rocket,10,50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

