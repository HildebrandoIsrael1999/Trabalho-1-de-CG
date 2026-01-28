import pygame
import sys
import os
import math
from biblioteca import setPreencherRetanguloFloodfill, renderizarPersonagem
from personagens import getBilly
from cenarios import getTapioca, getQueijo
from matrizes import calcularMatriz, translacao, multiplicaMatrizes

# --- CONFIGURAÇÕES ---
COR_FUNDO_MENU = (59, 58, 56)
COR_CONTORNO   = (0, 0, 0)
COR_TXT        = (255, 255, 255)

pygame.font.init()

try:
    fonte_titulo = pygame.font.Font("./Fontes/RubikDirt-Regular.ttf", 100)
except FileNotFoundError:
    fonte_titulo = pygame.font.SysFont("Arial", 90, bold=True)

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
    setPreencherRetanguloFloodfill(tela, botao["x"], botao["y"], botao["w"], botao["h"], COR_CONTORNO, botao["cor"])
    tela.blit(botao["texto_surf"], botao["txt_pos"])

def verifica_colisao_botao(mx, my, botao):
    return (mx >= botao["x"] and mx <= botao["x"] + botao["w"] and
            my >= botao["y"] and my <= botao["y"] + botao["h"])


def executar_menu_principal(tela, largura_tela, altura_tela):
    surf_titulo = fonte_titulo.render("TAPIOCARIA DO BILLY", True, COR_TXT)
    rect_titulo = surf_titulo.get_rect(center=(largura_tela // 2, 100))

    btn_jogar = getBotao(largura_tela//2 - 100, 500, 200, 80, (103, 173, 57), "JOGAR")
    btn_sair  = getBotao(largura_tela//2 - 100, 600, 200, 80, (196, 72, 39), "SAIR")
    
    clock = pygame.time.Clock()
    rodando_menu = True
    
 
    billy_menu_x = 90
    billy_menu_y = 300                    
    billy_escala_atual = 0.1
    billy_escala_final = 5.0
    escala_velocidade = 0.12
    billy_angulo_atual = 0
    voltas_totais = 3
    total_crescimento = billy_escala_final - billy_escala_atual
    total_frames = total_crescimento / escala_velocidade
    angulo_velocidade = (360 * voltas_totais) / total_frames

    
    tapioca_x = 1000
    tapioca_y = 450
    tapioca_scale = 4.0  
    tapioca_angulo = 0   

    
    ajuste_local_x = -13 
    ajuste_local_y = -6

    while rodando_menu:
        mx, my = pygame.mouse.get_pos()
        
        
        colidiu_jogar = verifica_colisao_botao(mx, my, btn_jogar)
        colidiu_sair = verifica_colisao_botao(mx, my, btn_sair)

        if colidiu_jogar or colidiu_sair:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                return False 
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if colidiu_jogar:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    return True 
                
                if colidiu_sair:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    return False

        
        if billy_escala_atual < billy_escala_final:
            billy_escala_atual += escala_velocidade
            billy_angulo_atual += angulo_velocidade
        else:
            billy_escala_atual = billy_escala_final
            billy_angulo_atual = 0

        
        tapioca_angulo -= 2 

        
        tela.fill(COR_FUNDO_MENU)
        tela.blit(surf_titulo, rect_titulo)

        m_billy_menu = calcularMatriz(billy_escala_atual, billy_angulo_atual, billy_menu_x, billy_menu_y)
        renderizarPersonagem(tela, getBilly(), m_billy_menu, None)
        
        
        m_tapioca = calcularMatriz(tapioca_scale, tapioca_angulo, tapioca_x, tapioca_y)
        m_ajuste = translacao(ajuste_local_x, ajuste_local_y)
        m_queijo = multiplicaMatrizes(m_tapioca, m_ajuste)
        
        renderizarPersonagem(tela, getTapioca(largura=30, altura=15), m_tapioca, None)
        renderizarPersonagem(tela, getQueijo(), m_queijo, None)

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
        mx, my = pygame.mouse.get_pos()
        
        colidiu_voltar = verifica_colisao_botao(mx, my, btn_voltar)
        
        if colidiu_voltar:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                return False
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if colidiu_voltar:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    return True # Retorna True para voltar ao loop do menu
        
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