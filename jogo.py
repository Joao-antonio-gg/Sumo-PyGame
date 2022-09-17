from assets import *
from classes_FUNCOES import *
from fontes_cores import *
from funcoes_animacoes import *
def in_game():
    while game_on:
        if contador0 > 80:
            contador0 = 0
            comer_ativo = False
        if contador0 > 0:
            contador0 += 1
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
                    caminha_direita = False
                    caminha_esquerda = True
                elif event.key == pygame.K_RIGHT:
                    sumo_sprite.speedx += 2
                    caminha_direita = True
                    caminha_esquerda = False

    #Verificar se o player soltou alguma tecla e alterar velocidade do sumo pra cada tecla.
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    caminha_esquerda = False
                    sumo_sprite.speedx += 2
                if event.key == pygame.K_RIGHT:
                    caminha_direita = False
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
        if hit_sushi:
            comer_ativo = True
            som_comer.play()
            c1 = comidas(sushipng)
            score += 10               
            sprites.add(c1)     
            sushi_sprite.add(c1)
            contador0 += 1
    #---------------------------------------------------------------------------------------------------
    #Gerar outro onigiri para cada onigiri comido pelo sumo
        hit_onigiri = pygame.sprite.spritecollide(sumo_sprite, onigiri_sprite, True, pygame.sprite.collide_mask) 
        if hit_onigiri:
            comer_ativo = True
            som_comer.play()
            c2 = comidas(onigiripng)
            sprites.add(c2)
            onigiri_sprite.add(c2)
            score += 15
            contador0 += 1
    #---------------------------------------------------------------------------------------------------       
    #Gerar outro lamen para cada lamen comido pelo sumo  
        hit_lamen = pygame.sprite.spritecollide(sumo_sprite, lamen_sprite, True, pygame.sprite.collide_mask)
        if hit_lamen:
            comer_ativo = True
            som_comer.play()
            c3 = comidas(lamenpng)
            sprites.add(c3)
            lamen_sprite.add(c3)
            score += 5
            contador0 += 1
    #---------------------------------------------------------------------------------------------------    
    #Gerar outro doce para cada doce comido pelo sumo
        hit_doce = pygame.sprite.spritecollide(sumo_sprite, doce_sprite, True, pygame.sprite.collide_mask)    
        if hit_doce:
            comer_ativo = True
            som_comer.play()
            c4 = comidas(docepng)
            sprites.add(c4)
            doce_sprite.add(c4)
            score += 20
            contador0 += 1
    #---------------------------------------------------------------------------------------------------    
    #Colocar wallpaper do jogo na tela
        # janela.fill((0,0,0))
        # janela.blit(background, (0,0))
    #---------------------------------------------------------------------------------------------------
    #Colocar score do jogador na tela
        pontos_na_tela = fonte_pontos.render("{:01d}".format(score), True, (vermelho))
        janela.blit(pontos_na_tela,(400,0))
    #---------------------------------------------------------------------------------------------------    
    #Mostrar sprites na tela
        sprites.draw(janela)
        pygame.display.flip()
    #---------------------------------------------------------------------------------------------------   
        redrawGameWindow()
        SumoComendo()