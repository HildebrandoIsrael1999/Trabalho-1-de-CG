# Constantes de Região (Códigos de Bit)
INSIDE = 0  # 0000
LEFT   = 1  # 0001
RIGHT  = 2  # 0010
BOTTOM = 4  # 0100
TOP    = 8  # 1000

def calcular_codigo_regiao(x, y, x_min, y_min, x_max, y_max):
    code = INSIDE
    
    if x < x_min:      # À esquerda da janela
        code |= LEFT
    elif x > x_max:    # À direita da janela
        code |= RIGHT
        
    if y < y_min:      # Abaixo da janela
        code |= BOTTOM
    elif y > y_max:    # Acima da janela
        code |= TOP
        
    return code

def cohenSutherlandClip(x1, y1, x2, y2, x_min, y_min, x_max, y_max):
    code1 = calcular_codigo_regiao(x1, y1, x_min, y_min, x_max, y_max)
    code2 = calcular_codigo_regiao(x2, y2, x_min, y_min, x_max, y_max)
    
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        

        elif (code1 & code2) != 0:
            break
        
        else:
            x = 0
            y = 0
            code_out = code1 if code1 != 0 else code2
            
            # Fórmulas de interseção (y = y1 + m * (x - x1))

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
                

            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
                

            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
                

            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min
            

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = calcular_codigo_regiao(x1, y1, x_min, y_min, x_max, y_max)
            else:
                x2 = x
                y2 = y
                code2 = calcular_codigo_regiao(x2, y2, x_min, y_min, x_max, y_max)

    if accept:
        return int(x1), int(y1), int(x2), int(y2)
    else:
        return None