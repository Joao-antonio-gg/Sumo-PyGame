from assets import *

#FUNCÃO ANIMAÇÕES - COMER
comer_ativo = False
quanto_comeu = 0
conta_frame2 = 1
def SumoComendo():
    global quanto_comeu, conta_frame2, comer_ativo
    mudancas_por_segundo2 = 40
    janela.blit(background, (0, 0))
    if quanto_comeu >= 27 or quanto_comeu > 2:
        quanto_comeu = 0
    if comer_ativo:
        sumo_sprite.update_image(comer[quanto_comeu])
        if conta_frame2 % mudancas_por_segundo2 == 0:
            quanto_comeu += 1
    conta_frame2 += 1

#FUNÇÃO ANIMAÇÕES - CAMINHAR
qtde_passos = 0
caminha_esquerda = False
caminha_direita = False
conta_frame = 1
def redrawGameWindow():
    global qtde_passos, conta_frame
    #Se esse número aumenta, diminui a velocidade dos passos
    mudancas_por_segundo = 40  
    janela.blit(background, (0, 0))
    if qtde_passos >= 27 or qtde_passos > 2:
        qtde_passos = 0
    if caminha_direita: 
        sumo_sprite.update_image(direita[qtde_passos])
        if conta_frame % mudancas_por_segundo == 0:
            qtde_passos += 1
    elif caminha_esquerda:
        sumo_sprite.update_image(esquerda[qtde_passos])
        if conta_frame % mudancas_por_segundo == 0:
            qtde_passos += 1
    elif not caminha_esquerda and not caminha_direita and not comer_ativo:
        sumo_sprite.update_image(sumopng)
    conta_frame += 1
