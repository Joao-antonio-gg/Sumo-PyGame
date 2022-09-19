import pygame
import random
import sys
import time

pygame.init()


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
        img_2 = pygame.transform.scale(img_2, (sumo_largura, sumo_altura))
        self.image = img_2

    # Atualizar posição do sumo
    def update(self):
        self.rect.x += self.speedx

        # Manter o sumo dentro de quadro
        if self.rect.right > largura:
            sumo_sprite.update_image(direita[1])
            key_pess = self.rect.right
            self.rect.right = largura
            if key_pess == largura:
                sumo_sprite.update_image(direita[2])
        if self.rect.left < 0:
            sumo_sprite.update_image(esquerda[1])
            key_pess = self.rect.left
            self.rect.left = 0
            if key_pess == 0:
                sumo_sprite.update_image(esquerda[2])

    def get_position(self):
        return self.rect.x, self.rect.y


class comidas(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura - comida_largura)
        self.rect.y = random.randint(-100, - comida_altura)
        self.speedy = random.randint(1, 3)
        self.mask = pygame.mask.from_surface(onigiripng)
        self.mask = pygame.mask.from_surface(sushipng)
        self.mask = pygame.mask.from_surface(lamenpng)
        self.mask = pygame.mask.from_surface(docepng)

    # Atualizar posição das comidas
    def update(self):
        self.rect.y += self.speedy

        # Se a comida sair de quadro, spawnar nova comida em posição e velocidade aleatórias
        if self.rect.top > altura or self.rect.right < 0 or self.rect.left > largura:
            self.rect.x = random.randint(0, largura - comida_largura)
            self.rect.y = random.randint(-100, -comida_altura)
            self.speedy = random.randint(1, 3)


class bigorna(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura - comida_largura)
        self.rect.y = random.randint(-100, - comida_largura)
        self.speedy = random.randint(1, 3)
        self.mask = pygame.mask.from_surface(bigornapng)

    # Atualizar posição da bigorna
    def update(self):
        self.rect.y += self.speedy

        # Se a bigorna sair de quadro, spawnar nova bigorna em posição e velocidade aleatórias
        if self.rect.top > altura or self.rect.right < 0 or self.rect.left > largura:
            self.rect.x = random.randint(0, largura - comida_largura)
            self.rect.y = random.randint(-100, - comida_largura)
            self.speedy = random.randint(1, 3)


def extractMaximum(ss):
    num, res = 0, 0
    for i in range(len(ss)):
        if ss[i] >= "0" and ss[i] <= "9":
            num = num * 10 + int(int(ss[i]) - 0)
        else:
            res = max(res, num)
            num = 0
    return max(res, num)


comida_largura = 60
comida_altura = 60
sumo_largura = 150
sumo_altura = 150
bigorna_altura = 80
bigorna_largura = 100
# ---------------------------------------------------------------------------------------------------
# Importar comidas, bigorna e sumo
sumopng = pygame.image.load('Assets/sumo_parado.png')
bigornapng = pygame.image.load('Assets/bigorna.png')
onigiripng = pygame.image.load('Assets/onigiri.png')

sushipng = pygame.image.load('Assets/sushi.png')

lamenpng = pygame.image.load('Assets/lamen.png')
docepng = pygame.image.load('Assets/doce.png')
# ---------------------------------------------------------------------------------------------------
# Redimensionar comidas, bigorna e sumo
onigiripng = pygame.transform.scale(onigiripng, (comida_largura, comida_altura))
lamenpng = pygame.transform.scale(lamenpng, (comida_largura, comida_altura))
docepng = pygame.transform.scale(docepng, (comida_largura, comida_altura))
sushipng = pygame.transform.scale(sushipng, (comida_largura, comida_altura))
# ---------------------------------------------------------------------------------------------------
# Cria classe sumo

sumopng = pygame.transform.scale(sumopng, (sumo_largura, sumo_altura))
bigornapng = pygame.transform.scale(bigornapng, (bigorna_largura, bigorna_altura))
largura = 1024

altura = 768

# ---------------------------------------------------------------------------------------------------
# Importar frames das animações e background
direita = [pygame.image.load('Assets/d0.png'), pygame.image.load('Assets/d1.png'), pygame.image.load('Assets/d2.png')]
esquerda = [pygame.image.load('Assets/e0.png'), pygame.image.load('Assets/e1.png'), pygame.image.load('Assets/e2.png')]
comer = [pygame.image.load('Assets/c0.png'), pygame.image.load('Assets/c1.png'), pygame.image.load('Assets/c2.png'),
         pygame.image.load('Assets/c3.png'), pygame.image.load('Assets/c4.png')]
morrer = [pygame.image.load('Assets/m1.png'), pygame.image.load('Assets/m2.png'), pygame.image.load('Assets/m3.png'),
          pygame.image.load('Assets/m4.png'), pygame.image.load('Assets/m5.png')]
background = pygame.image.load('Assets/wallpaper 2.png')
# ---------------------------------------------------------------------------------------------------
# Importar sons
som_comer = pygame.mixer.Sound('Assets/comer.mp3')
som_pontos = pygame.mixer.Sound('Assets/checkpoint.mp3')
som_perdeu = pygame.mixer.Sound('Assets/lose.mp3')
musica = pygame.mixer.Sound('Assets/musica.mp3')
# ---------------------------------------------------------------------------------------------------
# Criar grupos de sprites
sprites = pygame.sprite.Group()
bigorna_sprite = pygame.sprite.Group()
sushi_sprite = pygame.sprite.Group()
onigiri_sprite = pygame.sprite.Group()
lamen_sprite = pygame.sprite.Group()
doce_sprite = pygame.sprite.Group()
sprit_list = [bigorna_sprite, sushi_sprite, onigiri_sprite, lamen_sprite, doce_sprite]
sumo_sprite = sumo(sumopng)
sprites.add(sumo_sprite)
# ---------------------------------------------------------------------------------------------------
# Cria define tamanhos da janela
largura = 1024
altura = 768
janela = pygame.display.set_mode((largura, altura))
