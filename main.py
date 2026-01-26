import pygame
import sys
from biblioteca import *
from personagens import *
from matrizes import *
from cenarios import *
from interacoes import * # Importando nossa nova lógica!
from colisao import GerenciadorColisao

# --- CONFIGURAÇÕES INICIAIS ---
pygame.init()
pygame.display.set_caption("Billy da Tapioca - Versão Interativa")
clock = pygame.time.Clock()
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))

# Tenta carregar imagem ou cria erro
try:
    img_bandeira = pygame.image.load("bandeira.png").convert()
except:
    print("Aviso: bandeira.png não encontrada.")
    img_bandeira = pygame.Surface((100, 100))
    img_bandeira.fill((255, 0, 255))

# Inicializa gerenciadores
colisor = GerenciadorColisao(DADOS_DO_CENARIO)
matriz_vp = calcularMatrizViewport(960, 20, 1260, 190, 1280, 720)

# --- ESTADOS DO JOGADOR ---
billy_x, billy_y = 270, 330
billy_escala = 1.0
billy_angulo = 0

# Variáveis de Controle do Queijo
billy_tem_queijo = False # Ele está segurando?
tapioca_recheada = False # A tapioca já foi feita?

# --- ESTADOS DOS NPCs ---
clara_x, clara_y = 100, 590
clara_escala = 0.9
clara_angulo = 0

menino_x, menino_y = 200, 590
menino_escala = 1.0
menino_angulo = 0

rodando = True
while rodando:
    # --- 1. EVENTOS ---
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
        # Interação com a tecla ESPAÇO
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                
                # CENÁRIO A: Tentar PEGAR (Mão vazia e Tapioca vazia)
                if not billy_tem_queijo and not tapioca_recheada:
                    if pode_pegar_queijo(billy_x, billy_y):
                        billy_tem_queijo = True
                        print("Billy: Peguei o queijo!")
                    else:
                        print("Jogo: Chegue mais perto do queijo na mesa.")

                # CENÁRIO B: Tentar COLOCAR (Mão cheia)
                elif billy_tem_queijo:
                    if pode_colocar_queijo(billy_x, billy_y):
                        billy_tem_queijo = False # Solta
                        tapioca_recheada = True  # Recheia
                        print("Billy: Tapioca recheada com sucesso!")
                    else:
                        print("Jogo: Chegue mais perto da tapioca para rechear.")

    # --- 2. MOVIMENTO E INPUT CONTÍNUO ---
    teclas = pygame.key.get_pressed()
    
    # Movimentação Billy
    dx, dy = 0, 0
    if teclas[pygame.K_a]: dx -= 20
    if teclas[pygame.K_d]: dx += 20
    if teclas[pygame.K_w]: dy -= 20  
    if teclas[pygame.K_s]: dy += 20 
    if teclas[pygame.K_r]: billy_angulo += 5
    
    # Debug NPCs
    if teclas[pygame.K_LEFT]:  clara_x -= 10
    if teclas[pygame.K_RIGHT]: clara_x += 10
    if teclas[pygame.K_UP]:    clara_y -= 10  
    if teclas[pygame.K_DOWN]:  clara_y += 10 

    # --- 3. LÓGICA DE COLISÃO E FÍSICA ---
    # Atualiza caixas de colisão dos NPCs
    m_clara_temp = calcularMatriz(clara_escala, clara_angulo, clara_x, clara_y)
    aabb_clara = get_aabb(getMulher(), m_clara_temp)
    m_menino_temp = calcularMatriz(menino_escala, menino_angulo, menino_x, menino_y)
    aabb_menino = get_aabb(getMenino(), m_menino_temp)

    obstaculos_vivos = [aabb_clara, aabb_menino]

    # Verifica colisão antes de mover
    novo_x = billy_x + dx
    novo_y = billy_y + dy

    if not colisor.verificarMovimento(getBilly(), novo_x, novo_y, billy_escala, billy_angulo, obstaculos_vivos):
        billy_x = novo_x
        billy_y = novo_y
        # Mantém Billy dentro da tela e abaixo do horizonte (300)
        billy_x, billy_y = limitar_personagem_na_janela(billy_x, billy_y, 40, 110, largura, altura, 300)
    
    # --- 4. CÁLCULO DAS MATRIZES FINAIS ---
    m_billy = calcularMatriz(billy_escala, billy_angulo, billy_x, billy_y)
    m_clara = calcularMatriz(clara_escala, clara_angulo, clara_x, clara_y)
    m_menino = calcularMatriz(menino_escala, menino_angulo, menino_x, menino_y)

    # Lógica Visual do Queijo (A ordem dos ifs é importante!)
    if tapioca_recheada:
        # 1. Se já está pronta, desenha na tapioca
        m_queijo = get_matriz_queijo_tapioca()
    elif billy_tem_queijo:
        # 2. Se está na mão, desenha seguindo o Billy
        m_queijo = get_matriz_queijo_mao(billy_x, billy_y)
    else:
        # 3. Se não, desenha parado na mesa
        m_queijo = get_matriz_queijo_mesa()

    # --- 5. RENDERIZAÇÃO ---
    definirAreaDeRecorte(0, 0, 1280, 720)
    
    # Fundo
    tela.fill((135, 206, 235)) # Céu
    tela.fill((100, 100, 100), (0, 300, largura, 450)) # Chão

    # Desenha Cenário
    desenhar_cenario(tela, None, img_bandeira)
    
    # Desenha Personagens
    renderizarPersonagem(tela, getBilly(), m_billy, None)
    renderizarPersonagem(tela, getMulher(), m_clara, None)
    renderizarPersonagem(tela, getMenino(), m_menino, None)
    
    # Desenha o Queijo (dinâmico)
    renderizarPersonagem(tela, getQueijo(), m_queijo)
    
    # Viewport (Mini-mapa) - Adicionamos todos na lista
    personagens_atuais = [
        (getBilly(), m_billy),
        (getMulher(), m_clara),
        (getMenino(), m_menino),
        (getQueijo(), m_queijo) 
    ]
    renderizarViewport(tela, matriz_vp, personagens_atuais, img_bandeira)

    # Atualiza Tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()