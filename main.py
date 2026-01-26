import pygame
import sys
import math
from biblioteca import *
from personagens import *
from matrizes import *
from cenarios import *
from interacoes import *
from colisao import GerenciadorColisao

# --- CONFIGURAÇÕES INICIAIS ---
pygame.init()
pygame.display.set_caption("Billy da Tapioca - Versão Clara")
clock = pygame.time.Clock()
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))

try:
    img_bandeira = pygame.image.load("bandeira.png").convert()
except:
    print("Aviso: bandeira.png não encontrada.")
    img_bandeira = pygame.Surface((100, 100))
    img_bandeira.fill((255, 0, 255))

colisor = GerenciadorColisao(DADOS_DO_CENARIO)
matriz_vp = calcularMatrizViewport(960, 20, 1260, 190, 1280, 720)

# --- ESTADOS DO JOGADOR (BILLY) ---
billy_x, billy_y = 270, 330
billy_escala = 1.0
billy_angulo = 0

# Estados de Inventário
billy_tem_queijo = False 
tapioca_recheada = False 

# --- ESTADOS DOS NPCs ---

# CLARA
clara_x, clara_y = 100, 590
clara_escala = 0.9
clara_angulo = 0

# Deslocamento da Clara (Seus valores)
clara_velocidade = 7 
clara_destino_x = 50    
clara_destino_y = 380   
clara_chegou = False    

# Estados de Fluxo da Clara
clara_recebeu_pedido = False 
clara_foi_embora = False     


menino_x, menino_y = 200, 590
menino_escala = 1.0
menino_angulo = 0

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                
                # FASE 1: PEGAR QUEIJO
                if not billy_tem_queijo and not tapioca_recheada and not clara_recebeu_pedido:
                    if pode_pegar_queijo(billy_x, billy_y):
                        billy_tem_queijo = True
                        print("Billy: Peguei o queijo!")
                    else:
                        print("Jogo: Chegue mais perto do queijo.")

                # FASE 2: MONTAR TAPIOCA
                elif billy_tem_queijo:
                    if pode_colocar_queijo(billy_x, billy_y):
                        billy_tem_queijo = False 
                        tapioca_recheada = True  
                        print("Billy: Tapioca montada!")
                    else:
                        print("Jogo: Chegue mais perto do centro do balcão.")

                # FASE 3: ENTREGAR PEDIDO
                elif tapioca_recheada: 
                    if pode_entregar_tapioca(billy_x, billy_y, clara_x, clara_y):
                        tapioca_recheada = False    # Sai do balcão
                        clara_recebeu_pedido = True # Vai para a mão da Clara
                        print("Billy: Pedido entregue para Clara!")
                    else:
                        print("Jogo: Chegue perto da Clara para entregar.")

    
    # A) BILLY
    teclas = pygame.key.get_pressed()
    dx, dy = 0, 0
    if teclas[pygame.K_a]: dx -= 20
    if teclas[pygame.K_d]: dx += 20
    if teclas[pygame.K_w]: dy -= 20  
    if teclas[pygame.K_s]: dy += 20 
    if teclas[pygame.K_r]: billy_angulo += 5
    
    # B) CLARA
    if not clara_foi_embora:
        if not clara_chegou:
            clara_x, clara_y, clara_chegou = mover_npc_para_alvo(
                clara_x, clara_y, 
                clara_destino_x, clara_destino_y, 
                clara_velocidade
            )
            clara_angulo = math.sin(pygame.time.get_ticks() * 0.01) * 5
        else:
            clara_angulo = 0 
            
            # Se ela já pegou a comida, o novo destino é ir embora
            if clara_recebeu_pedido:
                clara_destino_x = -150 # Fora da tela
                clara_chegou = False   # Força ela a andar de novo
            
            elif clara_destino_x == -150:
                clara_foi_embora = True
                print("Sistema: Clara saiu da loja.")

    # --- 3. COLISÃO ---
    m_clara_temp = calcularMatriz(clara_escala, clara_angulo, clara_x, clara_y)
    aabb_clara = get_aabb(getMulher(), m_clara_temp)
    m_menino_temp = calcularMatriz(menino_escala, menino_angulo, menino_x, menino_y)
    aabb_menino = get_aabb(getMenino(), m_menino_temp)
    
    obstaculos_vivos = [aabb_clara, aabb_menino]

    novo_x = billy_x + dx
    novo_y = billy_y + dy

    if not colisor.verificarMovimento(getBilly(), novo_x, novo_y, billy_escala, billy_angulo, obstaculos_vivos):
        billy_x = novo_x
        billy_y = novo_y
        billy_x, billy_y = limitar_personagem_na_janela(billy_x, billy_y, 40, 110, largura, altura, 300)
    
    m_billy = calcularMatriz(billy_escala, billy_angulo, billy_x, billy_y)
    m_clara = calcularMatriz(clara_escala, clara_angulo, clara_x, clara_y)
    m_menino = calcularMatriz(menino_escala, menino_angulo, menino_x, menino_y)

    if clara_recebeu_pedido:
        m_queijo = get_matriz_queijo_clara(clara_x, clara_y)
    elif tapioca_recheada:
        m_queijo = get_matriz_queijo_tapioca()
    elif billy_tem_queijo:
        m_queijo = get_matriz_queijo_mao(billy_x, billy_y)
    else:
        m_queijo = get_matriz_queijo_mesa()


    if clara_recebeu_pedido:
        m_tapioca = get_matriz_tapioca_clara(clara_x, clara_y)
    else:
        m_tapioca = get_matriz_tapioca_mesa()

    definirAreaDeRecorte(0, 0, 1280, 720)
    
    tela.fill((135, 206, 235)) 
    tela.fill((100, 100, 100), (0, 300, largura, 450)) 

    desenhar_cenario(tela, None, img_bandeira)
    
    renderizarPersonagem(tela, getBilly(), m_billy, None)
    
    if not clara_foi_embora:
        renderizarPersonagem(tela, getMulher(), m_clara, None)
        
    renderizarPersonagem(tela, getMenino(), m_menino, None)
    
    if not clara_foi_embora or not clara_recebeu_pedido:
        renderizarPersonagem(tela, getTapioca(largura=25, altura=13), m_tapioca)
        renderizarPersonagem(tela, getQueijo(), m_queijo)
    
    # --- VIEWPORT ---
    personagens_atuais = [
        (getBilly(), m_billy),
        (getMenino(), m_menino),
        (getQueijo(), m_queijo),
        (getTapioca(), m_tapioca) 
    ]
    if not clara_foi_embora:
        personagens_atuais.append((getMulher(), m_clara))

    renderizarViewport(tela, matriz_vp, personagens_atuais, img_bandeira)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()