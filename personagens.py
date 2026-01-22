import pygame
from biblioteca import *
from matrizes import *


def getBilly():
    #Definido na orgiem (0,0) para nao deformar o billy
    cor_pele = (179, 139, 109)
    cor_roupa = (255, 0, 0)
    cor_branco = (255, 255, 255)
    cor_preto = (0, 0, 0)

    return [
        # --- CORPO E JALECO ---
        {"nome": "corpo", "cor": cor_roupa, "pontos": [(-5, 30), (35, 30), (35, 80), (-5, 80)]},
        {"nome": "jaleco", "cor": cor_branco, "pontos": [(-5, 30), (35, 30), (35, 80), (-5, 80)]},
        {"nome": "abertura_jaleco", "cor": cor_roupa, "pontos": [(12, 30), (18, 30), (18, 80), (12, 80)]},

        # --- CABEÇA ---
        {"nome": "cabeca", "cor": cor_pele, "pontos": [(0, 0), (30, 0), (30, 30), (0, 30)]},
        
        # --- BONÉ ---
        {"nome": "bone_topo", "cor": cor_branco, "pontos": [(0, -5), (30, -5), (30, 5), (0, 5)]},
        {"nome": "bone_aba", "cor": cor_branco, "pontos": [(15, 0), (35, 0), (35, 5), (15, 5)]},
        
        # --- OLHOS (Preenchidos) ---
        {"nome": "olho_e", "cor": cor_preto, "pontos": [(5, 12), (10, 12), (10, 17), (5, 17)]},
        {"nome": "olho_d", "cor": cor_preto, "pontos": [(20, 12), (25, 12), (25, 17), (20, 17)]},
        
        # --- BRAÇOS E PERNAS ---
        {"nome": "braco_e", "cor": cor_pele, "pontos": [(-15, 35), (-5, 35), (-5, 65), (-15, 65)]},
        {"nome": "braco_d", "cor": cor_pele, "pontos": [(35, 35), (45, 35), (45, 65), (35, 65)]},
        {"nome": "perna_e", "cor": cor_pele, "pontos": [(0, 80), (10, 80), (10, 110), (0, 110)]},
        {"nome": "perna_d", "cor": cor_pele, "pontos": [(20, 80), (30, 80), (30, 110), (20, 110)]},

        # --- ÓCULOS (Vazados - Apenas contorno para não tampar o olho) ---
        {"nome": "aro_e", "cor": cor_preto, "tipo": "apenas_contorno", "pontos": [(3, 10), (12, 10), (12, 19), (3, 19)]},
        {"nome": "aro_d", "cor": cor_preto, "tipo": "apenas_contorno", "pontos": [(18, 10), (27, 10), (27, 19), (18, 19)]},
        
        # --- LINHAS (Boca e Ponte dos óculos) ---
        {"nome": "ponte", "cor": cor_preto, "tipo": "linha", "pontos": [(12, 15), (18, 15)]},
        {"nome": "boca", "cor": cor_roupa, "tipo": "linha", "pontos": [(10, 23), (20, 23)]}
    ]

def renderizarBilly(superficie, modelo, matriz):
    for parte in modelo:
        # Aplica a matriz composta (Escala, Rotação, Translação)
        pts_trans = aplicaTransformacao(matriz, parte["pontos"])
        cor = parte["cor"]
        
        # Só preenche se não for uma peça marcada como 'apenas_contorno' ou 'linha'
        if len(pts_trans) > 2 and parte.get("tipo") != "apenas_contorno" and parte.get("tipo") != "linha":
            scanline_fill(superficie, pts_trans, cor)
        
        # Desenha o contorno com a mesma cor para suavizar as bordas e nao ficar com aquele treco preto ao redor
        n = len(pts_trans)
        for i in range(n):
            # Se for 'linha', não fecha o polígono (ex: boca) OBS:hidelbrando não apaga para nao deformar a boca do billy
            if parte.get("tipo") == "linha" and i == n - 1:
                break
                
            p1 = pts_trans[i]
            p2 = pts_trans[(i + 1) % n]
            
            setRetaBresenham(superficie, int(p1[0]), int(p1[1]), int(p2[0]), int(p2[1]), cor)

def setMulher(superficie, x, y):
    # Definindo cores específicas
    cor_pele = (179, 139, 109)
    cor_mecha_rosa = (255, 105, 180) # Rosa choque
    cor_olho = (0, 0, 0) # Preto
    cor_vestido = (255, 150, 200)
    cor_cabelo =(0, 0, 0)

    # --- CABEÇA ---
    setPreencherRetangulo(superficie, x, y, 30, 30, cor_pele)
    
    # --- CABELO (Por cima da cabeça) ---
    # Cabelo principal no topo
    setPreencherRetangulo(superficie, x, y - 10, 30, 15, cor_cabelo)
    # Cabelo nas laterais (para dar volume)
    setPreencherRetangulo(superficie, x - 5, y, 5, 20, cor_cabelo)
    setPreencherRetangulo(superficie, x + 30, y, 5, 20, cor_cabelo)
    
    # --- MECHA ROSA (Fina na frente, por cima do cabelo) ---
    setPreencherRetangulo(superficie, x + 10, y - 5, 5, 15, cor_mecha_rosa)

    # --- OLHOS ---
    setPreencherRetangulo(superficie, x + 5, y + 10, 5, 5, cor_olho)  # Olho esquerdo
    setPreencherRetangulo(superficie, x + 20, y + 10, 5, 5, cor_olho) # Olho direito

    # --- BOCA (Reta Vermelha) ---
    setRetaBresenham(superficie, x + 10, y + 23, x + 20, y + 23, (255, 0, 0))

    # --- CORPO (Vestido Rosa) ---
    # Começa um pouco mais estreito na parte de cima
    setPreencherRetangulo(superficie, x - 5, y + 30, 40, 60, cor_vestido)

    # --- BRAÇOS (Cor da Pele) ---
    setPreencherRetangulo(superficie, x - 15, y + 35, 10, 30, cor_pele) # Braço esquerdo
    setPreencherRetangulo(superficie, x + 35, y + 35, 10, 30, cor_pele) # Braço direito

    # --- PERNAS (Cor da Pele) ---
    setPreencherRetangulo(superficie, x, y + 90, 10, 30, cor_pele)      # Perna esquerda (Y um pouco mais baixo por causa do vestido)
    setPreencherRetangulo(superficie, x + 20, y + 90, 10, 30, cor_pele) # Perna direita
    
def setMenino(superficie, x, y):
    cor_pele = (255, 224, 189)   # Pele clara
    cor_cabelo = (0, 0, 0)        # Preto
    cor_blusa = (173, 216, 230)   # Azul Claro
    cor_calca = (0, 0, 139)       # Azul Escuro
    cor_preto = (0, 0, 0)

    # --- CABELO (Parte de trás/topo) ---
    setPreencherRetangulo(superficie, x, y - 5, 30, 15, cor_cabelo)

    # --- CABEÇA ---
    setPreencherRetangulo(superficie, x, y, 30, 30, cor_pele)

    # --- ÓCULOS REDONDOS --
    # Aro Esquerdo
    setCirculo(superficie, x + 8, y + 15, 6, cor_preto)
    # Aro Direito
    setCirculo(superficie, x + 22, y + 15, 6, cor_preto)
    # Ponte dos óculos 
    setRetaBresenham(superficie, x + 14, y + 15, x + 16, y + 15, cor_preto)

    # --- OLHOS (Pontinhos dentro dos óculos) ---
    setPixel(superficie, x + 8, y + 15, cor_preto)
    setPixel(superficie, x + 22, y + 15, cor_preto)

    # --- BOCA (Reta Vermelha básica) ---
    setRetaBresenham(superficie, x + 12, y + 25, x + 18, y + 25, (200, 0, 0))

    # --- BLUSA (Corpo) ---
    setPreencherRetangulo(superficie, x - 5, y + 30, 40, 40, cor_blusa)

    # --- BRAÇOS ---
    setPreencherRetangulo(superficie, x - 15, y + 30, 10, 30, cor_pele)
    setPreencherRetangulo(superficie, x + 35, y + 30, 10, 30, cor_pele)

    # --- CALÇA (Continuação do corpo) ---
    setPreencherRetangulo(superficie, x - 5, y + 70, 40, 20, cor_calca)

    # --- PERNAS 
    setPreencherRetangulo(superficie, x, y + 90, 12, 25, cor_calca)      # Perna esquerda
    setPreencherRetangulo(superficie, x + 18, y + 90, 12, 25, cor_calca) # Perna direita

