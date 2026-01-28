import pygame
import sys
from interface import executar_menu_principal, executar_tela_vitoria
from config import criar_estado_inicial, processar_eventos_jogo, atualizar_estado_jogo, desenhar_jogo


pygame.init()
pygame.display.set_caption("Tapiocaria do Billy")
clock = pygame.time.Clock()
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))

programa_rodando = True

while programa_rodando:
    
    
    if not executar_menu_principal(tela, largura, altura):
        programa_rodando = False
        break 

    
    estado_jogo = criar_estado_inicial(largura, altura)
    jogando = True
    tempo_final_registrado = 0.0
    
    while jogando:
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                jogando = False
                programa_rodando = False 
        
      
        processar_eventos_jogo(estado_jogo, eventos)
        atualizar_estado_jogo(estado_jogo)
        desenhar_jogo(tela, estado_jogo)
        
        
        if estado_jogo["jogo_finalizado"]:
            tempo_final_registrado = estado_jogo["tempo_atual_s"]
            jogando = False 

        pygame.display.flip()
        clock.tick(60)

    
    if programa_rodando:
        if not executar_tela_vitoria(tela, tempo_final_registrado):
            programa_rodando = False

pygame.quit()
sys.exit()