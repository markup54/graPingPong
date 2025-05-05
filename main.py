import pygame
from pygame.examples.go_over_there import clock, running

pygame.init()

screen = pygame.display.set_mode((1280,720))

clock = pygame.time.Clock()
running = True

while running:
    screen.fill("green")
    pygame.draw.circle(screen,"white",(30,60),10)
    pygame.display.flip()
    clock.tick(60)

