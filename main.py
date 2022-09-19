import pygame
import assets
import jogo

pygame.init()
pygame.mixer.init()
largura = 1024
altura = 768
janela = pygame.display.set_mode((largura, altura))
# ---------------------------------------------------------------------------------------------------
# Nome do jogo
pygame.display.set_caption("Sumo Eats")


# ---------------------------------------------------------------------------------------------------
# Gera tela principal
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
