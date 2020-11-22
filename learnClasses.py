import os
import random
import pygame
pygame.init()
running = True
screen = pygame.display.set_mode((600,600))
screen.fill((0,100,200))
pygame.display.set_caption("Computer Project - Class 12 : By - Arushi, Malavika and Praakhya")
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYUP and event.key == pygame.K_q:
                running = False
    pygame.display.update()

pygame.quit()
