# Faça um programa em python que abra e reproduza o áudio de um aequivo mp3

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('McPoze.mp3')
pygame.music.play()
pygame.event.wait()