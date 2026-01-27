import pygame
from biblioteca import setPreencherRetanguloFloodfill

COR_FUNDO_MENU = (59, 58, 56)
COR_CONTORNO   = (0, 0, 0)
COR_TXT         = (255, 255, 255)

pygame.font.init()

try:
    fonte_titulo = pygame.font.Font("./Fontes/RubikDirt-Regular.ttf", 100)
except FileNotFoundError:
    print("Erro: Arquivo Oi-Regular.ttf não encontrado. Usando fonte padrão.")
    fonte_titulo = pygame.font.SysFont("Arial", 90, bold=True)

#Fonte para os botões
fonte_ui = pygame.font.SysFont("Arial", 40, bold=True)

def getBotao(x, y, largura, altura, cor_fundo, texto):
    surf_texto = fonte_ui.render(texto, True, COR_TXT)
    txt_w, txt_h = surf_texto.get_size()
    
    txt_x = x + (largura - txt_w) // 2
    txt_y = y + (altura - txt_h) // 2

    return {
        "tipo": "botao",
        "x": x, "y": y,
        "w": largura, "h": altura,
        "cor": cor_fundo,
        "texto_surf": surf_texto,
        "txt_pos": (txt_x, txt_y)
    }

def desenhar_botao_customizado(tela, botao):
    #Usa a função da sua biblioteca para preencher com Floodfill
    setPreencherRetanguloFloodfill(tela, botao["x"], botao["y"], botao["w"], botao["h"], COR_CONTORNO, botao["cor"])
    #Desenha o texto por cima
    tela.blit(botao["texto_surf"], botao["txt_pos"])

def executar_menu_principal(tela, largura_tela, altura_tela):

    surf_titulo = fonte_titulo.render("TAPIOCARIA DO BILLY", True, COR_TXT)
    rect_titulo = surf_titulo.get_rect(center=(largura_tela // 2, 150))

    btn_jogar = getBotao(largura_tela//2 - 100, 320, 200, 80, (103, 173, 57), "JOGAR")
    btn_sair   = getBotao(largura_tela//2 - 100, 470, 200, 80, (196, 72, 39), "SAIR")
    
    rect_jogar = pygame.Rect(btn_jogar["x"], btn_jogar["y"], btn_jogar["w"], btn_jogar["h"])
    rect_sair = pygame.Rect(btn_sair["x"], btn_sair["y"], btn_sair["w"], btn_sair["h"])

    clock = pygame.time.Clock()
    rodando_menu = True
    
    while rodando_menu:
        mx, my = pygame.mouse.get_pos()
        
        if rect_jogar.collidepoint(mx, my) or rect_sair.collidepoint(mx, my):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) #reseta o cursor
                return False 
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if rect_jogar.collidepoint(mx, my):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) #reseta o cursor
                    return True 
                
                if rect_sair.collidepoint(mx, my):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) #reseta o cursor
                    return False

        tela.fill(COR_FUNDO_MENU)
        tela.blit(surf_titulo, rect_titulo)
        
        desenhar_botao_customizado(tela, btn_jogar)
        desenhar_botao_customizado(tela, btn_sair)
        
        pygame.display.flip()
        clock.tick(60)