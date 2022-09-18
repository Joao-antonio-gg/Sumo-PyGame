# from classes_FUNCOES import *
import funcoes_animacoes
from fontes_cores import *
from funcoes_animacoes import *
from assets import *


# Inicialização do Pygame
class In_Game:
    def __init__(self, sprite_list):
        self.contador0 = 0
        self.score = 0
        self.game_on = True
        self.bigorna_sprite = sprite_list[0]
        self.sushi_sprite = sprite_list[1]
        self.onigiri_sprite = sprite_list[2]
        self.lamen_sprite = sprite_list[3]
        self.doce_sprite = sprite_list[4]

    def gerar_comida(self, comida_png, comida_nome):
        comidadif = comidas(comida_png)
        sprites.add(comidadif)
        eval(str(comida_nome) + '_sprite.add(comidadif)')

    def tela_inicio(self):
        with open('Score.txt', 'r') as arquivo:
            conteudo = arquivo.read()
            lista_linhas = conteudo.split('\n')

            for linha in lista_linhas:
                valor_max = extractMaximum(linha)

        while True:
            inicio_screen = pygame.image.load('Assets/start.jpeg')
            janela.blit(inicio_screen, (0, 0))
            start_enter = fonte_start.render("Press ENTER to start", True, (branco))
            janela.blit(start_enter, (500, 600))
            high_score = fonte_high_score.render("HIGH SCORE: {0}".format(valor_max), True, (branco))
            janela.blit(high_score, (20, 400))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        self.in_game()
            pygame.display.flip()

    def in_game(self):
        # Gerar sushi
        self.gerar_comida(sushipng, 'sushi')
        # ---------------------------------------------------------------------------------------------------
        # Gerar onigiri
        self.gerar_comida(onigiripng, 'onigiri')
        # ---------------------------------------------------------------------------------------------------
        # Gerar lamen
        self.gerar_comida(lamenpng, 'lamen')
        # ---------------------------------------------------------------------------------------------------
        # Gerar doce
        self.gerar_comida(docepng, 'doce')
        while self.game_on:
            if self.contador0 > 80:
                self.contador0 = 0
            if self.contador0 > 0:
                self.contador0 += 1
                # funcoes_animacoes.comer_ativo = False
            # ---------------------------------------------------------------------------------------------------
            # Aumentar o número de bigornas a cada 100 pontos feitos
            if len(self.bigorna_sprite) < (self.score // 100 + 1):
                bigornadif = bigorna(bigornapng)
                sprites.add(bigornadif)
                self.bigorna_sprite.add(bigornadif)
            # ---------------------------------------------------------------------------------------------------
            eventos = pygame.event.get()
            for event in eventos:

                if event.type == pygame.QUIT:
                    # Fechar jogo se o player clicar no X
                    pygame.quit()
                    sys.exit()

                # Alterar velocidade do sumo pra cada tecla.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        sumo_sprite.speedx -= 2
                    elif event.key == pygame.K_RIGHT:
                        sumo_sprite.speedx += 2

                # Verificar se o player soltou alguma tecla e alterar velocidade do sumo pra cada tecla.
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        sumo_sprite.speedx += 2
                    if event.key == pygame.K_RIGHT:
                        sumo_sprite.speedx -= 2
            sprites.update()
            # ---------------------------------------------------------------------------------------------------
            # Checar hit de bigorna, e se ir para tela de game over
            hit_bigorna = pygame.sprite.spritecollide(sumo_sprite, self.bigorna_sprite, True,
                                                      pygame.sprite.collide_mask)
            if hit_bigorna:
                som_perdeu.play()
                time.sleep(1)
                sumo_sprite.speedx = 0
                sumo_sprite.speedy = 0
                sumo_sprite.rect.x = 500
                with open('Score.txt', 'r') as scores:
                    high_score_total = int(scores.read())
                if self.score > high_score_total:
                    with open('Score.txt', 'w') as arquivo_score:
                        arquivo_score.write(f'{self.score}')
                # main.state = 'TELA FINAL'
                self.tela_final()
            # ---------------------------------------------------------------------------------------------------
            # Gerar outro sushi para cada sushi comido pelo sumo
            hit_sushi = pygame.sprite.spritecollide(sumo_sprite, self.sushi_sprite, True, pygame.sprite.collide_mask)
            if hit_sushi:
                funcoes_animacoes.comer_ativo = True
                som_comer.play()
                self.gerar_comida(sushipng, 'sushi')
                self.score += 10
                self.contador0 += 1
            # ---------------------------------------------------------------------------------------------------
            # Gerar outro onigiri para cada onigiri comido pelo sumo
            hit_onigiri = pygame.sprite.spritecollide(sumo_sprite, self.onigiri_sprite, True,
                                                      pygame.sprite.collide_mask)
            if hit_onigiri:
                funcoes_animacoes.comer_ativo = True
                som_comer.play()
                self.gerar_comida(onigiripng, 'onigiri')
                self.score += 15
                self.contador0 += 1
            # ---------------------------------------------------------------------------------------------------
            # Gerar outro lamen para cada lamen comido pelo sumo
            hit_lamen = pygame.sprite.spritecollide(sumo_sprite, lamen_sprite, True, pygame.sprite.collide_mask)
            if hit_lamen:
                funcoes_animacoes.comer_ativo = True
                som_comer.play()
                self.gerar_comida(lamenpng, 'lamen')
                self.score += 5
                self.contador0 += 1
            # ---------------------------------------------------------------------------------------------------
            # Gerar outro doce para cada doce comido pelo sumo
            hit_doce = pygame.sprite.spritecollide(sumo_sprite, doce_sprite, True, pygame.sprite.collide_mask)
            if hit_doce:
                funcoes_animacoes.comer_ativo = True
                som_comer.play()
                self.gerar_comida(docepng, 'doce')
                self.score += 20
                self.contador0 += 1
            # ---------------------------------------------------------------------------------------------------
            # Colocar self.score do jogador na tela
            pontos_na_tela = fonte_pontos.render("{:01d}".format(self.score), True, (vermelho))
            janela.blit(pontos_na_tela, (400, 0))
            # ---------------------------------------------------------------------------------------------------
            # Mostrar sprites na tela
            sprites.draw(janela)
            pygame.display.flip()
            # ---------------------------------------------------------------------------------------------------
            SumoComendo()

    def tela_final(self):
        while self.game_on:
            eventos = pygame.event.get()
            for event in eventos:
                if event.type == pygame.QUIT:
                    # Fechar jogo se o player clicar no X
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_on = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        self.tela_inicio()
            janela.blit(pygame.image.load('Assets/game_over.png'), (0, 0))
            pontos_feitos = fonte_pontos_feitos.render(f"Nice! {self.score} points", True, (branco))
            game_over = fonte_game_over.render("Game Over", True, (vermelho))
            janela.blit(pontos_feitos, (0, 350))
            janela.blit(game_over, (70, 50))
            pygame.display.flip()
            pygame.display.flip()
