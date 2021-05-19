#Importando bibliotecas
import pygame
import random

#Iniciando Pygame
pygame.init()

#Definido janela
Width=1024
Height=769
win = pygame.display.set_mode((Width,Height))

#Nome do jogo
pygame.display.set_caption("Sumo Eats")

#Importar imagens
direita = [pygame.image.load('d0.png'), pygame.image.load('d1.png'), pygame.image.load('d2.png')]
esquerda = [pygame.image.load('e0.png'), pygame.image.load('e1.png'), pygame.image.load('e2.png')]
comer = [pygame.image.load('c0.png'), pygame.image.load('c1.png'), pygame.image.load('c2.png'), pygame.image.load('c3.png'), pygame.image.load('c4.png')]
background = [pygame.image.load('frame-001.png'), pygame.image.load('frame-002.png'), pygame.image.load('frame-003.png'), pygame.image.load('frame-004.png'), pygame.image.load('frame-005.png'), pygame.image.load('frame-006.png'), pygame.image.load('frame-007.png'), pygame.image.load('frame-008.png'), pygame.image.load('frame-009.png'), pygame.image.load('frame-010.png'), pygame.image.load('frame-011.png'), pygame.image.load('frame-012.png'), pygame.image.load('frame-013.png'), pygame.image.load('frame-014.png'), pygame.image.load('frame-015.png'), pygame.image.load('frame-016.png'), pygame.image.load('frame-017.png'), pygame.image.load('frame-018.png'), pygame.image.load('frame-019.png'), pygame.image.load('frame-020.png'), pygame.image.load('frame-021.png'), pygame.image.load('frame-022.png'), pygame.image.load('frame-023.png'), pygame.image.load('frame-024.png'), pygame.image.load('frame-025.png'), pygame.image.load('frame-026.png'), pygame.image.load('frame-027.png'), pygame.image.load('frame-028.png'), pygame.image.load('frame-029.png'), pygame.image.load('frame-030.png'), pygame.image.load('frame-031.png'), pygame.image.load('frame-032.png'), pygame.image.load('frame-033.png'), pygame.image.load('frame-034.png'), pygame.image.load('frame-035.png'), pygame.image.load('frame-036.png'), pygame.image.load('frame-037.png'), pygame.image.load('frame-038.png'), pygame.image.load('frame-039.png'), pygame.image.load('frame-040.png'), pygame.image.load('frame-041.png'), pygame.image.load('frame-042.png'), pygame.image.load('frame-043.png'), pygame.image.load('frame-044.png'), pygame.image.load('frame-045.png'), pygame.image.load('frame-046.png'), pygame.image.load('frame-047.png'), pygame.image.load('frame-048.png'), pygame.image.load('frame-049.png')]

#Importar sons
som_comer = pygame.mixer.Sound('Comendo_Comidas.mp3')
som_pontos = pygame.mixer.Sound('checkpoint.mp3')
som_perdeu = pygame.mixer.Sound('Lose.mp3')
musica = pygame.mixer.music.load('Background_soundtrack-Rude_Eternal_Youth.mp3')
pygame.mixer.music.play(-1)

