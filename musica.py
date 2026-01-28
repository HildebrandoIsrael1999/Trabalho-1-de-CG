import pygame

def tocar_musica_menu():
    pygame.mixer.music.load("Músicas/menu.mp3")
    pygame.mixer.music.play(-1)

def tocar_musica_jogo():
    pygame.mixer.music.load("Músicas/Dinâmica do Jogo.mp3")
    pygame.mixer.music.play(-1)

def parar_musica():
    pygame.mixer.music.stop()
