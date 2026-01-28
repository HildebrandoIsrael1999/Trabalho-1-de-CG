from biblioteca import *
from matrizes import *


def getBilly():
    
    cor_pele = (179, 139, 109)
    cor_roupa = (255, 0, 0)
    cor_branco = (255, 255, 255)
    cor_preto = (0, 0, 0)
    
    modelo = []

    modelo.append(getRetanguloPreenchido(0, 0, 30, 30, cor_pele, "cabeca"))
    modelo.append(getRetanguloPreenchido(-5, 30, 40, 50, cor_roupa, "corpo"))
    modelo.append(getRetanguloPreenchido(-5, 30, 40, 50, cor_branco, "jaleco"))
    modelo.append(getRetanguloPreenchido(12, 30, 6, 50, cor_roupa, "abertura_jaleco"))
    modelo.append(getRetanguloPreenchido(0, -5, 30, 10, cor_branco, "bone_topo"))
    modelo.append(getRetanguloPreenchido(15, 0, 20, 5, cor_branco, "bone_aba"))
    modelo.append(getRetanguloPreenchido(5, 12, 5, 5, cor_preto, "olho_e"))
    modelo.append(getRetanguloPreenchido(20, 12, 5, 5, cor_preto, "olho_d"))
    modelo.append(getRetanguloPreenchido(-15, 35, 10, 30, cor_pele, "braco_e"))
    modelo.append(getRetanguloPreenchido(35, 35, 10, 30, cor_pele, "braco_d"))
    modelo.append(getRetanguloPreenchido(0, 80, 10, 30, cor_pele, "perna_e"))
    modelo.append(getRetanguloPreenchido(20, 80, 10, 30, cor_pele, "perna_d"))
    modelo.append(getQuadrado(3, 10, 9, 9, cor_preto, "aro_e"))
    modelo.append(getQuadrado(18, 10, 9, 9, cor_preto, "aro_d"))
    modelo.append(getLinha(12, 15, 18, 15, cor_preto, "ponte"))
    modelo.append(getLinha(10, 23, 20, 23, cor_roupa, "boca"))

    return modelo

def getMulher():
    # Cores
    cor_pele = (179, 139, 109)
    cor_mecha_rosa = (255, 105, 180)
    cor_olho = (0, 0, 0)
    cor_vestido = (255, 150, 200)
    cor_cabelo = (0, 0, 0)
    cor_boca = (255, 0, 0)

    modelo = []

    modelo.append(getRetanguloPreenchido(-5, 0, 5, 20, cor_cabelo, "cabelo_esq"))
    modelo.append(getRetanguloPreenchido(30, 0, 5, 20, cor_cabelo, "cabelo_dir"))
    modelo.append(getRetanguloPreenchido(0, -10, 30, 15, cor_cabelo, "cabelo_topo"))
    modelo.append(getRetanguloPreenchido(0, 0, 30, 30, cor_pele, "cabeca"))
    modelo.append(getRetanguloPreenchido(10, -5, 5, 15, cor_mecha_rosa, "mecha"))
    modelo.append(getRetanguloPreenchido(5, 10, 5, 5, cor_olho, "olho_e"))
    modelo.append(getRetanguloPreenchido(20, 10, 5, 5, cor_olho, "olho_d"))
    modelo.append(getRetanguloPreenchido(-5, 30, 40, 60, cor_vestido, "vestido"))
    modelo.append(getRetanguloPreenchido(-15, 35, 10, 30, cor_pele, "braco_e"))
    modelo.append(getRetanguloPreenchido(35, 35, 10, 30, cor_pele, "braco_d"))
    modelo.append(getRetanguloPreenchido(0, 90, 10, 30, cor_pele, "perna_e"))
    modelo.append(getRetanguloPreenchido(20, 90, 10, 30, cor_pele, "perna_d"))
    modelo.append(getLinha(10, 23, 20, 23, cor_boca, "boca"))

    return modelo

def getMenino():
    
    cor_pele = (255, 224, 189)
    cor_cabelo = (0, 0, 0)
    cor_blusa = (173, 216, 230)
    cor_calca = (0, 0, 139)
    cor_preto = (0, 0, 0)
    cor_boca = (200, 0, 0)

    modelo = []
    
    modelo.append(getRetanguloPreenchido(0, -5, 30, 15, cor_cabelo, "cabelo"))
    modelo.append(getRetanguloPreenchido(0, 0, 30, 30, cor_pele, "cabeca"))
    modelo.append(getRetanguloPreenchido(8, 15, 1, 1, cor_preto, "olho_e"))
    modelo.append(getRetanguloPreenchido(22, 15, 1, 1, cor_preto, "olho_d"))
    modelo.append(getCirculo(cx=8, cy=15, raio=6, cor=cor_preto, nome="aro_e", resolucao=40))
    modelo.append(getCirculo(cx=22, cy=15, raio=6, cor=cor_preto, nome="aro_d", resolucao=40))
    modelo.append(getLinha(14, 15, 16, 15, cor_preto, "ponte_oculos"))
    modelo.append(getLinha(12, 25, 18, 25, cor_boca, "boca"))
    modelo.append(getRetanguloPreenchido(-5, 30, 40, 40, cor_blusa, "blusa"))
    modelo.append(getRetanguloPreenchido(-15, 30, 10, 30, cor_pele, "braco_e"))
    modelo.append(getRetanguloPreenchido(35, 30, 10, 30, cor_pele, "braco_d"))
    modelo.append(getRetanguloPreenchido(-5, 70, 40, 20, cor_calca, "calca_topo"))
    modelo.append(getRetanguloPreenchido(0, 90, 12, 25, cor_calca, "perna_e"))
    modelo.append(getRetanguloPreenchido(18, 90, 12, 25, cor_calca, "perna_d"))

    return modelo

