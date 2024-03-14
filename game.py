import pygame

pygame.init()

window = pygame.display.set_mode([600, 600])

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing=False
