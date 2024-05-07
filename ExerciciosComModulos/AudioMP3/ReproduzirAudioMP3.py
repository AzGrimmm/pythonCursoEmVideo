import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("amb.mp3")
pygame.music.play()
input()
pygame.event.wait()