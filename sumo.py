#Importar bibliotecas
import pygame
import random
import sys
import time
#---------------------------------------------------------------------------------------------------
#Iniciar Pygame
pygame.init()
#---------------------------------------------------------------------------------------------------
#Definir janela
largura=1024
altura=768
janela = pygame.display.set_mode((largura,altura))
#---------------------------------------------------------------------------------------------------
#Nome do jogo
pygame.display.set_caption("Sumo Eats")
#---------------------------------------------------------------------------------------------------
#Definir dimensões
comida_largura = 60
comida_altura = 60
sumo_largura = 150
sumo_altura = 150
bigorna_altura = 80
bigorna_largura = 100
#---------------------------------------------------------------------------------------------------
#Importar comidas, bigorna e sumo
sumopng = pygame.image.load('Assets/sumo_parado.png')
bigornapng = pygame.image.load('Assets/bigorna.png')
onigiripng = pygame.image.load('Assets/onigiri.png')
sushipng = pygame.image.load('Assets/sushi.png')
lamenpng = pygame.image.load('Assets/lamen.png')
docepng = pygame.image.load('Assets/doce.png')
#---------------------------------------------------------------------------------------------------
#Redimensionar comidas, bigorna e sumo
onigiripng = pygame.transform.scale(onigiripng, (comida_largura, comida_altura))
lamenpng = pygame.transform.scale(lamenpng, (comida_largura, comida_altura))
docepng = pygame.transform.scale(docepng, (comida_largura, comida_altura))
sushipng = pygame.transform.scale(sushipng, (comida_largura, comida_altura))
sumopng = pygame.transform.scale(sumopng, (sumo_largura, sumo_altura))
bigornapng = pygame.transform.scale(bigornapng, (bigorna_largura, bigorna_altura))
#---------------------------------------------------------------------------------------------------
#Importar frames das animações
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
#Definir cores pros textos
branco = (255,255,255)
vermelho = (255, 0, 0)

#---------------------------------------------------------------------------------------------------
#Alterar volume da música
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
#---------------------------------------------------------------------------------------------------
#Importar fontes
fonte_pontos=pygame.font.Font('Assets/arcade.ttf', 100)
fonte_game_over=pygame.font.Font('Assets/gameoverfont.ttf', 170)
fonte_start=pygame.font.SysFont("Consolas", 45)
fonte_pontos_feitos=pygame.font.Font('Assets/gameoverfont.ttf', 90)
#---------------------------------------------------------------------------------------------------
#Definir classe do sumo
class sumo(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura - 5
        self.speedx = 0
        self.mask = pygame.mask.from_surface(sumopng)

#Atualizar posição do sumo
    def update(self):
        self.rect.x += self.speedx
 
#Manter o sumo dentro de quadro
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0
#---------------------------------------------------------------------------------------------------
#Definir classe das comidas
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

#Atualizar posição das comidas
    def update(self):
        self.rect.y += self.speedy

#Se a comida sair de quadro, spawnar nova comida em posição e velocidade aleatórias
        if self.rect.top > altura or self.rect.right < 0 or self.rect.left > largura:
            self.rect.x = random.randint(0, largura-comida_largura)
            self.rect.y = random.randint(-100, -comida_altura)
            self.speedy = random.randint(1, 3)
#---------------------------------------------------------------------------------------------------
#Definir classe da bigorna
class bigorna(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
 
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura - comida_largura)
        self.rect.y = random.randint(-100, - comida_largura)
        self.speedy = random.randint(1, 3)
        self.mask = pygame.mask.from_surface(bigornapng)

#Atualizar posição da bigorna        
    def update(self):  
        self.rect.y += self.speedy

#Se a bigorna sair de quadro, spawnar nova bigorna em posição e velocidade aleatórias
        if self.rect.top > altura or self.rect.right < 0 or self.rect.left > largura:
            self.rect.x = random.randint(0, largura - comida_largura)
            self.rect.y = random.randint(-100, - comida_largura)
            self.speedy = random.randint(1, 3)
#---------------------------------------------------------------------------------------------------
#Definir quadros por segundo
clock = pygame.time.Clock()
FPS = 144
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
#Gerar sushi
for i in range(1):
    sushidif = comidas(sushipng)
    sprites.add(sushidif)
    sushi_sprite.add(sushidif)
#---------------------------------------------------------------------------------------------------
#Gerar onigiri
for i in range(1):
    onigiridif = comidas(onigiripng)
    sprites.add(onigiridif)
    onigiri_sprite.add(onigiridif)
#---------------------------------------------------------------------------------------------------
#Gerar lamen
for i in range(1):
    lamendif = comidas(lamenpng)
    sprites.add(lamendif)
    lamen_sprite.add(lamendif)
#---------------------------------------------------------------------------------------------------    
#Gerar doce
for i in range(1):
    docedif = comidas(docepng)
    sprites.add(docedif)
    doce_sprite.add(docedif)
#---------------------------------------------------------------------------------------------------
#Score inicial
score = 0
#---------------------------------------------------------------------------------------------------
#Tocar a música de fundo em loop
pygame.mixer.music.play(-1)
#---------------------------------------------------------------------------------------------------
#Gerar tela inicial do jogo
inicio_de_jogo=False
while (inicio_de_jogo==False):
    inicio_screen=pygame.image.load('Assets/start.jpeg')
    janela.blit(inicio_screen, (0,0))
    start_enter=fonte_start.render("Press ENTER to start", True, (branco))
    janela.blit(start_enter,(500,600))

    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                inicio_de_jogo=True
    pygame.display.flip()
#---------------------------------------------------------------------------------------------------
#Criar condição de jogo ativo
game_on = True
while game_on:
#---------------------------------------------------------------------------------------------------
#Aumentar o número de bigornas a cada 100 pontos feitos
    if len(bigorna_sprite.sprites()) < (score//100 + 1):
        bigornadif = bigorna(bigornapng)
        sprites.add(bigornadif)
        bigorna_sprite.add(bigornadif)
#---------------------------------------------------------------------------------------------------
    eventos = pygame.event.get()
    for event in eventos:

        if event.type == pygame.QUIT:
#Fechar jogo se o player clicar no X
            pygame.quit()
            sys.exit()
            game_on = False

#Alterar velocidade do sumo pra cada tecla.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sumo_sprite.speedx -= 2
            if event.key == pygame.K_RIGHT:
                sumo_sprite.speedx += 2

#Verificar se o player soltou alguma tecla e alterar velocidade do sumo pra cada tecla.
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                sumo_sprite.speedx += 2
            if event.key == pygame.K_RIGHT:
                sumo_sprite.speedx -= 2
    sprites.update()
#---------------------------------------------------------------------------------------------------
#Checar hit de bigorna, e se ir para tela de game over
    hit_bigorna = pygame.sprite.spritecollide(sumo_sprite, bigorna_sprite, True, pygame.sprite.collide_mask)
    for bigorna_sprite in hit_bigorna:     
        som_perdeu.play()
        time.sleep(1)
        game_on = False
#---------------------------------------------------------------------------------------------------
#Gerar outro sushi para cada sushi comido pelo sumo
    hit_sushi = pygame.sprite.spritecollide(sumo_sprite, sushi_sprite, True, pygame.sprite.collide_mask)
    for sushi in hit_sushi:
        som_comer.play()
        c1 = comidas(sushipng)
        score += 10               
        sprites.add(c1)     
        sushi_sprite.add(c1)
#---------------------------------------------------------------------------------------------------
#Gerar outro onigiri para cada onigiri comido pelo sumo
    hit_onigiri = pygame.sprite.spritecollide(sumo_sprite, onigiri_sprite, True, pygame.sprite.collide_mask) 
    for onigiri in hit_onigiri:
        som_comer.play()
        c2 = comidas(onigiripng)
        sprites.add(c2)
        onigiri_sprite.add(c2)
        score += 15
#---------------------------------------------------------------------------------------------------       
#Gerar outro lamen para cada lamen comido pelo sumo  
    hit_lamen = pygame.sprite.spritecollide(sumo_sprite, lamen_sprite, True, pygame.sprite.collide_mask)
    for lamen in hit_lamen:
        som_comer.play()
        c3 = comidas(lamenpng)
        sprites.add(c3)
        lamen_sprite.add(c3)
        score += 5
#---------------------------------------------------------------------------------------------------    
#Gerar outro doce para cada doce comido pelo sumo
    hit_doce = pygame.sprite.spritecollide(sumo_sprite, doce_sprite, True, pygame.sprite.collide_mask)    
    for doce in hit_doce:
        som_comer.play()
        c4 = comidas(docepng)
        sprites.add(c4)
        doce_sprite.add(c4)
        score += 20
#---------------------------------------------------------------------------------------------------    
#Colocar wallpaper do jogo na tela
    janela.fill((0,0,0))
    janela.blit(background, (0,0))
#---------------------------------------------------------------------------------------------------
#Colocar score do jogador na tela
    pontos_na_tela = fonte_pontos.render("{:01d}".format(score), True, (vermelho))
    janela.blit(pontos_na_tela,(400,0))
#---------------------------------------------------------------------------------------------------    
#Mostrar sprites na tela
    sprites.draw(janela)
    pygame.display.flip()
#---------------------------------------------------------------------------------------------------
#Gerar tela de game over ao perder
if game_on == False:
    gameoverscreen=pygame.image.load('Assets/game_over.png')
    janela.blit(gameoverscreen, (0,0))
    pontos_feitos=fonte_pontos_feitos.render("Nice! {:01d} points".format(score), True, (branco))
    game_over=fonte_game_over.render("Game Over", True, (vermelho))
    janela.blit(pontos_feitos,(0,350))
    janela.blit(game_over,(70,50))
    pygame.display.flip()
    time.sleep(3)

pygame.quit()