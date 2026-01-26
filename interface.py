import pygame
from biblioteca import setPreencherRetanguloFloodfill

COR_FUNDO_MENU = (200, 220, 255)
COR_CONTORNO   = (0, 0, 0)
COR_TXT        = (0, 0, 0)

pygame.font.init()
fonte_ui = pygame.font.SysFont("Arial", 40, bold=True)

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
    setPreencherRetanguloFloodfill(tela,botao["x"], botao["y"],botao["w"], botao["h"],COR_CONTORNO, botao["cor"])
    
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
                return False # 
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                
                if (mx >= btn_jogar["x"] and mx <= btn_jogar["x"] + btn_jogar["w"] and
                    my >= btn_jogar["y"] and my <= btn_jogar["y"] + btn_jogar["h"]):
                    return True 
                
                # Colisão Botão SAIR
                if (mx >= btn_sair["x"] and mx <= btn_sair["x"] + btn_sair["w"] and
                    my >= btn_sair["y"] and my <= btn_sair["y"] + btn_sair["h"]):
                    return False # Sinaliza para fechar
        
        if continuar:
            tela.fill(COR_FUNDO_MENU)
            
            desenhar_botao_customizado(tela, btn_jogar)
            desenhar_botao_customizado(tela, btn_sair)
            
            pygame.display.flip()
            continuar = False
            
        clock.tick(60)