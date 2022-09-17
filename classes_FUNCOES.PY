#Definir classe do sumo
from assets import *
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
def extractMaximum(ss): 
    num, res = 0, 0 
    for i in range(len(ss)): 
        if ss[i] >= "0" and ss[i] <= "9": 
            num = num * 10 + int(int(ss[i]) - 0) 
        else: 
            res = max(res, num) 
            num = 0 
    return max(res, num) 
