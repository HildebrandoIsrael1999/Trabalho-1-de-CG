import pygame
import sys
from biblioteca import *
from personagens import *
from matrizes import *
from cenarios import *
from textos import *
from colisao import GerenciadorColisao

# ---CONFIGURAÇÕES INICIAIS ---
pygame.init()
pygame.display.set_caption("Billy da Tapioca - Versão com Textura")
clock = pygame.time.Clock()
largura, altura = 1280, 720
tela = pygame.display.set_mode((largura, altura))

# pygame.font.init()
# fonte_oi = pygame.font.Font("Fontes/Oi-Regular.ttf", 40)
# texto = fonte_oi.render("Oi Tapioca!", True, (0, 0, 0))
# rect_texto = texto.get_rect(center=(largura // 2, altura // 2))


try:
    img_bandeira = pygame.image.load("bandeira.png").convert()
except:
    print("Erro: Não encontrei o arquivo bandeira.png. Usando superfície de erro.")
    img_bandeira = pygame.Surface((100, 100))
    img_bandeira.fill((255, 0, 255))

colisor = GerenciadorColisao(DADOS_DO_CENARIO)
matriz_vp = calcularMatrizViewport(960, 20, 1260, 190, 1280, 720)

billy_x, billy_y = 270, 330
billy_escala = 1.0
billy_angulo = 0

clara_x, clara_y = 100, 590
clara_escala = 0.9
clara_angulo = 0

menino_x, menino_y = 200, 590
menino_escala = 1.0
menino_angulo = 0

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Salva posição atual
    billy_x_antigo, billy_y_antigo = billy_x, billy_y
    
    # Lógica de Input
    teclas = pygame.key.get_pressed()
    
    # Movimentação Billy
    dx, dy = 0, 0
    if teclas[pygame.K_a]: dx -= 40
    if teclas[pygame.K_d]: dx += 40
    if teclas[pygame.K_w]: dy -= 40  
    if teclas[pygame.K_s]: dy += 40 
    
    # Rotação Billy
    if teclas[pygame.K_r]: billy_angulo += 5

    # Teste de colisão antes de aplicar o movimento
    novo_x = billy_x + dx
    novo_y = billy_y + dy

    if not colisor.verificarMovimento(getBilly(), novo_x, novo_y, billy_escala, billy_angulo):
        billy_x = novo_x
        billy_y = novo_y
        billy_x, billy_y = limitar_personagem_na_janela(billy_x, billy_y, 40, 110, largura, altura)
    

    if teclas[pygame.K_LEFT]:  clara_x -= 10
    if teclas[pygame.K_RIGHT]: clara_x += 10
    if teclas[pygame.K_UP]:    clara_y -= 10  
    if teclas[pygame.K_DOWN]:  clara_y += 10 

    # --- CÁLCULO DAS MATRIZES ---
    m_billy = calcularMatriz(billy_escala, billy_angulo, billy_x, billy_y)
    m_clara = calcularMatriz(clara_escala, clara_angulo, clara_x, clara_y)
    m_menino = calcularMatriz(menino_escala, menino_angulo, menino_x, menino_y)


    definirAreaDeRecorte(0, 0, 1280, 720)
    tela.fill((146, 255, 222))
    tela.fill((100, 100, 100), (0, 300, largura, 450)) 

    desenhar_cenario(tela, None, img_bandeira)
    
    setBalao1(tela, clara_x + 20, clara_y - 100)
    setBalao2(tela, billy_x + 20, billy_y - 100)

    renderizarPersonagem(tela, getBilly(), m_billy, None)
    renderizarPersonagem(tela, getMulher(), m_clara, None)
    renderizarPersonagem(tela, getMenino(), m_menino, None)
    
    # Viewport (O mini-mapa também receberá a textura da bandeira)
    personagens_atuais = [
        (getBilly(), m_billy),
        (getMulher(), m_clara),
        (getMenino(), m_menino),
    ]
    renderizarViewport(tela, matriz_vp, personagens_atuais)

    # # Testes de preenchimento
    # setPreencherQuadradoFloodfill(tela, 50, 50, 100, (0, 255, 0), (0, 0, 255))
    # setPreencherRetanguloFloodfill(tela, 200, 50, 150, 80, (255, 255, 0), (128, 0, 128))
    # setPreencherTrianguloFloodfill(tela, 400, 50, 100, (255, 255, 255), (255, 0, 255))
    # setTrianguloGenerico(tela, 600, 50, 550, 150, 650, 150, (0, 0, 0))

    # TEXTO
    # tela.blit(texto,rect_texto)
    renderizarViewport(tela, matriz_vp, personagens_atuais, img_bandeira)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
