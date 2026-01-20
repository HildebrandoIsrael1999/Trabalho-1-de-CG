from biblioteca import *

def setBilly(superficie, x, y):
    cor_pele = (179, 139, 109)
    cor_roupa = (255, 0, 0)  # Camisa vermelha por baixo
    cor_branco = (255, 255, 255) # Cor do boné e jaleco
    cor_boca = (255, 0, 0) # Vermelho puro para boca ficar lindinha
    
    # --- CORPO ---
    setPreencherRetangulo(superficie, x - 5, y + 30, 40, 50, cor_roupa)
    
    # --- JALECO BRANCO  ---
    # Deixamos uma bordinha da camisa vermelha aparecendo se quiser, 
    # ou cobrimos quase tudo.
    setPreencherRetangulo(superficie, x - 5, y + 30, 40, 50, cor_branco)
    # Detalhe: um retângulo fino vermelho no meio para parecer o jaleco aberto
    setPreencherRetangulo(superficie, x + 12, y + 30, 6, 50, cor_roupa)

    # --- CABEÇA ---
    setPreencherRetangulo(superficie, x, y, 30, 30, cor_pele)
    
    # --- BONÉ BRANCO ---
    # Parte de cima do boné
    setPreencherRetangulo(superficie, x, y - 5, 30, 10, cor_branco) 
    # Aba do boné (um retângulo que sai para o lado)
    setPreencherRetangulo(superficie, x + 15, y, 20, 5, cor_branco)

    # --- OLHOS ---
    setPreencherRetangulo(superficie, x + 5, y + 12, 5, 5, (0, 0, 0))
    setPreencherRetangulo(superficie, x + 20, y + 12, 5, 5, (0, 0, 0))

    # --- BRAÇOS ---
    setPreencherRetangulo(superficie, x - 15, y + 35, 10, 30, cor_pele)
    setPreencherRetangulo(superficie, x + 35, y + 35, 10, 30, cor_pele)

    # --- PERNAS ---
    setPreencherRetangulo(superficie, x, y + 80, 10, 30, cor_pele)
    setPreencherRetangulo(superficie, x + 20, y + 80, 10, 30, cor_pele)
    # --- ÓCULOS --
    # Aro Esquerdo (ao redor do olho esquerdo)
    setQuadrado(superficie, x + 3, y + 10, 9, (0, 0, 0))
    
    # Aro Direito (ao redor do olho direito)
    # x + 18 para ficar centralizado no olho que está em x + 20
    setQuadrado(superficie, x + 18, y + 10, 9, (0, 0, 0))
    
    # Ponte dos óculos (uma pequena linha ligando os dois quadrados)
    setRetaBresenham(superficie, x + 12, y + 15, x + 18, y + 15, (0, 0, 0))
    # --- BOCA (Reta Vermelha) ---
    setRetaBresenham(superficie, x + 10, y + 23, x + 20, y + 23, cor_boca)
    
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