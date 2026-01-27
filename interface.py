import pygame
import sys
from biblioteca import setPreencherRetanguloFloodfill

# --- CONFIGURAÇÕES DE CORES E FONTE ---
COR_FUNDO_MENU = (200, 220, 255)
COR_CONTORNO   = (0, 0, 0)
COR_TXT        = (0, 0, 0)

pygame.font.init()
# Fonte Arial tamanho 40 e Negrito
fonte_ui = pygame.font.SysFont("Arial", 40, bold=True)

def getBotao(x, y, largura, altura, cor_fundo, texto):
    """
    Cria a estrutura de dados do botão e centraliza o texto dentro dele.
    """
    surf_texto = fonte_ui.render(texto, True, COR_TXT)
    txt_w, txt_h = surf_texto.get_size()
    
    # Cálculo para centralizar o texto no botão
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
    """
    Desenha o retângulo usando o Floodfill da sua biblioteca e coloca o texto por cima.
    """
    setPreencherRetanguloFloodfill(
        tela,
        botao["x"], botao["y"],
        botao["w"], botao["h"],
        COR_CONTORNO, botao["cor"]
    )
    tela.blit(botao["texto_surf"], botao["txt_pos"])

def executar_menu_principal(tela, largura_tela, altura_tela):
    """
    Loop do Menu Principal.
    """
    # Botões do Menu Principal
    btn_jogar = getBotao(largura_tela//2 - 100, 300, 200, 80, (50, 200, 50), "JOGAR")
    btn_sair  = getBotao(largura_tela//2 - 100, 450, 200, 80, (200, 50, 50), "SAIR")
    
    clock = pygame.time.Clock()
    rodando_menu = True
    continuar = True # Flag para desenhar apenas uma vez (otimização do floodfill)
    
    while rodando_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False 
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                
                # Clique no JOGAR
                if (mx >= btn_jogar["x"] and mx <= btn_jogar["x"] + btn_jogar["w"] and
                    my >= btn_jogar["y"] and my <= btn_jogar["y"] + btn_jogar["h"]):
                    return True 
                
                # Clique no SAIR
                if (mx >= btn_sair["x"] and mx <= btn_sair["x"] + btn_sair["w"] and
                    my >= btn_sair["y"] and my <= btn_sair["y"] + btn_sair["h"]):
                    return False
        
        # Desenho
        if continuar:
            tela.fill(COR_FUNDO_MENU)
            desenhar_botao_customizado(tela, btn_jogar)
            desenhar_botao_customizado(tela, btn_sair)
            pygame.display.flip()
            continuar = False
            
        clock.tick(60)

def executar_tela_vitoria(tela, tempo_final):
    """
    Exibe a tela de finalização com o tempo.
    """
    largura = tela.get_width()
    
    # Textos de Vitória
    txt_titulo = fonte_ui.render("ENTREGA CONCLUÍDA!", True, (0, 100, 0))
    txt_tempo = fonte_ui.render(f"Seu Tempo: {tempo_final:.2f} segundos", True, (0, 0, 0))
    
    # --- AQUI FOI A MUDANÇA ---
    # Aumentei a largura de 300 para 400 e ajustei o X (largura//2 - 200) para manter centralizado
    btn_voltar = getBotao(largura//2 - 200, 450, 400, 80, (100, 100, 255), "VOLTAR AO MENU")

    clock = pygame.time.Clock()
    rodando = True
    precisa_desenhar = True
    
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False # Fecha o jogo
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                # Verifica clique no botão VOLTAR
                if (mx >= btn_voltar["x"] and mx <= btn_voltar["x"] + btn_voltar["w"] and
                    my >= btn_voltar["y"] and my <= btn_voltar["y"] + btn_voltar["h"]):
                    return True # Volta para o loop do menu na main
        
        if precisa_desenhar:
            tela.fill((240, 240, 220)) # Fundo creme
            
            # Desenha Textos
            tela.blit(txt_titulo, (largura//2 - txt_titulo.get_width()//2, 200))
            tela.blit(txt_tempo, (largura//2 - txt_tempo.get_width()//2, 300))
            
            # Desenha Botão
            desenhar_botao_customizado(tela, btn_voltar)
            
            pygame.display.flip()
            precisa_desenhar = False
            
        clock.tick(60)