import pygame
import sys
import os
from biblioteca import setPreencherRetanguloFloodfill

# --- CONFIGURAÇÕES DE CORES E FONTE ---
COR_FUNDO_MENU = (200, 220, 255)
COR_CONTORNO   = (0, 0, 0)
COR_TXT        = (0, 0, 0)

pygame.font.init()
fonte_ui = pygame.font.SysFont("Arial", 40, bold=True)
fonte_ranking = pygame.font.SysFont("Arial", 30, bold=False)

def getBotao(x, y, largura, altura, cor_fundo, texto):
    surf_texto = fonte_ui.render(texto, True, COR_TXT)
    txt_w, txt_h = surf_texto.get_size()
    
    txt_x = x + (largura - txt_w) // 2
    txt_y = y + (altura - txt_h) // 2

    return {
        "tipo": "botao",
        "x": x, "y": y,
        "w": largura, "h": altura,
        "cor": cor_fundo,
        "texto_surf": surf_texto,
        "txt_pos": (txt_x, txt_y)
    }

def desenhar_botao_customizado(tela, botao):
    setPreencherRetanguloFloodfill(
        tela,
        botao["x"], botao["y"],
        botao["w"], botao["h"],
        COR_CONTORNO, botao["cor"]
    )
    tela.blit(botao["texto_surf"], botao["txt_pos"])

def executar_menu_principal(tela, largura_tela, altura_tela):
    btn_jogar = getBotao(largura_tela//2 - 100, 300, 200, 80, (50, 200, 50), "JOGAR")
    btn_sair  = getBotao(largura_tela//2 - 100, 450, 200, 80, (200, 50, 50), "SAIR")
    
    clock = pygame.time.Clock()
    rodando_menu = True
    continuar = True 
    
    while rodando_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False 
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                
                if (mx >= btn_jogar["x"] and mx <= btn_jogar["x"] + btn_jogar["w"] and
                    my >= btn_jogar["y"] and my <= btn_jogar["y"] + btn_jogar["h"]):
                    return True 
                
                if (mx >= btn_sair["x"] and mx <= btn_sair["x"] + btn_sair["w"] and
                    my >= btn_sair["y"] and my <= btn_sair["y"] + btn_sair["h"]):
                    return False
        
        if continuar:
            tela.fill(COR_FUNDO_MENU)
            desenhar_botao_customizado(tela, btn_jogar)
            desenhar_botao_customizado(tela, btn_sair)
            pygame.display.flip()
            continuar = False
            
        clock.tick(60)

def gerenciar_ranking(novo_tempo):
    arquivo = "ranking.txt"
    tempos = []

    if os.path.exists(arquivo):
        with open(arquivo, "r") as f:
            for linha in f:
                try:
                    val = float(linha.strip())
                    tempos.append(val)
                except ValueError:
                    pass
    
    tempos.append(novo_tempo)
    tempos.sort()
    tempos = tempos[:5]

    with open(arquivo, "w") as f:
        for t in tempos:
            f.write(f"{t:.2f}\n")
            
    return tempos

def executar_tela_vitoria(tela, tempo_final):
    largura = tela.get_width()
    
    top_5 = gerenciar_ranking(tempo_final)

    txt_titulo = fonte_ui.render("ENTREGA CONCLUÍDA!", True, (0, 100, 0))
    txt_seu_tempo = fonte_ui.render(f"Seu Tempo: {tempo_final:.2f} s", True, (0, 0, 0))
    txt_rank_titulo = fonte_ui.render("--- MELHORES TEMPOS ---", True, (50, 50, 50))

    btn_voltar = getBotao(largura//2 - 250, 550, 500, 80, (100, 100, 255), "VOLTAR AO MENU")

    clock = pygame.time.Clock()
    rodando = True
    precisa_desenhar = True
    
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if (mx >= btn_voltar["x"] and mx <= btn_voltar["x"] + btn_voltar["w"] and
                    my >= btn_voltar["y"] and my <= btn_voltar["y"] + btn_voltar["h"]):
                    return True 
        
        if precisa_desenhar:
            tela.fill((240, 240, 220)) 
            
            tela.blit(txt_titulo, (largura//2 - txt_titulo.get_width()//2, 50))
            tela.blit(txt_seu_tempo, (largura//2 - txt_seu_tempo.get_width()//2, 120))
            tela.blit(txt_rank_titulo, (largura//2 - txt_rank_titulo.get_width()//2, 200))

            y_inicial = 260
            for i, tempo in enumerate(top_5):
                texto_rank = f"{i+1}º  -  {tempo:.2f} s"
                cor = (255, 0, 0) if abs(tempo - tempo_final) < 0.001 else (0, 0, 0)
                
                surf_rank = fonte_ranking.render(texto_rank, True, cor)
                tela.blit(surf_rank, (largura//2 - surf_rank.get_width()//2, y_inicial))
                y_inicial += 40

            desenhar_botao_customizado(tela, btn_voltar)
            
            pygame.display.flip()
            precisa_desenhar = False
            
        clock.tick(60)