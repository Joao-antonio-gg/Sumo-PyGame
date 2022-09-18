import pygame

import assets
import jogo


pygame.init()
pygame.mixer.init()
largura=1024; altura=768
janela = pygame.display.set_mode((largura,altura))
#---------------------------------------------------------------------------------------------------
#Nome do jogo
pygame.display.set_caption("Sumo Eats")
#---------------------------------------------------------------------------------------------------
#Definir dimensões
#comida_largura = 60; comida_altura = 60; sumo_largura = 150; sumo_altura = 150; bigorna_altura = 80; bigorna_largura = 100
# ----- Gera tela principal
state = 'INIT'
while state != 'QUIT':
    if state == 'INIT':
        state = jogo.In_Game(assets.sprit_list)
        state.tela_inicio()
    # elif state == 'TELA FINAL':
    #     state = tela_final(window, assets)
    else:
        state = 'QUIT'

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

# gameoverscreen = pygame.image.load('Assets/game_over.png')
# janela.blit(gameoverscreen, (0, 0))
# pontos_feitos = fonte_pontos_feitos.render("Nice! {:01d} points".format(score), True, (branco))
#     game_over = fonte_game_over.render("Game Over", True, (vermelho))
#     janela.blit(pontos_feitos, (0, 350))
#     janela.blit(game_over, (70, 50))
#     pygame.display.flip()
# # Guardando o score
# with open('Score.txt', 'r') as scores:
#     high_score_total = int(scores.read())
# if high_score_total < score:
#     with open('Score.txt', 'w') as arquivo_score:
#         arquivo_score.write('{0}'.format(score))