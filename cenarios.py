from biblioteca import *
from textos import *

def setCachorro(superficie, x, y):
    cor1 = (236, 178, 95)
    cor2 = (244, 146, 71)
    cor3 = (0, 0, 0)
    cor4 = (182, 0, 71)

    #orelha1
    setPreencherRetangulo(superficie, x + -10, y , 10, 15, cor2)
    #cabeça
    setPreencherRetangulo(superficie, x, y, 25, 25, cor1)
    #orelha2
    setPreencherRetangulo(superficie, x + 25, y , 10, 15, cor2)
    #olho1
    setPreencherRetangulo(superficie, x + 2, y + 8, 5, 5, cor3)
    #olho2
    setPreencherRetangulo(superficie, x + 15, y + 8, 5, 5, cor3)
    #nariz
    setPreencherRetangulo(superficie, x + 5, y + 15, 5, 5, cor4)

    #corpo
    setPreencherRetangulo(superficie, x + 10, y + 25, 80, 25, cor1)
    #rabo
    setPreencherRetangulo(superficie, x + 85, y + 35, 30, 8, cor1)

    #perna1
    setPreencherRetangulo(superficie, x + 15, y + 50, 8, 25, cor1)
    
    #perna2
    setPreencherRetangulo(superficie, x + 30, y + 50, 8, 25, cor1)
    
    #perna3
    setPreencherRetangulo(superficie, x + 60, y + 50, 8, 25, cor1)
    
    #perna4
    setPreencherRetangulo(superficie, x + 75, y + 50, 8, 25, cor1)
    
def setCachorroMarrom(superficie, x, y):
    cor1 = (143, 97, 60)
    cor2 = (105, 68, 40)
    cor3 = (0, 0, 0)
    cor4 = (66, 17, 31)

    #orelha1
    setPreencherRetangulo(superficie, x -5, y - 10, 10, 15, cor2)
    #cabeça
    setPreencherRetangulo(superficie, x, y, 25, 25, cor1)
    #orelha2
    setPreencherRetangulo(superficie, x + 20, y - 10, 10, 15, cor2)
    #olho1
    setPreencherRetangulo(superficie, x + 2, y + 8, 5, 5, cor3)
    #olho2
    setPreencherRetangulo(superficie, x + 15, y + 8, 5, 5, cor3)
    #nariz
    setPreencherRetangulo(superficie, x + 5, y + 15, 5, 5, cor4)

    #corpo
    setPreencherRetangulo(superficie, x + 10, y + 25, 80, 25, cor1)
    #rabo
    setPreencherRetangulo(superficie, x + 85, y + 35, 30, 8, cor1)

    #perna1
    setPreencherRetangulo(superficie, x + 15, y + 50, 8, 25, cor1)
    
    #perna2
    setPreencherRetangulo(superficie, x + 30, y + 50, 8, 25, cor1)
    
    #perna3
    setPreencherRetangulo(superficie, x + 60, y + 50, 8, 25, cor1)
    
    #perna4
    setPreencherRetangulo(superficie, x + 75, y + 50, 8, 25, cor1)

def setBanco(superficie, x, y):
    corbanco1 = (186, 186, 178)
    corbanco2 = (145, 145, 131)
    corbanco3 = (110, 109, 102)
    
    #parte de sentar
    setPreencherRetangulo(superficie, x, y, 200, 20, corbanco1)
    
    #parte das costas
    setPreencherRetangulo(superficie, x  + 10 , y - 50, 180, 50, corbanco2)
    
    setPreencherRetangulo(superficie, x  + 10 , y - 40, 180, 5, corbanco3)
    setPreencherRetangulo(superficie, x  + 10 , y -20, 180, 5, corbanco3)

    #PÉ ESQUERDO
    setPreencherRetangulo(superficie, x + 15, y + 15, 15, 30, corbanco1)
    #PÉ DIREITO
    setPreencherRetangulo(superficie, x + 170, y + 15, 15, 30, corbanco1)

def setJarro(superficie, x, y):
    corjarro1 = (100, 50, 0)
    corjarro2 = (117, 94, 80)
    corjarro3 = (26, 166, 19)
    corjarro4 = (201, 58, 110)
    
    #tronco
    setPreencherRetangulo(superficie, x + 15, y - 50, 10, 50, corjarro1)

    #arvore1
    setPreencherRetangulo(superficie, x, y - 80, 40, 40, corjarro3)
    #arvore2
    setPreencherRetangulo(superficie, x + 10, y - 110, 20, 40, corjarro3)
    #arvore3
    setPreencherRetangulo(superficie, x + 15, y - 130, 10, 30, corjarro3)

    #Jarro1
    setPreencherRetangulo(superficie, x, y, 40, 40, corjarro2)

     #flor1
    setPreencherRetangulo(superficie, x , y - 60, 10, 10, corjarro4)
    #flor2
    setPreencherRetangulo(superficie, x + 30, y - 70, 10, 10, corjarro4)
    #flor3
    setPreencherRetangulo(superficie, x + 10, y - 100, 10, 10, corjarro4)

def setMesa(superficie, x, y):
    cor = (100, 50, 0)

    setPreencherRetangulo(superficie, x, y, 200, 20, cor)
    
    # --- PÉ ESQUERDO ---
    setPreencherRetangulo(superficie, x + 15, y + 20, 15, 80, cor)
    
    # --- PÉ DIREITO ---
    # Posicionado no final do tampo (x + 170) e logo abaixo do tampo (y + 20)
    setPreencherRetangulo(superficie, x + 170, y + 20, 15, 80, cor)

def setCarrinho(superficie, x, y):
    corcarrinho1 = (193, 197, 209)
    corcarrinho2 = (230, 101, 85)
    corcarrinho3 = (116, 117, 120)
    corcarrinho4= (89, 89, 89)
    corcarrinho5= (38, 70, 166)
    tamanho = 50  # Tamanho do quadrado e base dos triângulos
    largura_base = 150 # tamanho * 3 (pois são 3 peças em cima)

    # --- 1. QUADRADO CENTRAL (Preenchido) ---
    # Ele começa deslocado para a direita pelo tamanho do primeiro triângulo
    setPreencherRetangulo(superficie, x + tamanho, y, tamanho, tamanho, corcarrinho1)

    # --- 2. TRIÂNGULO DA ESQUERDA (Contorno) ---
    # Ângulo reto encostado no quadrado (x + tamanho, y + tamanho)
    setPreencherTrianguloGenerico(
        superficie,
        x + tamanho, y,           # Topo (encostado no quadrado)
        x + tamanho, y + tamanho, # Ângulo Reto (inferior direito)
        x,           y + tamanho, # Ponta esquerda
        corcarrinho1
    )

    # --- 3. TRIÂNGULO DA DIREITA (Contorno) ---
    # Ângulo reto encostado no outro lado do quadrado (x + 2*tamanho)
    setPreencherTrianguloGenerico(
        superficie,
        x + (tamanho * 2), y,           # Topo (encostado no quadrado)
        x + (tamanho * 2), y + tamanho, # Ângulo Reto (inferior esquerdo)
        x + (tamanho * 3), y + tamanho, # Ponta direita
        corcarrinho1
    )

    # --- 4. BASE RETANGULAR (Contorno) ---
    # Posicionado logo abaixo das outras peças (y + tamanho)
    setPreencherRetangulo(superficie, x, y + tamanho, largura_base, 40, corcarrinho5)
    setPreencherRetangulo(superficie, x, y + tamanho, largura_base, 15, corcarrinho2)
    
    #roda1
    setPreencherRetangulo(superficie, x + 10, y + tamanho + 40, 20, 30, corcarrinho3)
    #roda1linha1
    setPreencherRetangulo(superficie, x + 10, y + tamanho + 40, 10, 20, corcarrinho4)

    #roda2
    setPreencherRetangulo(superficie, x + 120, y + tamanho + 40, 20, 30, corcarrinho3)
    #roda2linha2
    setPreencherRetangulo(superficie, x + 130, y + tamanho + 40, 10, 20, corcarrinho4)

def setLixeiras(superficie, x, y):
    corlixeira1 = (217, 56, 56)
    corlixeira2 = (235, 198, 17)
    corlixeira3 = (50, 173, 31)
    corlixeira4 = (31, 46, 173)
    corsuportelixeira = (107, 107, 107)
    cordentrolixeira = (38, 38, 38)

    #suporte lixeira
    setPreencherRetangulo(superficie, x , y+ 10, 10, 80, corsuportelixeira)
    #suporte lateral lixeira 1
    setPreencherRetangulo(superficie, x + 38, y + 10, 20, 10, corsuportelixeira)

    #lixeira vermelha
    setPreencherRetangulo(superficie, x + 10 , y, 35, 60, corlixeira1)
    #lixeira vermelha parte de dentro
    setPreencherRetangulo(superficie, x + 18, y + 10, 20, 10, cordentrolixeira)

    #lixeira amarela
    setPreencherRetangulo(superficie, x + 55 , y, 35, 60, corlixeira2)
    #lixeira amarela parte de dentro
    setPreencherRetangulo(superficie, x + 63, y + 10, 20, 10, cordentrolixeira)

    #suporte lateral lixeira 2
    setPreencherRetangulo(superficie, x + 90, y + 10, 20, 10, corsuportelixeira)

    #lixeira verde
    setPreencherRetangulo(superficie, x + 100 , y, 35, 60, corlixeira3)
    #lixeira verde parte de dentro
    setPreencherRetangulo(superficie, x + 108, y + 10, 20, 10, cordentrolixeira)

    #suporte lateral lixeira 3
    setPreencherRetangulo(superficie, x + 135, y + 10, 20, 10, corsuportelixeira)

    #lixeira azul
    setPreencherRetangulo(superficie, x + 145 , y, 35, 60, corlixeira4)
    #lixeira azul parte de dentro
    setPreencherRetangulo(superficie, x + 153, y + 10, 20, 10, cordentrolixeira)

    #suporte lixeira
    setPreencherRetangulo(superficie, x + 180, y+ 10, 10, 80, corsuportelixeira)

def setMoita(superficie, x, y):
    
    cormoita = (108, 168, 84)
    corcaule=(110,10,10)
    corjarro = (161, 138, 104)
    corflor = (184, 32, 26)
    
    setPreencherRetangulo(superficie, x , y, 160, 30, cormoita)
    setPreencherRetangulo(superficie, x + 40 , y - 20, 80, 50, cormoita)
    
    #caule1
    setPreencherRetangulo(superficie, x + 20 , y + 30, 10, 20, corcaule)
    #caule2
    setPreencherRetangulo(superficie, x + 70 , y + 30, 10, 20, corcaule)
    #caule3
    setPreencherRetangulo(superficie, x + 125 , y + 30, 10, 20, corcaule)

    #jarro
    setPreencherRetangulo(superficie, x - 10, y + 50, 180, 25, corjarro)

    #flor1
    setPreencherRetangulo(superficie, x + 10, y + 10, 10, 10, corflor)
    #flor2
    setPreencherRetangulo(superficie, x + 60, y -10, 8, 8, corflor)
    #flor3
    setPreencherRetangulo(superficie, x + 90, y + 10, 10, 10, corflor)
    #flor4
    setPreencherRetangulo(superficie, x + 140, y + 15, 8, 8, corflor)

def setCarro(superficie, x, y):

    corcarro = (54, 54, 54)
    corroda = (0, 0, 0)
    corjanela = (168, 168, 168)
    corfarol = (232, 219, 160)
    corplaca = (255, 255, 255)

    setPreencherRetangulo(superficie, x, y, 150, 100, corcarro)
    setPreencherRetangulo(superficie, x -25, y + 60, 200, 50, corcarro)

    #roda1
    setPreencherRetangulo(superficie, x, y + 110, 20, 30, corroda)
    #roda1
    setPreencherRetangulo(superficie, x + 130, y + 110, 20, 30, corroda)

    #farol1
    setPreencherRetangulo(superficie, x - 10, y + 70, 25, 25, corfarol)
    #farol2
    setPreencherRetangulo(superficie, x + 130, y + 70, 25, 25, corfarol)

    #janela
    setPreencherRetangulo(superficie, x + 15, y + 10, 120, 40, corjanela)

    #placa
    setPreencherRetangulo(superficie, x + 55, y + 80, 40, 20, corplaca)

def setGato(superficie, x, y):
    # Cores do gato
    cor_principal = (128, 128, 128)  # Cinza
    cor_detalhe = (80, 80, 80)       # Cinza Escuro
    cor_preto = (0, 0, 0)
    cor_nariz = (255, 182, 193)      # Rosa claro

    # --- ORELHAS ---
    # Diminuídas para 6x10
    setPreencherRetangulo(superficie, x, y - 6, 6, 10, cor_detalhe)
    setPreencherRetangulo(superficie, x + 12, y - 6, 6, 10, cor_detalhe)

    # --- CABEÇA ---
    # Reduzida de 25x25 para 18x18
    setPreencherRetangulo(superficie, x, y, 18, 18, cor_principal)

    # --- OLHOS ---
    # Reduzidos para 3x3
    setPreencherRetangulo(superficie, x + 3, y + 5, 3, 3, cor_preto)
    setPreencherRetangulo(superficie, x + 12, y + 5, 3, 3, cor_preto)

    # --- NARIZ ---
    setPreencherRetangulo(superficie, x + 8, y + 10, 3, 2, cor_nariz)

    # --- BIGODES ---
    setRetaBresenham(superficie, x - 3, y + 10, x + 4, y + 11, cor_preto)
    setRetaBresenham(superficie, x + 14, y + 11, x + 21, y + 10, cor_preto)

    # --- CORPO ---
    # Encurtado de 60 para 40 de largura
    setPreencherRetangulo(superficie, x + 8, y + 18, 40, 18, cor_principal)

    # --- RABO ---
    # Mais curto e fino
    setPreencherRetangulo(superficie, x + 48, y + 22, 20, 4, cor_principal)

    # --- PERNAS ---
    # Encurtadas para 6x15
    setPreencherRetangulo(superficie, x + 9, y + 36, 6, 15, cor_principal) # Perna 1
    setPreencherRetangulo(superficie, x + 19, y + 36, 6, 15, cor_principal) # Perna 2
    setPreencherRetangulo(superficie, x + 32, y + 36, 6, 15, cor_principal) # Perna 3
    setPreencherRetangulo(superficie, x + 42, y + 36, 6, 15, cor_principal) # Perna 4

def desenhar_cenario(superficie):
    setMoita(superficie, 420, 260)
    setCarrinho(superficie, 100, 350)
    setJarro(superficie, 30,290)
    setBanco(superficie, 700, 300)
    setCachorro(superficie, 500, 400)
    setCachorroMarrom(superficie, 700, 600)
    setCarro(superficie, 1073, 400)
    setLixeiras(superficie, 1050, 250)
    setGato(superficie, 800,500)
    # setBalao1(superficie, 480, 200)
    # setBalao2(superficie, 680, 200)