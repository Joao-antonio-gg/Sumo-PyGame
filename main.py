import pygame
from Constantes import WIDTH, HEIGHT, INIT, INSTRUCOES, GAME, QUIT, GAME_2, HISTORIA, GAME_3, GAME_4, TELA_FINAL
from game_screen_1 import game_screen, game_screen_2, game_screen_3, game_screen_4, load_assets
from init_screen import tela_inicial
from instrucoes import regras
from Tela_adicionais import tela_das_hist, tela_final
import jogo


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo')
#Assets
assets = load_assets()

state = INIT
while state != QUIT:
    if state == INIT:
        state = jogo.game(window,assets)
    elif state == INSTRUCOES:
        state = regras(window,assets)
    elif state == HISTORIA:
        state = tela_das_hist(window,assets)
    elif state == GAME:
        state = game_screen(window,assets)
    elif state == GAME_2:
        state = game_screen_2(window,assets)
    elif state == GAME_3:
        state = game_screen_3(window,assets)
    elif state == GAME_4:
        state = game_screen_4(window, assets)
    elif state == TELA_FINAL:
        state = tela_final(window, assets)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados