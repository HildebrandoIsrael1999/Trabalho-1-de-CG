from biblioteca import *
from matrizes import *

def getCachorro(marrom=False):
    # Alterna entre o cachorro amarelo e o marrom
    if not marrom:
        c1, c2, c4 = (236, 178, 95), (244, 146, 71), (182, 0, 71)
    else:
        c1, c2, c4 = (143, 97, 60), (105, 68, 40), (66, 17, 31)
    c3 = (0, 0, 0)

    return [
        {"nome": "orelha1", "cor": c2, "pontos": [(-10, 0), (0, 0), (0, 15), (-10, 15)]},
        {"nome": "cabeca", "cor": c1, "pontos": [(0, 0), (25, 0), (25, 25), (0, 25)]},
        {"nome": "orelha2", "cor": c2, "pontos": [(25, 0), (35, 0), (35, 15), (25, 15)]},
        {"nome": "olho1", "cor": c3, "pontos": [(2, 8), (7, 8), (7, 13), (2, 13)]},
        {"nome": "olho2", "cor": c3, "pontos": [(15, 8), (20, 8), (20, 13), (15, 13)]},
        {"nome": "nariz", "cor": c4, "pontos": [(5, 15), (10, 15), (10, 20), (5, 20)]},
        {"nome": "corpo", "cor": c1, "pontos": [(10, 25), (90, 25), (90, 50), (10, 50)]},
        {"nome": "rabo", "cor": c1, "pontos": [(85, 35), (115, 35), (115, 43), (85, 43)]},
        {"nome": "perna1", "cor": c1, "pontos": [(15, 50), (23, 50), (23, 75), (15, 75)]},
        {"nome": "perna2", "cor": c1, "pontos": [(30, 50), (38, 50), (38, 75), (30, 75)]},
        {"nome": "perna3", "cor": c1, "pontos": [(60, 50), (68, 50), (68, 75), (60, 75)]},
        {"nome": "perna4", "cor": c1, "pontos": [(75, 50), (83, 50), (83, 75), (75, 75)]}
    ]

def getBanco():
    c1, c2, c3 = (186, 186, 178), (145, 145, 131), (110, 109, 102)
    return [
        {"nome": "assento", "cor": c1, "pontos": [(0, 0), (200, 0), (200, 20), (0, 20)]},
        {"nome": "costas", "cor": c2, "pontos": [(10, -50), (190, -50), (190, 0), (10, 0)]},
        {"nome": "detalhe1", "cor": c3, "pontos": [(10, -40), (190, -40), (190, -35), (10, -35)]},
        {"nome": "detalhe2", "cor": c3, "pontos": [(10, -20), (190, -20), (190, -15), (10, -15)]},
        {"nome": "pe1", "cor": c1, "pontos": [(15, 20), (30, 20), (30, 50), (15, 50)]},
        {"nome": "pe2", "cor": c1, "pontos": [(170, 20), (185, 20), (185, 50), (170, 50)]}
    ]

def getJarro():
    c1, c2, c3, c4 = (100, 50, 0), (117, 94, 80), (26, 166, 19), (201, 58, 110)
    return [
        {"nome": "tronco", "cor": c1, "pontos": [(15, -50), (25, -50), (25, 0), (15, 0)]},
        {"nome": "folha1", "cor": c3, "pontos": [(0, -80), (40, -80), (40, -40), (0, -40)]},
        {"nome": "folha2", "cor": c3, "pontos": [(10, -110), (30, -110), (30, -70), (10, -70)]},
        {"nome": "folha3", "cor": c3, "pontos": [(15, -130), (25, -130), (25, -100), (15, -100)]},
        {"nome": "vaso", "cor": c2, "pontos": [(0, 0), (40, 0), (40, 40), (0, 40)]},
        {"nome": "flor1", "cor": c4, "pontos": [(0, -60), (10, -60), (10, -50), (0, -50)]},
        {"nome": "flor2", "cor": c4, "pontos": [(30, -70), (40, -70), (40, -60), (30, -60)]},
        {"nome": "flor3", "cor": c4, "pontos": [(10, -100), (20, -100), (20, -90), (10, -90)]}
    ]

def getCarrinho():
    c1, c2, c3, c4, c5 = (193, 197, 209), (230, 101, 85), (116, 117, 120), (89, 89, 89), (38, 70, 166)
    t = 50
    return [
        {"nome": "quadrado_central", "cor": c1, "pontos": [(t, 0), (2*t, 0), (2*t, t), (t, t)]},
        {"nome": "tri_esq", "cor": c1, "pontos": [(t, 0), (t, t), (0, t)]},
        {"nome": "tri_dir", "cor": c1, "pontos": [(2*t, 0), (2*t, t), (3*t, t)]},
        {"nome": "base_azul", "cor": c5, "pontos": [(0, t), (150, t), (150, t+40), (0, t+40)]},
        {"nome": "faixa_vermelha", "cor": c2, "pontos": [(0, t), (150, t), (150, t+15), (0, t+15)]},
        {"nome": "roda1", "cor": c3, "pontos": [(10, t+40), (30, t+40), (30, t+70), (10, t+70)]},
        {"nome": "roda1_det", "cor": c4, "pontos": [(10, t+40), (20, t+40), (20, t+60), (10, t+60)]},
        {"nome": "roda2", "cor": c3, "pontos": [(120, t+40), (140, t+40), (140, t+70), (120, t+70)]},
        {"nome": "roda2_det", "cor": c4, "pontos": [(130, t+40), (140, t+40), (140, t+60), (130, t+60)]}
    ]

def getLixeiras():
    colors = [(217, 56, 56), (235, 198, 17), (50, 173, 31), (31, 46, 173)] # R, Y, G, B
    sup, dent = (107, 107, 107), (38, 38, 38)
    
    modelo = [
        {"nome": "suporte_e", "cor": sup, "pontos": [(0, 10), (10, 10), (10, 90), (0, 90)]},
        {"nome": "suporte_d", "cor": sup, "pontos": [(180, 10), (190, 10), (190, 90), (180, 90)]}
    ]
    
    for i, color in enumerate(colors):
        x_offset = 10 + (i * 45)
        modelo.append({"nome": f"lix_{i}", "cor": color, "pontos": [(x_offset, 0), (x_offset+35, 0), (x_offset+35, 60), (x_offset, 60)]})
        modelo.append({"nome": f"det_{i}", "cor": dent, "pontos": [(x_offset+8, 10), (x_offset+28, 10), (x_offset+28, 20), (x_offset+8, 20)]})
        if i < 3: # Suportes entre lixeiras
            modelo.append({"nome": f"sup_lat_{i}", "cor": sup, "pontos": [(x_offset+28, 10), (x_offset+48, 10), (x_offset+48, 20), (x_offset+28, 20)]})
            
    return modelo

def getMoita():
    c1, c2, c3, c4 = (108, 168, 84), (110, 10, 10), (161, 138, 104), (184, 32, 26)
    return [
        {"nome": "folha_b", "cor": c1, "pontos": [(0, 0), (160, 0), (160, 30), (0, 30)]},
        {"nome": "folha_t", "cor": c1, "pontos": [(40, -20), (120, -20), (120, 30), (40, 30)]},
        {"nome": "caule1", "cor": c2, "pontos": [(20, 30), (30, 30), (30, 50), (20, 50)]},
        {"nome": "caule2", "cor": c2, "pontos": [(70, 30), (80, 30), (80, 50), (70, 50)]},
        {"nome": "caule3", "cor": c2, "pontos": [(125, 30), (135, 30), (135, 50), (125, 50)]},
        {"nome": "jarro", "cor": c3, "pontos": [(-10, 50), (170, 50), (170, 75), (-10, 75)]},
        {"nome": "f1", "cor": c4, "pontos": [(10, 10), (20, 10), (20, 20), (10, 20)]},
        {"nome": "f2", "cor": c4, "pontos": [(60, -10), (68, -10), (68, -2), (60, -2)]},
        {"nome": "f3", "cor": c4, "pontos": [(90, 10), (100, 10), (100, 20), (90, 20)]},
        {"nome": "f4", "cor": c4, "pontos": [(140, 15), (148, 15), (148, 23), (140, 23)]}
    ]

def getCarro():
    c_car, c_wheel, c_win, c_light, c_plate = (54, 54, 54), (0, 0, 0), (168, 168, 168), (232, 219, 160), (255, 255, 255)
    return [
        {"nome": "cabine", "cor": c_car, "pontos": [(0, 0), (150, 0), (150, 100), (0, 100)]},
        {"nome": "chassis", "cor": c_car, "pontos": [(-25, 60), (175, 60), (175, 110), (-25, 110)]},
        {"nome": "roda1", "cor": c_wheel, "pontos": [(0, 110), (20, 110), (20, 140), (0, 140)]},
        {"nome": "roda2", "cor": c_wheel, "pontos": [(130, 110), (150, 110), (150, 140), (130, 140)]},
        {"nome": "farol1", "cor": c_light, "pontos": [(-10, 70), (15, 70), (15, 95), (-10, 95)]},
        {"nome": "farol2", "cor": c_light, "pontos": [(130, 70), (155, 70), (155, 95), (130, 95)]},
        {"nome": "janela", "cor": c_win, "pontos": [(15, 10), (135, 10), (135, 50), (15, 50)]},
        {"nome": "placa", "cor": c_plate, "pontos": [(55, 80), (95, 80), (95, 100), (55, 100)]}
    ]

def getGato():
    c_p, c_d, c_n, preto = (128, 128, 128), (80, 80, 80), (255, 182, 193), (0, 0, 0)
    return [
        {"nome": "orelha1", "cor": c_d, "pontos": [(0, -6), (6, -6), (6, 4), (0, 4)]},
        {"nome": "orelha2", "cor": c_d, "pontos": [(12, -6), (18, -6), (18, 4), (12, 4)]},
        {"nome": "cabeca", "cor": c_p, "pontos": [(0, 0), (18, 0), (18, 18), (0, 18)]},
        {"nome": "olho1", "cor": preto, "pontos": [(3, 5), (6, 5), (6, 8), (3, 8)]},
        {"nome": "olho2", "cor": preto, "pontos": [(12, 5), (15, 5), (15, 8), (12, 8)]},
        {"nome": "nariz", "cor": c_n, "pontos": [(8, 10), (11, 10), (11, 12), (8, 12)]},
        {"nome": "bigode1", "cor": preto, "tipo": "linha", "pontos": [(-3, 10), (4, 11)]},
        {"nome": "bigode2", "cor": preto, "tipo": "linha", "pontos": [(14, 11), (21, 10)]},
        {"nome": "corpo", "cor": c_p, "pontos": [(8, 18), (48, 18), (48, 36), (8, 36)]},
        {"nome": "rabo", "cor": c_p, "pontos": [(48, 22), (68, 22), (68, 26), (48, 26)]},
        {"nome": "p1", "cor": c_p, "pontos": [(9, 36), (15, 36), (15, 51), (9, 51)]},
        {"nome": "p2", "cor": c_p, "pontos": [(19, 36), (25, 36), (25, 51), (19, 51)]},
        {"nome": "p3", "cor": c_p, "pontos": [(32, 36), (38, 36), (38, 51), (32, 51)]},
        {"nome": "p4", "cor": c_p, "pontos": [(42, 36), (48, 36), (48, 51), (42, 51)]}
    ]
    