import pygame
import math
from biblioteca import *
from personagens import *
from matrizes import *
from cenarios import *
from interacoes import *
from colisao import GerenciadorColisao
from textos import *

#CONFIGURAÇÕES VISUAIS DA UI 
BTN_INSTR_X, BTN_INSTR_Y = 1050, 650
BTN_INSTR_W, BTN_INSTR_H = 200, 50

MODAL_X, MODAL_Y = 340, 160
MODAL_W, MODAL_H = 600, 400
BTN_FECHAR_TAM = 40

#INICIALIZAÇÃO DOS DADOS
def criar_estado_inicial(largura, altura):
    try:
        img_bandeira = pygame.image.load("bandeira.png").convert()
    except:
        img_bandeira = pygame.Surface((100, 100))
        img_bandeira.fill((255, 0, 255))

    return {
        "largura": largura, 
        "altura": altura,
        "colisor": GerenciadorColisao(DADOS_DO_CENARIO),
        "matriz_vp": calcularMatrizViewport(960, 20, 1260, 190, 1280, 720),
        "img_bandeira": img_bandeira,
        
        "tempo_inicio": pygame.time.get_ticks(),
        "tempo_atual_s": 0.0,
        "jogo_finalizado": False, 
        "mostrando_instrucoes": False,

        "billy_x": 270, "billy_y": 330,
        "billy_escala": 1.0, "billy_angulo": 0,
        "billy_tem_queijo": False,
        "tapioca_recheada": False,

        "clara_x": 100, "clara_y": 590,
        "clara_escala": 0.9, "clara_angulo": 0,
        "clara_velocidade": 7,
        "clara_destino_x": 50, "clara_destino_y": 380,
        "clara_chegou": False,
        "clara_recebeu_pedido": False,
        "clara_foi_embora": False,

        "menino_x": 200, "menino_y": 590,
        "menino_escala": 1.0, "menino_angulo": 0,
        
        "matrizes": {} 
    }

# --- INPUTS ---
def processar_eventos_jogo(estado, eventos):
    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            if estado["mostrando_instrucoes"]:
                bx = MODAL_X + MODAL_W - BTN_FECHAR_TAM - 10
                by = MODAL_Y + 10
                if (mx >= bx and mx <= bx + BTN_FECHAR_TAM and
                    my >= by and my <= by + BTN_FECHAR_TAM):
                    estado["mostrando_instrucoes"] = False
            else:
                if (mx >= BTN_INSTR_X and mx <= BTN_INSTR_X + BTN_INSTR_W and
                    my >= BTN_INSTR_Y and my <= BTN_INSTR_Y + BTN_INSTR_H):
                    estado["mostrando_instrucoes"] = True

        if evento.type == pygame.KEYDOWN and not estado["mostrando_instrucoes"]:
            if evento.key == pygame.K_SPACE:
                bx, by = estado["billy_x"], estado["billy_y"]
                cx, cy = estado["clara_x"], estado["clara_y"]
                
                if not estado["billy_tem_queijo"] and not estado["tapioca_recheada"] and not estado["clara_recebeu_pedido"]:
                    if pode_pegar_queijo(bx, by):
                        estado["billy_tem_queijo"] = True
                elif estado["billy_tem_queijo"]:
                    if pode_colocar_queijo(bx, by):
                        estado["billy_tem_queijo"] = False
                        estado["tapioca_recheada"] = True
                elif estado["tapioca_recheada"]:
                    if pode_entregar_tapioca(bx, by, cx, cy):
                        estado["tapioca_recheada"] = False
                        estado["clara_recebeu_pedido"] = True

def atualizar_estado_jogo(estado):
    if estado["mostrando_instrucoes"]:
        return 

    tempo_agora = pygame.time.get_ticks()

    if not estado["jogo_finalizado"]:
        diferenca_ms = tempo_agora - estado["tempo_inicio"]
        estado["tempo_atual_s"] = diferenca_ms / 1000.0

    teclas = pygame.key.get_pressed()
    dx, dy = 0, 0
    if teclas[pygame.K_a]: dx -= 20
    if teclas[pygame.K_d]: dx += 20
    if teclas[pygame.K_w]: dy -= 20  
    if teclas[pygame.K_s]: dy += 20 
    
    if not estado["clara_foi_embora"]:
        if not estado["clara_chegou"]:
            estado["clara_x"], estado["clara_y"], estado["clara_chegou"] = mover_npc_para_alvo(
                estado["clara_x"], estado["clara_y"], 
                estado["clara_destino_x"], estado["clara_destino_y"], 
                estado["clara_velocidade"]
            )
        else:
            estado["clara_angulo"] = 0
            if estado["clara_recebeu_pedido"]:
                if estado["clara_destino_x"] != -150:
                    estado["clara_destino_x"] = -150
                    estado["clara_chegou"] = False 
                elif estado["clara_destino_x"] == -150:
                    estado["clara_foi_embora"] = True
                    estado["jogo_finalizado"] = True 

    if estado["clara_x"] <= -140:
        estado["jogo_finalizado"] = True

    m_clara_t = calcularMatriz(estado["clara_escala"], estado["clara_angulo"], estado["clara_x"], estado["clara_y"])
    m_menino_t = calcularMatriz(estado["menino_escala"], estado["menino_angulo"], estado["menino_x"], estado["menino_y"])
    
    obstaculos = [
        get_aabb(getMulher(), m_clara_t),
        get_aabb(getMenino(), m_menino_t)
    ]
    
    novo_x = estado["billy_x"] + dx
    novo_y = estado["billy_y"] + dy
    if not estado["colisor"].verificarMovimento(getBilly(), novo_x, novo_y, estado["billy_escala"], estado["billy_angulo"], obstaculos):
        estado["billy_x"] = novo_x
        estado["billy_y"] = novo_y
        estado["billy_x"], estado["billy_y"] = limitar_personagem_na_janela(estado["billy_x"], estado["billy_y"], 40, 110, 
            estado["largura"], estado["altura"])

    estado["matrizes"]["billy"] = calcularMatriz(estado["billy_escala"], estado["billy_angulo"], estado["billy_x"], estado["billy_y"])
    estado["matrizes"]["clara"] = calcularMatriz(estado["clara_escala"], estado["clara_angulo"], estado["clara_x"], estado["clara_y"])
    estado["matrizes"]["menino"] = calcularMatriz(estado["menino_escala"], estado["menino_angulo"], estado["menino_x"], estado["menino_y"])
    
    if estado["clara_recebeu_pedido"]:
        estado["matrizes"]["queijo"] = get_matriz_queijo_clara(estado["clara_x"], estado["clara_y"])
        estado["matrizes"]["tapioca"] = get_matriz_tapioca_clara(estado["clara_x"], estado["clara_y"])
    else:
        estado["matrizes"]["tapioca"] = get_matriz_tapioca_mesa()
        if estado["tapioca_recheada"]:
            estado["matrizes"]["queijo"] = get_matriz_queijo_tapioca()
        elif estado["billy_tem_queijo"]:
            estado["matrizes"]["queijo"] = get_matriz_queijo_mao(estado["billy_x"], estado["billy_y"])
        else:
            estado["matrizes"]["queijo"] = get_matriz_queijo_mesa()

# RENDERIZAÇÃO
def desenhar_jogo(tela, estado):
    definirAreaDeRecorte(0, 0, estado["largura"], estado["altura"])
    
    #FUNDO
    tela.fill((135, 206, 235)) 
    tela.fill((100, 100, 100), (0, 300, estado["largura"], 450)) 

    #CENÁRIO
    desenhar_cenario(tela, None, estado["img_bandeira"])
    
    m = estado["matrizes"]
    renderizarPersonagem(tela, getBilly(), m["billy"], None)
    renderizarPersonagem(tela, getMenino(), m["menino"], None)
    
    if estado["clara_chegou"] and not estado["clara_recebeu_pedido"]:
            if not estado["billy_tem_queijo"] and not estado["tapioca_recheada"]:
                setBalao1(tela, estado["clara_x"] + 20, estado["clara_y"] - 100)
                setObjetivo1(tela, 500, 50)
            elif estado["billy_tem_queijo"]:
                setObjetivo2(tela, 500, 50)
            elif estado["tapioca_recheada"]:
                setObjetivo3(tela, 500, 50)

    if not estado["clara_foi_embora"]:
        renderizarPersonagem(tela, getMulher(), m["clara"], None)

    if not estado["clara_foi_embora"] or not estado["clara_recebeu_pedido"]:
        renderizarPersonagem(tela, getTapioca(largura=25, altura=13), m["tapioca"])
        renderizarPersonagem(tela, getQueijo(), m["queijo"])
    
    if estado["clara_recebeu_pedido"] and not estado["clara_foi_embora"]:
        setBalao2(tela, estado["clara_x"] + 20, estado["clara_y"] - 100)

    #VIEWPORT
    personagens_vp = [
        (getBilly(), m["billy"]),
        (getMenino(), m["menino"]),
        (getQueijo(), m["queijo"]),
        (getTapioca(), m["tapioca"]) 
    ]
    if not estado["clara_foi_embora"]:
        personagens_vp.append((getMulher(), m["clara"]))

    renderizarViewport(tela, estado["matriz_vp"], personagens_vp, estado["img_bandeira"])

    #INTERFACE
    tempo_texto = f"Tempo: {estado['tempo_atual_s']:.1f}s"
    setTexto(tela, tempo_texto, 20, 20, (0, 0, 0))

    # Botão Instruções
    setPreencherRetanguloFloodfill(
        tela, BTN_INSTR_X, BTN_INSTR_Y, BTN_INSTR_W, BTN_INSTR_H, 
        (0,0,0), (200, 200, 200)
    )
    setTexto(tela, "INSTRUÇÕES", BTN_INSTR_X + 45, BTN_INSTR_Y + 15, (0,0,0))

    # MODAL DE INSTRUÇÕES (CORRIGIDO COM SCANLINE, o floodfill não funcionou bem aqui)
    if estado["mostrando_instrucoes"]:
        setPreencherRetangulo(
            tela, MODAL_X, MODAL_Y, MODAL_W, MODAL_H, 
            (250, 240, 200) # Bege 
        )
        
        # Desenha apenas a borda preta
        setRetangulo(
            tela, MODAL_X, MODAL_Y, MODAL_W, MODAL_H, 
            (0, 0, 0)
        )

        # Botão Fechar
        fechar_x = MODAL_X + MODAL_W - BTN_FECHAR_TAM - 10
        fechar_y = MODAL_Y + 10
        
        setPreencherRetangulo(
             tela, fechar_x, fechar_y, BTN_FECHAR_TAM, BTN_FECHAR_TAM,
             (255, 0, 0)
        )
        setRetangulo(
             tela, fechar_x, fechar_y, BTN_FECHAR_TAM, BTN_FECHAR_TAM,
             (0, 0, 0)
        )
        
        # O X branco
        setRetaBresenham(tela, fechar_x + 5, fechar_y + 5, fechar_x + 35, fechar_y + 35, (255,255,255))
        setRetaBresenham(tela, fechar_x + 35, fechar_y + 5, fechar_x + 5, fechar_y + 35, (255,255,255))

        # Texto
        txt_instrucoes = (
            "COMO JOGAR: [quebra de linha]"
            "[quebra de linha]"
            "W, A, S, D  ->  Mover o Billy [quebra de linha]"
            "ESPAÇO      ->  Interagir (Pegar/Entregar) [quebra de linha]"
            "[quebra de linha]"
            "OBJETIVO: [quebra de linha]"
            "1. Pegue o queijo na caixa amarela. [quebra de linha]"
            "2. Coloque o queijo na tapioca no balcão. [quebra de linha]"
            "3. Entregue a tapioca pronta para a Clara."
        )
        setTexto(tela, txt_instrucoes, MODAL_X + 30, MODAL_Y + 30, (0,0,0))