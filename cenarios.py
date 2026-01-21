from biblioteca import *

def setCachorro(superficie, x, y):
    cor1 = (236, 178, 95)
    cor2 = (244, 146, 71)
    cor3 = (0, 0, 0)
    cor4 = (182, 0, 71)

    #orelha1
    setPreencherRetangulo(superficie, x + -10, y , 10, 20, cor2)
    #cabeça
    setPreencherRetangulo(superficie, x, y, 35, 35, cor1)
    #orelha2
    setPreencherRetangulo(superficie, x + 30, y , 15, 20, cor2)
    #olho1
    setPreencherRetangulo(superficie, x + 3, y + 8, 8, 8, cor3)
    #olho2
    setPreencherRetangulo(superficie, x + 20, y + 8, 8, 8, cor3)
    #nariz
    setPreencherRetangulo(superficie, x + 5, y + 20, 8, 8, cor4)

    #corpo
    setPreencherRetangulo(superficie, x + 10, y + 35, 110, 35, cor1)
    #rabo
    setPreencherRetangulo(superficie, x + 110, y + 35, 30, 10, cor1)

    #perna1
    setPreencherRetangulo(superficie, x + 20, y + 70, 12, 35, cor1)
    #pé1
    setPreencherRetangulo(superficie, x + 15, y + 95, 10, 10, cor2)

    #perna2
    setPreencherRetangulo(superficie, x + 40, y + 70, 12, 35, cor1)
    #pé2
    setPreencherRetangulo(superficie, x + 36, y + 95, 10, 10, cor2)

    #perna3
    setPreencherRetangulo(superficie, x + 80, y + 70, 12, 35, cor1)
    #pé3
    setPreencherRetangulo(superficie, x + 75, y + 95, 10, 10, cor2)

    #perna4
    setPreencherRetangulo(superficie, x + 100, y + 70, 12, 35, cor1)
    #pé4
    setPreencherRetangulo(superficie, x + 95, y + 95, 10, 10, cor2)


def setBanco(superficie, x, y):
    corbanco1 = (186, 186, 178)
    corbanco2 = (145, 145, 131)
    corbanco3 = (110, 109, 102)
    
    #parte de sentar
    setPreencherRetangulo(superficie, x, y, 200, 30, corbanco1)
    
    #parte das costas
    setPreencherRetangulo(superficie, x  + 10 , y - 60, 180, 60, corbanco2)
    #parte das costas linha1
    setPreencherRetangulo(superficie, x  + 10 , y - 50, 180, 10, corbanco3)
    #parte das costas linha2
    setPreencherRetangulo(superficie, x  + 10 , y - 30, 180, 10, corbanco3)
    #parte das costas linha3
    setPreencherRetangulo(superficie, x  + 10 , y - 10, 180, 10, corbanco3)
    

    #PÉ ESQUERDO
    setPreencherRetangulo(superficie, x + 15, y + 20, 15, 50, corbanco1)
    
    #PÉ DIREITO
    setPreencherRetangulo(superficie, x + 170, y + 20, 15, 50, corbanco1)

def setJarro(superficie, x, y):
    corjarro1 = (100, 50, 0)
    corjarro2 = (117, 94, 80)
    corjarro3 = (26, 166, 19)
    corjarro4 = (201, 58, 110)
    
    #tronco
    setPreencherRetangulo(superficie, x + 13, y - 50, 15, 100, corjarro1)

    #arvore1
    setPreencherRetangulo(superficie, x - 30, y - 80, 100, 50, corjarro3)
    #arvore2
    setPreencherRetangulo(superficie, x - 10, y - 110, 60, 40, corjarro3)
    #arvore3
    setPreencherRetangulo(superficie, x + 5, y - 130, 30, 20, corjarro3)

    #Jarro1
    setPreencherRetangulo(superficie, x, y, 40, 50, corjarro2)
    #Jarro2
    setPreencherRetangulo(superficie, x -10, y + 30, 60, 60, corjarro2)

     #flor1
    setPreencherRetangulo(superficie, x - 10, y - 60, 15, 15, corjarro4)
    #flor2
    setPreencherRetangulo(superficie, x + 40, y - 60, 15, 15, corjarro4)
    #flor3
    setPreencherRetangulo(superficie, x + 10, y - 100, 15, 15, corjarro4)

def setMesa(superficie, x, y):
    cor = (100, 50, 0)

    setPreencherRetangulo(superficie, x, y, 200, 20, cor)
    
    # --- PÉ ESQUERDO ---
    setPreencherRetangulo(superficie, x + 15, y + 20, 15, 80, cor)
    
    # --- PÉ DIREITO ---
    # Posicionado no final do tampo (x + 170) e logo abaixo do tampo (y + 20)
    setPreencherRetangulo(superficie, x + 170, y + 20, 15, 80, cor)

def setCarrinho(superficie, x, y):
    cor_preto = (0, 0, 0)
    
    # --- NOVAS DIMENSÕES (Dobro do tamanho anterior) ---
    escala = 100         
    altura_base = 40     
    largura_total = escala * 3  # 300px no total
    
    # 1. QUADRADO CENTRAL (Preenchido)
    setPreencherRetangulo(superficie, x + escala, y, escala, escala, cor_preto)

    # 2. TRIÂNGULO DA ESQUERDA (Contorno)
    setTrianguloGenerico(
        superficie,
        x + escala, y,           # Topo (encosta no quadrado)
        x + escala, y + escala,  # Canto reto (inferior direito)
        x,           y + escala,  # Ponta esquerda
        cor_preto
    )

    # 3. TRIÂNGULO DA DIREITA (Contorno)
    # Ângulo reto no canto inferior esquerdo (x + 2*escala, y + escala)
    setTrianguloGenerico(
        superficie,
        x + (escala * 2), y,           # Topo (encosta no outro lado do quadrado)
        x + (escala * 2), y + escala,  # Canto reto (inferior esquerdo)
        x + (escala * 3), y + escala,  # Ponta direita
        cor_preto
    )

    # 4. BASE RETANGULAR (Contorno)
    # Fica logo abaixo das formas de cima
    setRetangulo(superficie, x, y + escala, largura_total, altura_base, cor_preto)