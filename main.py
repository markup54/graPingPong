import pygame
from pygame.examples.go_over_there import clock, running

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
running = True

x_ball = 10
y_ball = 10
move_ball = 3

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    x_ball = x_ball + move_ball
    y_ball = y_ball + move_ball
    screen.fill("green")
    pygame.draw.circle(screen,"white",(x_ball,y_ball),10)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

