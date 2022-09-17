import pygame
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
comida_largura = 60; comida_altura = 60; sumo_largura = 150; sumo_altura = 150; bigorna_altura = 80; bigorna_largura = 100
# ----- Gera tela principal

state = 'INIT'
while state != 'QUIT':
    if state == 'INIT':
        state = jogo.in_game()
    # elif state == TELA_FINAL:
    #     state = tela_final(window, assets)
    else:
        state = 'QUIT'

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados