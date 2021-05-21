#Importando bibliotecas
import pygame
import random
import sys
import time

#Iniciando Pygame
pygame.init()

#Definindo janela
largura=1024
altura=768
janela = pygame.display.set_mode((largura,altura))

#Nome do jogo
pygame.display.set_caption("Sumo Eats")

#Importar imagens
sumopng = pygame.image.load('Assets/sumo_parado.png')
bigornapng = pygame.image.load('Assets/bigorna.png')
onigiripng = pygame.image.load('Assets/onigiri.png')
sushipng = pygame.image.load('Assets/sushi.png')
lamenpng = pygame.image.load('Assets/lamen.png')
docepng = pygame.image.load('Assets/doce.png')

comida_largura = 60
comida_altura = 60
sumo_largura = 200
sumo_altura = 200
bigorna_altura = 80
bigorna_largura = 100

assets = {}
#Importar animações
direita = [pygame.image.load('Assets/d0.png'), pygame.image.load('Assets/d1.png'), pygame.image.load('Assets/d2.png')]
esquerda = [pygame.image.load('Assets/e0.png'), pygame.image.load('Assets/e1.png'), pygame.image.load('Assets/e2.png')]
comer = [pygame.image.load('Assets/c0.png'), pygame.image.load('Assets/c1.png'), pygame.image.load('Assets/c2.png'), pygame.image.load('Assets/c3.png'), pygame.image.load('Assets/c4.png')]
morrer = [pygame.image.load('Assets/m1.png'), pygame.image.load('Assets/m2.png'), pygame.image.load('Assets/m3.png'), pygame.image.load('Assets/m4.png'), pygame.image.load('Assets/m5.png')]
background = [pygame.image.load('Assets/frame-001.png'), pygame.image.load('Assets/frame-002.png'), pygame.image.load('Assets/frame-003.png'), pygame.image.load('Assets/frame-004.png'), pygame.image.load('Assets/frame-005.png'), pygame.image.load('Assets/frame-006.png'), pygame.image.load('Assets/frame-007.png'), pygame.image.load('Assets/frame-008.png'), pygame.image.load('Assets/frame-009.png'), pygame.image.load('Assets/frame-010.png'), pygame.image.load('Assets/frame-011.png'), pygame.image.load('Assets/frame-012.png'), pygame.image.load('Assets/frame-013.png'), pygame.image.load('Assets/frame-014.png'), pygame.image.load('Assets/frame-015.png'), pygame.image.load('Assets/frame-016.png'), pygame.image.load('Assets/frame-017.png'), pygame.image.load('Assets/frame-018.png'), pygame.image.load('Assets/frame-019.png'), pygame.image.load('Assets/frame-020.png'), pygame.image.load('Assets/frame-021.png'), pygame.image.load('Assets/frame-022.png'), pygame.image.load('Assets/frame-023.png'), pygame.image.load('Assets/frame-024.png'), pygame.image.load('Assets/frame-025.png'), pygame.image.load('Assets/frame-026.png'), pygame.image.load('Assets/frame-027.png'), pygame.image.load('Assets/frame-028.png'), pygame.image.load('Assets/frame-029.png'), pygame.image.load('Assets/frame-030.png'), pygame.image.load('Assets/frame-031.png'), pygame.image.load('Assets/frame-032.png'), pygame.image.load('Assets/frame-033.png'), pygame.image.load('Assets/frame-034.png'), pygame.image.load('Assets/frame-035.png'), pygame.image.load('Assets/frame-036.png'), pygame.image.load('Assets/frame-037.png'), pygame.image.load('Assets/frame-038.png'), pygame.image.load('Assets/frame-039.png'), pygame.image.load('Assets/frame-040.png'), pygame.image.load('Assets/frame-041.png'), pygame.image.load('Assets/frame-042.png'), pygame.image.load('Assets/frame-043.png'), pygame.image.load('Assets/frame-044.png'), pygame.image.load('Assets/frame-045.png'), pygame.image.load('Assets/frame-046.png'), pygame.image.load('Assets/frame-047.png'), pygame.image.load('Assets/frame-048.png'), pygame.image.load('Assets/frame-049.png')]

#Importar sons
som_comer = pygame.mixer.Sound('Assets/comer.mp3')
som_pontos = pygame.mixer.Sound('Assets/checkpoint.mp3')
som_perdeu = pygame.mixer.Sound('Assets/lose.mp3')
musica = pygame.mixer.music.load('Assets/musica.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

assets["fonte_pontos"] = pygame.font.Font('Assets/fonte_sumo.ttf', 28)
assets["fonte_gameover"] = pygame.font.Font('Assets/gameoverfont.ttf', 28)


onigiripng = pygame.transform.scale(onigiripng, (comida_largura, comida_altura))
lamenpng = pygame.transform.scale(lamenpng, (comida_largura, comida_altura))
docepng = pygame.transform.scale(docepng, (comida_largura, comida_altura))
sushipng = pygame.transform.scale(sushipng, (comida_largura, comida_altura))
sumopng = pygame.transform.scale(sumopng, (sumo_largura, sumo_altura))
bigornapng = pygame.transform.scale(bigornapng, (bigorna_largura, bigorna_altura))

class sumo(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura / 2
        self.rect.bottom = altura - 10
        self.speedx = 0
        self.mask = pygame.mask.from_surface(sumopng)

    def update(self):
    # Atualização da posição do boneco
        self.rect.x += self.speedx
 
    # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0

class comidas(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
 
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura - comida_largura)
        self.rect.y = random.randint(-100, - comida_altura)
        self.speedy = random.randint(2, 5)
        self.mask = pygame.mask.from_surface(onigiripng)
        self.mask = pygame.mask.from_surface(sushipng)
        self.mask = pygame.mask.from_surface(lamenpng)
        self.mask = pygame.mask.from_surface(docepng)
    def update(self):
        # Atualizando a posição da fruta 
        self.rect.y += self.speedy
        # Se a fruta passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > altura or self.rect.right < 0 or self.rect.left > largura:
            self.rect.x = random.randint(0, largura-comida_largura)
            self.rect.y = random.randint(-100, -comida_altura)
            self.speedy = random.randint(2, 5)
        
class bigorna(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
 
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura - comida_largura)
        self.rect.y = random.randint(-100, - comida_largura)
        self.speedy = random.randint(2, 5)
        self.mask = pygame.mask.from_surface(bigornapng)
    def update(self):
        # Atualizando a posição da bigorna  
        self.rect.y += self.speedy
        # Se a bigorna passar do final da tela, volta para cima e sorteia novas posições e velocidades
        if self.rect.top > altura or self.rect.right < 0 or self.rect.left > largura:
            self.rect.x = random.randint(0, largura - comida_largura)
            self.rect.y = random.randint(-100, - comida_largura)
            self.speedy = random.randint(2, 5)

clock = pygame.time.Clock()
FPS = 144

jogo_on = True

#criando grupo 
sprites = pygame.sprite.Group()
onigiri_sprite = pygame.sprite.Group()
sushi_sprite = pygame.sprite.Group()
doce_sprite = pygame.sprite.Group()
lamen_sprite = pygame.sprite.Group()
bigorna_sprite = pygame.sprite.Group()
sumo_sprite = sumo(sumopng)
sprites.add(sumo_sprite)
#cria sushi
for i in range(1):
    sushidif = comidas(sushipng)
    sprites.add(sushidif)
    sushi_sprite.add(sushidif)

#cria onigiri
for i in range(1):
    onigiridif = comidas(onigiripng)
    sprites.add(onigiridif)
    onigiri_sprite.add(onigiridif)
    
#cria lamen
for i in range(1):
    lamendif = comidas(lamenpng)
    sprites.add(lamendif)
    lamen_sprite.add(lamendif)
    
#cria doce
for i in range(1):
    docedif = comidas(docepng)
    sprites.add(docedif)
    doce_sprite.add(docedif)

#---------------------------------------------------------------------------------------------------------------
##ESPACO PONTUACAO TELA INICIAL
#contador da pontuação
score = 0
#Toca a música e deixa em um loop infinito
pygame.mixer.music.play(-1)

black=(0,0,0)
end_it=False

#cria tela de início
while (end_it==False):
    startscreen=pygame.image.load('Assets/start.jpeg')
    janela.blit(startscreen, (0,0))
    fontestart=pygame.font.SysFont("Consolas", 45)
    start_enter=fontestart.render("Press ENTER to start", 1, (255, 255, 255))

    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                end_it=True
    janela.blit(start_enter,(500,600))
    pygame.display.flip()
#---------------------------------------------------------------------------------------------------------------
game_on = True
while game_on:
#aumenta o número de bigornas a cada 100 pontos
    if len(bigorna_sprite.sprites()) < (score//100 + 1):
        bigornadif = bigorna(bigornapng)
        sprites.add(bigornadif)
        bigorna_sprite.add(bigornadif)

    clock.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            game_on = False
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                sumo_sprite.speedx -= 4
            if event.key == pygame.K_RIGHT:
                sumo_sprite.speedx += 4
            # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                sumo_sprite.speedx += 4
            if event.key == pygame.K_RIGHT:
                sumo_sprite.speedx -= 4

    sprites.update()

    # Verifica se houve contato entre o player e a bomba
    hits = pygame.sprite.spritecollide(sumo_sprite, bigorna_sprite, True, pygame.sprite.collide_mask)
    for bigorna_sprite in hits:     
        som_perdeu.play()
        time.sleep(1)
        game_on = False

    hits2 = pygame.sprite.spritecollide(sumo_sprite, sushi_sprite, True, pygame.sprite.collide_mask)
    hits3 = pygame.sprite.spritecollide(sumo_sprite, onigiri_sprite, True, pygame.sprite.collide_mask) 
    hits4 = pygame.sprite.spritecollide(sumo_sprite, lamen_sprite, True, pygame.sprite.collide_mask)
    hits5 = pygame.sprite.spritecollide(sumo_sprite, doce_sprite, True, pygame.sprite.collide_mask) 

    #gera um novo sushi para cada hit
    for sushi in hits2:
        som_comer.play()
        c1 = comidas(sushipng)
        score += 10               
        sprites.add(c1)     
        sushi_sprite.add(c1)

    #gera um novo onigiri para cada hit
    for onigiri in hits3:
        som_comer.play()
        c2 = comidas(onigiripng)
        sprites.add(c2)
        onigiri_sprite.add(c2)
        score += 15
        
    #gera uma novo lamen para cada hit    
    for lamen in hits4:
        som_comer.play()
        c3 = comidas(lamenpng)
        sprites.add(c3)
        lamen_sprite.add(c3)
        score += 5
    
    #gera um novo doce para cada hit    
    for doce in hits5:
        som_comer.play()
        c4 = comidas(docepng)
        sprites.add(c4)
        doce_sprite.add(c4)
        score += 20

    janela.fill((0,0,0))
    #adiciona o score na tela
    text_surface = assets['fonte_pontos'].render("{:01d}".format(score), True, (255, 255, 0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (largura / 2,  10)
    janela.blit(text_surface, text_rect)
    
    sprites.draw(janela)
 
    pygame.display.flip()
    #-------------------------------------------------------

#finalização
listascore = []
listascore.append(score)
#cria tela de encerramento do jogo
if game_on == False:
    gameoverscreen=pygame.image.load('Assets/game_over.png')
    janela.blit(gameoverscreen, (0,0))
    fontepontosfeitos=pygame.font.SysFont("Britannic Bold", 80)
    fontegameover=pygame.font.Font('Assets/gameoverfont.ttf', 100)
    pontos_feitos=fontepontosfeitos.render("Você fez {:01d} pontos".format(score), 1, (255, 255, 255))
    game_over=fontegameover.render("Game Over", 1, (255, 0, 0))
    janela.blit(pontos_feitos,(110,450))
    janela.blit(game_over,(90,300))
    pygame.display.flip()
    time.sleep(3)

pygame.quit()
