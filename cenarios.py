from biblioteca import *



def getCachorro(marrom=False):
    if not marrom:
        c1, c2, c4 = (236, 178, 95), (244, 146, 71), (182, 0, 71)
    else:
        c1, c2, c4 = (143, 97, 60), (105, 68, 40), (66, 17, 31)
    c3 = (0, 0, 0)

    modelo = []
    modelo.append(getRetanguloPreenchido(-10, 0, 10, 15, c2, "orelha1"))
    modelo.append(getRetanguloPreenchido(0, 0, 25, 25, c1, "cabeca"))
    modelo.append(getRetanguloPreenchido(25, 0, 10, 15, c2, "orelha2"))
    modelo.append(getRetanguloPreenchido(2, 8, 5, 5, c3, "olho1"))
    modelo.append(getRetanguloPreenchido(15, 8, 5, 5, c3, "olho2"))
    modelo.append(getRetanguloPreenchido(5, 15, 5, 5, c4, "nariz"))
    modelo.append(getRetanguloPreenchido(10, 25, 80, 25, c1, "corpo"))
    modelo.append(getRetanguloPreenchido(85, 35, 30, 8, c1, "rabo"))
    modelo.append(getRetanguloPreenchido(15, 50, 8, 25, c1, "perna1"))
    modelo.append(getRetanguloPreenchido(30, 50, 8, 25, c1, "perna2"))
    modelo.append(getRetanguloPreenchido(60, 50, 8, 25, c1, "perna3"))
    modelo.append(getRetanguloPreenchido(75, 50, 8, 25, c1, "perna4"))
    return modelo

def getBanco(): 
    c1, c2, c3 = (186, 186, 178), (145, 145, 131), (110, 109, 102)
    modelo = []
    modelo.append(getRetanguloPreenchido(0, 0, 200, 20, c1, "assento"))
    modelo.append(getRetanguloPreenchido(10, -50, 180, 50, c2, "costas"))
    modelo.append(getRetanguloPreenchido(10, -40, 180, 5, c3, "detalhe1"))
    modelo.append(getRetanguloPreenchido(10, -20, 180, 5, c3, "detalhe2"))
    modelo.append(getRetanguloPreenchido(15, 20, 15, 30, c1, "pe1"))
    modelo.append(getRetanguloPreenchido(170, 20, 15, 30, c1, "pe2"))
    return modelo

def getJarro():
    c1, c2, c3, c4 = (100, 50, 0), (117, 94, 80), (26, 166, 19), (201, 58, 110)
    modelo = []
    modelo.append(getRetanguloPreenchido(15, -50, 10, 50, c1, "tronco"))
    modelo.append(getRetanguloPreenchido(0, -80, 40, 40, c3, "folha1"))
    modelo.append(getRetanguloPreenchido(10, -110, 20, 40, c3, "folha2"))
    modelo.append(getRetanguloPreenchido(15, -130, 10, 30, c3, "folha3"))
    modelo.append(getRetanguloPreenchido(0, 0, 40, 40, c2, "vaso"))
    modelo.append(getRetanguloPreenchido(0, -60, 10, 10, c4, "flor1"))
    modelo.append(getRetanguloPreenchido(30, -70, 10, 10, c4, "flor2"))
    modelo.append(getRetanguloPreenchido(10, -100, 10, 10, c4, "flor3"))
    return modelo

def getCarrinho():
    c1, c2, c3, c4, c5 = (193, 197, 209), (230, 101, 85), (116, 117, 120), (89, 89, 89), (38, 70, 166)
    t = 50
    modelo = []
    modelo.append(getRetanguloPreenchido(t, 0, t, t, c1, "quadrado_central"))
    modelo.append(getTrianguloPreenchido((t, 0), (t, t), (0, t), c1, "tri_esq"))
    modelo.append(getTrianguloPreenchido((2*t, 0), (2*t, t), (3*t, t), c1, "tri_dir"))
    modelo.append(getRetanguloPreenchido(0, t, 150, 40, c5, "base_azul"))
    modelo.append(getRetanguloPreenchido(0, t, 150, 15, c2, "faixa_vermelha"))
    modelo.append(getRetanguloPreenchido(10, t+40, 20, 30, c3, "roda1"))
    modelo.append(getRetanguloPreenchido(10, t+40, 10, 20, c4, "roda1_det"))
    modelo.append(getRetanguloPreenchido(120, t+40, 20, 30, c3, "roda2"))
    modelo.append(getRetanguloPreenchido(130, t+40, 10, 20, c4, "roda2_det"))
    return modelo

def getLixeiras():
    colors = [(217, 56, 56), (235, 198, 17), (50, 173, 31), (31, 46, 173)] # R, Y, G, B
    sup, dent = (107, 107, 107), (38, 38, 38)
    modelo = []
    modelo.append(getRetanguloPreenchido(0, 10, 10, 80, sup, "suporte_e"))
    modelo.append(getRetanguloPreenchido(180, 10, 10, 80, sup, "suporte_d"))

    for i, color in enumerate(colors):
        x_offset = 10 + (i * 45)
        modelo.append(getRetanguloPreenchido(x_offset, 0, 35, 60, color, f"lix_{i}"))
        modelo.append(getRetanguloPreenchido(x_offset+8, 10, 20, 10, dent, f"det_{i}"))
        if i < 3: 
            modelo.append(getRetanguloPreenchido(x_offset+28, 10, 20, 10, sup, f"sup_lat_{i}"))
    return modelo

def getMoita():
    c1, c2, c3, c4 = (108, 168, 84), (110, 10, 10), (161, 138, 104), (184, 32, 26)
    modelo = []
    modelo.append(getRetanguloPreenchido(0, 0, 160, 30, c1, "folha_b"))
    modelo.append(getRetanguloPreenchido(40, -20, 80, 50, c1, "folha_t"))
    modelo.append(getRetanguloPreenchido(20, 30, 10, 20, c2, "caule1"))
    modelo.append(getRetanguloPreenchido(70, 30, 10, 20, c2, "caule2"))
    modelo.append(getRetanguloPreenchido(125, 30, 10, 20, c2, "caule3"))
    modelo.append(getRetanguloPreenchido(-10, 50, 180, 25, c3, "jarro"))
    modelo.append(getRetanguloPreenchido(10, 10, 10, 10, c4, "f1"))
    modelo.append(getRetanguloPreenchido(60, -10, 8, 8, c4, "f2"))
    modelo.append(getRetanguloPreenchido(90, 10, 10, 10, c4, "f3"))
    modelo.append(getRetanguloPreenchido(140, 15, 8, 8, c4, "f4"))
    return modelo

def getCarro():
    c_car, c_wheel, c_win, c_light, c_plate = (54, 54, 54), (0, 0, 0), (168, 168, 168), (232, 219, 160), (255, 255, 255)
    modelo = []
    modelo.append(getRetanguloPreenchido(0, 0, 150, 100, c_car, "cabine"))
    modelo.append(getRetanguloPreenchido(-25, 60, 200, 50, c_car, "chassis"))
    modelo.append(getRetanguloPreenchido(0, 110, 20, 30, c_wheel, "roda1"))
    modelo.append(getRetanguloPreenchido(130, 110, 20, 30, c_wheel, "roda2"))
    modelo.append(getRetanguloPreenchido(-10, 70, 25, 25, c_light, "farol1"))
    modelo.append(getRetanguloPreenchido(130, 70, 25, 25, c_light, "farol2"))
    modelo.append(getRetanguloPreenchido(15, 10, 120, 40, c_win, "janela"))
    modelo.append(getRetanguloPreenchido(55, 80, 40, 20, c_plate, "placa"))
    return modelo

def getGato():
    c_p, c_d, c_n, preto = (128, 128, 128), (80, 80, 80), (255, 182, 193), (0, 0, 0)
    modelo = []
    modelo.append(getRetanguloPreenchido(0, -6, 6, 10, c_d, "orelha1"))
    modelo.append(getRetanguloPreenchido(12, -6, 6, 10, c_d, "orelha2"))
    modelo.append(getRetanguloPreenchido(0, 0, 18, 18, c_p, "cabeca"))
    modelo.append(getRetanguloPreenchido(3, 5, 3, 3, preto, "olho1"))
    modelo.append(getRetanguloPreenchido(12, 5, 3, 3, preto, "olho2"))
    modelo.append(getRetanguloPreenchido(8, 10, 3, 2, c_n, "nariz"))
    modelo.append(getLinha(-3, 10, 4, 11, preto, "bigode1"))
    modelo.append(getLinha(14, 11, 21, 10, preto, "bigode2"))
    modelo.append(getRetanguloPreenchido(8, 18, 40, 18, c_p, "corpo"))
    modelo.append(getRetanguloPreenchido(48, 22, 20, 4, c_p, "rabo"))
    modelo.append(getRetanguloPreenchido(9, 36, 6, 15, c_p, "p1"))
    modelo.append(getRetanguloPreenchido(19, 36, 6, 15, c_p, "p2"))
    modelo.append(getRetanguloPreenchido(32, 36, 6, 15, c_p, "p3"))
    modelo.append(getRetanguloPreenchido(42, 36, 6, 15, c_p, "p4"))
    return modelo

def getNuvem():
    cor_nuvem = (255, 255, 255) # Branco puro
    modelo = []
    
    modelo.append(getCirculoPreenchido(0, 0, 35, cor_nuvem, "centro"))
    modelo.append(getCirculoPreenchido(-30, 10, 25, cor_nuvem, "esq"))
    modelo.append(getCirculoPreenchido(30, 10, 25, cor_nuvem, "dir"))
    modelo.append(getRetanguloPreenchido(-30, 15, 60, 20, cor_nuvem, "base"))

    return modelo

def getBandeira():
    return [{
        "nome": "areabandeira",
        "cor": (0, 100, 0),
        "pontos": [(0, 0), (100, 0), (100, 80), (0, 80)],
        "uvs": [(0, 0), (1, 0), (1, 1), (0, 1)] 
    }]

def getTapioca(largura=22, altura=10):
    cx, cy = 0, 0
    resolucao = 30
    pontos = []
    
    for i in range(resolucao):
        rad = math.radians(i * (360 / resolucao))
        # Usa os valores passados nos parâmetros
        px = cx + largura * math.cos(rad)
        py = cy + altura * math.sin(rad)
        pontos.append((px, py))

    return [{
        "nome": "tapioca",
        "cor": (255, 255, 255),
        "pontos": pontos,
        "tipo": "padrao"
    }]
def getQueijo():
    # Cores
    cor_base = (255, 215, 0)   # Amarelo Ouro (o mesmo de antes)
    cor_buraco = (218, 165, 32) # Um tom mais escuro/alaranjado para o buraco

    modelo = []

    # 1. A Base retangular do queijo (Fatia deitada)
    # x=0, y=0, largura=25, altura=12
    modelo.append(getRetanguloPreenchido(0, 0, 25, 12, cor_base, "base_queijo"))

    # 2. Os Buracos
    # Vamos adicionar 3 buracos de tamanhos diferentes em posições variadas.
    # Usamos o "truque" de mudar o tipo para "padrao" para que eles sejam preenchidos.
    # Usamos uma resolução baixa (10 ou 12) porque são muito pequenos.

    # Buraco 1 (Esquerda, pequeno)
    # cx=5, cy=4, raio=2
    b1 = getCirculo(5, 4, 2, cor_buraco, "furo1", resolucao=12)
    b1["tipo"] = "padrao" # O TRUQUE para preencher
    modelo.append(b1)

    # Buraco 2 (Centro-direita, médio)
    # cx=15, cy=7, raio=3
    b2 = getCirculo(15, 7, 3, cor_buraco, "furo2", resolucao=12)
    b2["tipo"] = "padrao"
    modelo.append(b2)
    
    # Buraco 3 (Perto da borda direita, pequeno)
    # cx=21, cy=3, raio=1.5 (pode usar float no raio se seu getCirculo aceitar)
    b3 = getCirculo(21, 3, 1.5, cor_buraco, "furo3", resolucao=10)
    b3["tipo"] = "padrao"
    modelo.append(b3)

    return modelo

DADOS_DO_CENARIO = [
    {"modelo": getMoita(),    "x": 420,  "y": 260},
    {"modelo": getCarrinho(), "x": 100,  "y": 350},
    {"modelo": getJarro(),    "x": 30,   "y": 290},
    {"modelo": getBanco(),    "x": 700,  "y": 300},
    {"modelo": getCachorro(), "x": 500,  "y": 400},
    {"modelo": getCachorro(marrom=True), "x": 700, "y": 600},
    {"modelo": getCarro(),    "x": 1073, "y": 400},
    {"modelo": getLixeiras(), "x": 1050, "y": 250},
    {"modelo": getGato(),     "x": 800,  "y": 500},
    {"modelo": getNuvem(), "x": 350, "y": 130},
    {"modelo": getNuvem(), "x": 600, "y": 80},
    {"modelo": getNuvem(), "x": 900, "y": 120},
    {"modelo": getNuvem(), "x": 1100, "y": 60},
    {"modelo": getTapioca(),  "x": 175,  "y": 355}, 
    {"modelo": getTapioca(largura=25, altura=13),  "x": 173,  "y": 380},
]