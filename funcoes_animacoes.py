from assets import *

#FUNCÃO ANIMAÇÕES - COMER
comer_ativo = False
quanto_comeu = 0
conta_frame2 = 1
def SumoComendo():
    global quanto_comeu, conta_frame2, comer_ativo
    mudancas_por_segundo2 = 40
    janela.blit(background, (0, 0))
    if comer_ativo:
        sumo_sprite.update_image(comer[quanto_comeu])
        if conta_frame2 % mudancas_por_segundo2 == 0:
            quanto_comeu += 1
    conta_frame2 += 1
    if quanto_comeu == 4:
        quanto_comeu = 0
        comer_ativo = False

#FUNÇÃO ANIMAÇÕES - CAMINHAR
qtde_passos = 0
caminha_esquerda = False
caminha_direita = False
conta_frame = 1
