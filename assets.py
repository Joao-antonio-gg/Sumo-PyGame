from unicodedata import name
import pygame; import random; import sys; import time

pygame.init()
comida_largura = 60; comida_altura = 60; sumo_largura = 150; sumo_altura = 150; bigorna_altura = 80; bigorna_largura = 100
#---------------------------------------------------------------------------------------------------
#Importar comidas, bigorna e sumo
sumopng = pygame.image.load('Assets/sumo_parado.png'); bigornapng = pygame.image.load('Assets/bigorna.png')
onigiripng = pygame.image.load('Assets/onigiri.png'); sushipng = pygame.image.load('Assets/sushi.png')
lamenpng = pygame.image.load('Assets/lamen.png'); docepng = pygame.image.load('Assets/doce.png')
#---------------------------------------------------------------------------------------------------
#Redimensionar comidas, bigorna e sumo
onigiripng = pygame.transform.scale(onigiripng, (comida_largura, comida_altura))
lamenpng = pygame.transform.scale(lamenpng, (comida_largura, comida_altura)) 
docepng = pygame.transform.scale(docepng, (comida_largura, comida_altura))
sushipng = pygame.transform.scale(sushipng, (comida_largura, comida_altura))
sumopng = pygame.transform.scale(sumopng, (sumo_largura, sumo_altura))
bigornapng = pygame.transform.scale(bigornapng, (bigorna_largura, bigorna_altura))
#---------------------------------------------------------------------------------------------------
#Cria classe sumo

largura=1024; altura=768
class sumo(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura + 10
        self.speedx = 0
        self.mask = pygame.mask.from_surface(sumopng)
    
    def update_image(self, img_2):
        img_2 = pygame.transform.scale(img_2,(sumo_largura,sumo_altura))
        self.image = img_2

#Atualizar posição do sumo
    def update(self):
        self.rect.x += self.speedx
 
#Manter o sumo dentro de quadro
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0
#---------------------------------------------------------------------------------------------------
#Importar frames das animações e background
direita = [pygame.image.load('Assets/d0.png'), pygame.image.load('Assets/d1.png'), pygame.image.load('Assets/d2.png')]
esquerda = [pygame.image.load('Assets/e0.png'), pygame.image.load('Assets/e1.png'), pygame.image.load('Assets/e2.png')]
comer = [pygame.image.load('Assets/c0.png'), pygame.image.load('Assets/c1.png'), pygame.image.load('Assets/c2.png'), pygame.image.load('Assets/c3.png'), pygame.image.load('Assets/c4.png')]
morrer = [pygame.image.load('Assets/m1.png'), pygame.image.load('Assets/m2.png'), pygame.image.load('Assets/m3.png'), pygame.image.load('Assets/m4.png'), pygame.image.load('Assets/m5.png')]
background = pygame.image.load('Assets/wallpaper 2.png')
#---------------------------------------------------------------------------------------------------
#Importar sons
som_comer = pygame.mixer.Sound('Assets/comer.mp3')
som_pontos = pygame.mixer.Sound('Assets/checkpoint.mp3')
som_perdeu = pygame.mixer.Sound('Assets/lose.mp3')
musica = pygame.mixer.music.load('Assets/musica.mp3')
#---------------------------------------------------------------------------------------------------
#Criar grupos de sprites
sprites = pygame.sprite.Group()
onigiri_sprite = pygame.sprite.Group()
sushi_sprite = pygame.sprite.Group()
doce_sprite = pygame.sprite.Group()
lamen_sprite = pygame.sprite.Group()
bigorna_sprite = pygame.sprite.Group()
sumo_sprite = sumo(sumopng)
sprites.add(sumo_sprite)
#---------------------------------------------------------------------------------------------------
#Cria define tamanhos da janela
largura=1024; altura=768
janela = pygame.display.set_mode((largura,altura))
