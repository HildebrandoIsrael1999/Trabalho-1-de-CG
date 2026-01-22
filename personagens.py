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

def renderizarPersonagem(superficie, modelo, matriz):
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

def getMulher():
    # Cores extraídas da sua função original
    cor_pele = (179, 139, 109)
    cor_mecha_rosa = (255, 105, 180)
    cor_olho = (0, 0, 0)
    cor_vestido = (255, 150, 200)
    cor_cabelo = (0, 0, 0)
    cor_boca = (255, 0, 0)

    return [
        # --- CABELO FUNDO (Laterais) ---
        {"nome": "cabelo_esq", "cor": cor_cabelo, "pontos": [(-5, 0), (0, 0), (0, 20), (-5, 20)]},
        {"nome": "cabelo_dir", "cor": cor_cabelo, "pontos": [(30, 0), (35, 0), (35, 20), (30, 20)]},
        
        # --- CABEÇA ---
        {"nome": "cabeca", "cor": cor_pele, "pontos": [(0, 0), (30, 0), (30, 30), (0, 30)]},
        
        # --- CABELO TOPO ---
        {"nome": "cabelo_topo", "cor": cor_cabelo, "pontos": [(0, -10), (30, -10), (30, 5), (0, 5)]},
        
        # --- MECHA ROSA ---
        {"nome": "mecha", "cor": cor_mecha_rosa, "pontos": [(10, -5), (15, -5), (15, 10), (10, 10)]},

        # --- OLHOS ---
        {"nome": "olho_e", "cor": cor_olho, "pontos": [(5, 10), (10, 10), (10, 15), (5, 15)]},
        {"nome": "olho_d", "cor": cor_olho, "pontos": [(20, 10), (25, 10), (25, 15), (20, 15)]},

        # --- CORPO (Vestido) ---
        {"nome": "vestido", "cor": cor_vestido, "pontos": [(-5, 30), (35, 30), (35, 90), (-5, 90)]},

        # --- BRAÇOS ---
        {"nome": "braco_e", "cor": cor_pele, "pontos": [(-15, 35), (-5, 35), (-5, 65), (-15, 65)]},
        {"nome": "braco_d", "cor": cor_pele, "pontos": [(35, 35), (45, 35), (45, 65), (35, 65)]},

        # --- PERNAS ---
        {"nome": "perna_e", "cor": cor_pele, "pontos": [(0, 90), (10, 90), (10, 120), (0, 120)]},
        {"nome": "perna_d", "cor": cor_pele, "pontos": [(20, 90), (30, 90), (30, 120), (20, 120)]},

        # --- BOCA (Linha) ---
        {"nome": "boca", "cor": cor_boca, "tipo": "linha", "pontos": [(10, 23), (20, 23)]}
    ]
    
def getMenino():
    # Cores extraídas da sua função original
    cor_pele = (255, 224, 189)
    cor_cabelo = (0, 0, 0)
    cor_blusa = (173, 216, 230)
    cor_calca = (0, 0, 139)
    cor_preto = (0, 0, 0)
    cor_boca = (200, 0, 0)

    return [
        # --- CABELO (Parte de trás/topo) ---
        {"nome": "cabelo", "cor": cor_cabelo, "pontos": [(0, -5), (30, -5), (30, 10), (0, 10)]},

        # --- CABEÇA ---
        {"nome": "cabeca", "cor": cor_pele, "pontos": [(0, 0), (30, 0), (30, 30), (0, 30)]},

        # --- OLHOS (Pontinhos) ---
        {"nome": "olho_e", "cor": cor_preto, "pontos": [(8, 15), (9, 15), (9, 16), (8, 16)]},
        {"nome": "olho_d", "cor": cor_preto, "pontos": [(22, 15), (23, 15), (23, 16), (22, 16)]},

        # --- ÓCULOS (Vazados - Apenas contorno) ---
        # Convertidos de círculos para quadrados para funcionar no seu motor atual
        {"nome": "aro_e", "cor": cor_preto, "tipo": "apenas_contorno", "pontos": [(2, 9), (14, 9), (14, 21), (2, 21)]},
        {"nome": "aro_d", "cor": cor_preto, "tipo": "apenas_contorno", "pontos": [(16, 9), (28, 9), (28, 21), (16, 21)]},
        {"nome": "ponte_oculos", "cor": cor_preto, "tipo": "linha", "pontos": [(14, 15), (16, 15)]},

        # --- BOCA (Linha) ---
        {"nome": "boca", "cor": cor_boca, "tipo": "linha", "pontos": [(12, 25), (18, 25)]},

        # --- CORPO (Blusa) ---
        {"nome": "blusa", "cor": cor_blusa, "pontos": [(-5, 30), (35, 30), (35, 70), (-5, 70)]},

        # --- BRAÇOS ---
        {"nome": "braco_e", "cor": cor_pele, "pontos": [(-15, 30), (-5, 30), (-5, 60), (-15, 60)]},
        {"nome": "braco_d", "cor": cor_pele, "pontos": [(35, 30), (45, 30), (45, 60), (35, 60)]},

        # --- CALÇA ---
        {"nome": "calca_topo", "cor": cor_calca, "pontos": [(-5, 70), (35, 70), (35, 90), (-5, 90)]},
        {"nome": "perna_e", "cor": cor_calca, "pontos": [(0, 90), (12, 90), (12, 115), (0, 115)]},
        {"nome": "perna_d", "cor": cor_calca, "pontos": [(18, 90), (30, 90), (30, 115), (18, 115)]}
    ]

