import pygame
import sys
import os
from biblioteca import setPreencherRetanguloFloodfill

COR_FUNDO_MENU = (59, 58, 56)
COR_CONTORNO   = (0, 0, 0)
COR_TXT         = (255, 255, 255)

pygame.font.init()

try:
    fonte_titulo = pygame.font.Font("./Fontes/RubikDirt-Regular.ttf", 100)
except FileNotFoundError:
    print("Erro: Arquivo Oi-Regular.ttf não encontrado. Usando fonte padrão.")
    fonte_titulo = pygame.font.SysFont("Arial", 90, bold=True)

#Fonte para os botões
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
    #Usa a função da sua biblioteca para preencher com Floodfill
    setPreencherRetanguloFloodfill(tela, botao["x"], botao["y"], botao["w"], botao["h"], COR_CONTORNO, botao["cor"])
    #Desenha o texto por cima
    tela.blit(botao["texto_surf"], botao["txt_pos"])

def executar_menu_principal(tela, largura_tela, altura_tela):

    surf_titulo = fonte_titulo.render("TAPIOCARIA DO BILLY", True, COR_TXT)
    rect_titulo = surf_titulo.get_rect(center=(largura_tela // 2, 150))

    btn_jogar = getBotao(largura_tela//2 - 100, 320, 200, 80, (103, 173, 57), "JOGAR")
    btn_sair   = getBotao(largura_tela//2 - 100, 470, 200, 80, (196, 72, 39), "SAIR")
    
    rect_jogar = pygame.Rect(btn_jogar["x"], btn_jogar["y"], btn_jogar["w"], btn_jogar["h"])
    rect_sair = pygame.Rect(btn_sair["x"], btn_sair["y"], btn_sair["w"], btn_sair["h"])

    clock = pygame.time.Clock()
    rodando_menu = True
    
    while rodando_menu:
        mx, my = pygame.mouse.get_pos()
        
        if rect_jogar.collidepoint(mx, my) or rect_sair.collidepoint(mx, my):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) #reseta o cursor
                return False 
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_jogar.collidepoint(mx, my):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) #reseta o cursor
                    return True 
                
                if rect_sair.collidepoint(mx, my):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) #reseta o cursor
                    return False

        tela.fill(COR_FUNDO_MENU)
        tela.blit(surf_titulo, rect_titulo)
        
        desenhar_botao_customizado(tela, btn_jogar)
        desenhar_botao_customizado(tela, btn_sair)
        
        pygame.display.flip()
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