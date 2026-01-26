import pygame
import math
from biblioteca import *
from personagens import *
from matrizes import *
from cenarios import *
from interacoes import *
from colisao import GerenciadorColisao

# --- INICIALIZAÇÃO DOS DADOS ---
def criar_estado_inicial(largura, altura):
    
    img_bandeira = pygame.image.load("bandeira.png").convert()

    return {
        "largura": largura, 
        "altura": altura,
        "colisor": GerenciadorColisao(DADOS_DO_CENARIO),
        "matriz_vp": calcularMatrizViewport(960, 20, 1260, 190, 1280, 720),
        "img_bandeira": img_bandeira,
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

# --- INPUTS (TECLADO/EVENTOS) ---
def processar_eventos_jogo(estado, eventos):
    for evento in eventos:
        if evento.type == pygame.KEYDOWN:
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
    teclas = pygame.key.get_pressed()
    dx, dy = 0, 0
    if teclas[pygame.K_a]: dx -= 20
    if teclas[pygame.K_d]: dx += 20
    if teclas[pygame.K_w]: dy -= 20  
    if teclas[pygame.K_s]: dy += 20 
    if teclas[pygame.K_r]: estado["billy_angulo"] += 5


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
                estado["clara_destino_x"] = -150
                estado["clara_chegou"] = False
            elif estado["clara_destino_x"] == -150:
                estado["clara_foi_embora"] = True
                print("Sistema: Clara saiu.")

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
    
    # Matrizes dos itens 
    if estado["clara_recebeu_pedido"]:
        estado["matrizes"]["queijo"] = get_matriz_queijo_clara(estado["clara_x"], estado["clara_y"])
        estado["matrizes"]["tapioca"] = get_matriz_tapioca_clara(estado["clara_x"], estado["clara_y"])
    else:
        # Lógica da Tapioca
        estado["matrizes"]["tapioca"] = get_matriz_tapioca_mesa()
        # Lógica do Queijo
        if estado["tapioca_recheada"]:
            estado["matrizes"]["queijo"] = get_matriz_queijo_tapioca()
        elif estado["billy_tem_queijo"]:
            estado["matrizes"]["queijo"] = get_matriz_queijo_mao(estado["billy_x"], estado["billy_y"])
        else:
            estado["matrizes"]["queijo"] = get_matriz_queijo_mesa()

# RENDERIZAÇÃO
def desenhar_jogo(tela, estado):
    """
    Só desenha. Não calcula lógica nenhuma.
    """
    definirAreaDeRecorte(0, 0, estado["largura"], estado["altura"])
    tela.fill((135, 206, 235)) 
    tela.fill((100, 100, 100), (0, 300, estado["largura"], 450)) 

    # Desenha Cenário
    desenhar_cenario(tela, None, estado["img_bandeira"])
    
    # Desenha Personagens 
    m = estado["matrizes"]
    renderizarPersonagem(tela, getBilly(), m["billy"], None)
    renderizarPersonagem(tela, getMenino(), m["menino"], None)
    
    if not estado["clara_foi_embora"]:
        renderizarPersonagem(tela, getMulher(), m["clara"], None)

    if not estado["clara_foi_embora"] or not estado["clara_recebeu_pedido"]:
        renderizarPersonagem(tela, getTapioca(largura=25, altura=13), m["tapioca"])
        renderizarPersonagem(tela, getQueijo(), m["queijo"])

    # Desenha Viewport
    personagens_vp = [
        (getBilly(), m["billy"]),
        (getMenino(), m["menino"]),
        (getQueijo(), m["queijo"]),
        (getTapioca(), m["tapioca"]) 
    ]
    if not estado["clara_foi_embora"]:
        personagens_vp.append((getMulher(), m["clara"]))

    renderizarViewport(tela, estado["matriz_vp"], personagens_vp, estado["img_bandeira"])