# Documentação - Billy da Tapioca
## Sistema de Renderização Gráfica 2D com Transformações Afins

### Descrição Geral

Este projeto implementa um motor gráfico 2D educacional que demonstra os conceitos fundamentais de computação gráfica. O objetivo principal é criar uma cena 2D com personagens que possam ser transformados (escalados, rotacionados e transladados) em tempo real através da entrada do teclado, com renderização de viewport (mini-mapa) no canto da tela.

**Conceitos principais abordados:**
- Construção de personagens através de primitivas geométricas
- Transformações afins usando multiplicação de matrizes
- Algoritmos de rasterização (Bresenham, Scanline)
- Clipping de linhas (Cohen-Sutherland)
- Transformação entre espaços de coordenadas (mundo → viewport)

---

## 1. Modelagem de Personagens

### 1.1 A Lógica por Trás da Construção

A ideia central é que **qualquer personagem complexo pode ser decomposto em formas geométricas simples** (retângulos, triângulos e linhas). Por exemplo, Billy é composto por:
- Um retângulo para a cabeça
- Retângulos para corpo, braços e pernas
- Linhas para detalhes como a boca e ponte de óculos

Cada personagem é construído com uma **origem de referência** (geralmente a cabeça), permitindo que todas as partes se movimentem juntas quando transformações são aplicadas.

### 1.2 Estrutura de Dados - O que é um "Modelo"

Cada personagem é retornado como uma **lista de dicionários**, onde cada dicionário representa uma parte do corpo:

```python
modelo = [
    {
        "nome": "cabeca",
        "cor": (179, 139, 109),      # RGB da cor da pele
        "tipo": "padrao",             # Como renderizar
        "pontos": [(0, 0), (30, 0), (30, 30), (0, 30)]  # Vértices do polígono
    },
    {
        "nome": "boca",
        "cor": (255, 0, 0),
        "tipo": "linha",              # Linhas não fecham o polígono
        "pontos": [(10, 23), (20, 23)]
    }
]
```

**Por que estruturar assim?**
- Separar dados (pontos, cores) da lógica de renderização
- Permitir transformações uniformes em todas as partes
- Facilitar a reutilização de código entre personagens

### 1.3 Funções de Construção no arquivo personagens.py

#### `getBilly()`

Retorna uma lista contendo todos os componentes visuais de Billy:

```python
def getBilly():
    # Definimos uma paleta de cores reutilizável
    cor_pele = (179, 139, 109)
    cor_roupa = (255, 0, 0)
    cor_branco = (255, 255, 255)
    cor_preto = (0, 0, 0)
    
    modelo = []
    
    # Adicionamos cada parte do personagem
    modelo.append(getRetanguloPreenchido(0, 0, 30, 30, cor_pele, "cabeca"))
    modelo.append(getRetanguloPreenchido(-5, 30, 40, 50, cor_roupa, "corpo"))
    # ... mais componentes
    
    return modelo  # Retorna a lista completa
```

**Estratégia de posicionamento:**
- A cabeça começa em (0, 0) - essa é nossa origem
- O corpo fica em (-5, 30), ou seja, ligeiramente deslocado para a esquerda e para baixo
- Pernas começam em y=80 (abaixo do corpo que termina em y=80)

**Componentes principais de Billy:**

| Componente | Posição | Dimensões | Propósito |
|---|---|---|---|
| Cabeça | (0, 0) | 30×30 | Forma base do rosto |
| Olhos | (5,12) e (20,12) | 5×5 cada | Expressão |
| Boné | (0, -5) e (15, 0) | 30×10 e 20×5 | Acessório |
| Corpo | (-5, 30) | 40×50 | Tronco |
| Jaleco | (-5, 30) | 40×50 | Camada branca sobre o corpo |
| Braços | (-15, 35) e (35, 35) | 10×30 | Membros superiores |
| Pernas | (0, 80) e (20, 80) | 10×30 | Membros inferiores |
| Óculos | (3,10) e (18,10) | 9×9 | Acessório (apenas contorno) |
| Boca | (10,23) → (20,23) | - | Linha de expressão |

**Observação importante:** Os óculos têm tipo `"apenas_contorno"` (não preenchidos), enquanto a boca tem tipo `"linha"` (não fecha o polígono para não deformar a forma).

#### `getMulher()` e `getMenino()`

Seguem a mesma lógica, mas com cores e proporções diferentes:
- **Clara (Mulher)**: Cabelo preto, mecha rosa, vestido rosa - escala 0.9 (ligeiramente menor)
- **Menino**: Blusa azul claro, calça azul escuro, óculos redondos

---

## 2. O Processo de Renderização

### 2.1 Por que usar Primitivas Geométricas?

Em vez de carregar imagens (sprites), construímos personagens com formas matemáticas simples. Isso oferece:
- **Controle total**: Podemos transformar cada pixel com precisão
- **Escalabilidade**: Um personagem fica bem em qualquer tamanho
- **Aprendizado**: Entendemos como funcionam algoritmos de rasterização
- **Eficiência**: Menos dados para transmitir e processar

### 2.2 A Função `getRetanguloPreenchido()` - Criando Primitivas

Esta função (em biblioteca.py) **encapsula a criação de retângulos**:

```python
def getRetanguloPreenchido(x, y, w, h, cor, nome="retangulo"):
    return {
        "nome": nome,
        "cor": cor,
        "pontos": [
            (x, y),           # Canto superior esquerdo
            (x + w, y),       # Canto superior direito
            (x + w, y + h),   # Canto inferior direito
            (x, y + h)        # Canto inferior esquerdo
        ]
    }
```

**Por que retornar um dicionário?**
- Cada componente é uma unidade independente
- Carrega informações de cor e tipo junto com os pontos
- Facilita a busca por componentes específicos no modelo

**Outras primitivas:**
- `getTrianguloPreenchido(p1, p2, p3, cor, nome)` - Cria triângulos
- `getLinha(x1, y1, x2, y2, cor, nome)` - Cria linhas (tipo: "linha")
- `getQuadrado(x, y, w, h, cor, nome)` - Cria apenas o contorno (tipo: "apenas_contorno")

---

## 3. Transformações Usando Matrizes

### 3.1 O Problema que Queremos Resolver

Quando um jogador pressiona uma tecla, o personagem deve:
1. **Mudar de tamanho** (escala)
2. **Girar** (rotação)
3. **Sair do lugar** (translação)

A solução matemática elegante é usar **matrizes 3×3 em coordenadas homogêneas**:

```
[x']   [a  b  tx] [x]
[y'] = [c  d  ty] [y]
[1 ]   [0  0  1 ] [1]
```

Onde:
- `a, b, c, d` controlam escala e rotação
- `tx, ty` controlam translação

### 3.2 Por que Matrizes?

Matrizes permitem **compor transformações**:
- Aplicar escala
- Depois rotação
- Depois translação

Tudo em uma **única multiplicação** ao final, em vez de fazer 3 operações separadas em cada ponto. Isso economiza processamento!

### 3.3 A Função `calcularMatriz()` em matrizes.py

```python
def calcularMatriz(esc, ang, x, y):
    m = identidade()                      # Começa com identidade [1, 0, 0; ...]
    m = multiplicaMatrizes(escala(esc, esc), m)
    m = multiplicaMatrizes(rotacao(ang), m)
    m = multiplicaMatrizes(translacao(x, y), m)
    return m
```

**Fluxo lógico:**
1. Começa com a matriz identidade (sem transformação)
2. Multiplica pela matriz de escala (redimensiona)
3. Multiplica pela matriz de rotação (gira)
4. Multiplica pela matriz de translação (move para a posição final)

**A ordem é crítica!** Se trocássemos a ordem, o resultado seria diferente:
- Escala → Rotação → Translação ✅ (correto)
- Translação → Rotação → Escala ❌ (posições ficariam erradas)

Isso é porque a **composição de matrizes não é comutativa** - `A × B ≠ B × A`.

### 3.4 Aplicando a Transformação aos Pontos

A função `aplicaTransformacao()` aplica a matriz calculada a cada ponto:

```python
def aplicaTransformacao(m, pontos):
    novos = []
    for x, y in pontos:
        # Transforma (x, y) usando a matriz m
        nx = m[0][0]*x + m[0][1]*y + m[0][2]
        ny = m[1][0]*x + m[1][1]*y + m[1][2]
        novos.append((nx, ny))
    return novos
```

Essa função converte as **coordenadas do personagem** (no seu sistema de coordenadas local) para **coordenadas da tela** (após escala, rotação e translação).

---

## 4. Renderizando o Personagem na Tela

### 4.1 A Função `renderizarPersonagem()` - O Coração do Sistema

Esta função recebe:
- A tela (superfície Pygame)
- O modelo (lista de componentes)
- A matriz de transformação

E realiza o seguinte processo:

```python
def renderizarPersonagem(superficie, modelo, matriz):
    for parte in modelo:
        # 1. Extrai os dados da parte
        pts_trans = aplicaTransformacao(matriz, parte["pontos"])
        cor = parte["cor"]
        tipo = parte.get("tipo", "padrao")
        
        # 2. Se é um polígono sólido, preenche
        if len(pts_trans) > 2 and tipo != "apenas_contorno" and tipo != "linha":
            scanlineFill(superficie, pts_trans, cor)
        
        # 3. Desenha o contorno
        n = len(pts_trans)
        for i in range(n):
            # Para linhas, não fecha o polígono
            if tipo == "linha" and i == n - 1:
                break
            
            p1 = pts_trans[i]
            p2 = pts_trans[(i + 1) % n]
            
            setRetaRecortada(superficie, int(p1[0]), int(p1[1]), 
                           int(p2[0]), int(p2[1]), cor)
```

**O algoritmo em passos:**

1. **Transforma todos os pontos**: Aplica a matriz ao modelo
2. **Preenche o interior** (se aplicável): Usa Scanline para preencher com cor sólida
3. **Desenha o contorno**: Conecta os pontos com linhas recortadas

**Lógica de tipos:**
- `"padrao"`: Preenche interior + desenha contorno = polígono sólido
- `"apenas_contorno"`: Só desenha contorno = quadrado vazio
- `"linha"`: Desenha pontos sem fechar = detalhes como boca

### 4.2 Os Algoritmos Auxiliares

#### Scanline Fill (Preencher Polígonos)

Este algoritmo **preenche um polígono varredura por varredura** (linha horizontal por linha):

1. Encontra o Y mínimo e máximo do polígono
2. Para cada linha horizontal entre Y min e Y max:
   - Calcula onde a linha horizontal intersecta os lados do polígono
   - Ordena as interseções
   - Preenche os pixels entre pares de interseções

**Vantagem**: Funciona com polígonos de qualquer forma, não apenas retângulos!

#### Bresenham (Desenhar Linhas)

Desenha uma linha usando apenas **pixels inteiros**, evitando desperdício:

- Começa em um ponto
- Decide qual próximo pixel está mais próximo da linha matemática
- Continua até o ponto final

**Por que Bresenham?** Porque é rápido (apenas somas inteiras, sem divisões).

#### Cohen-Sutherland Clipping (Recortar Linhas)

Antes de desenhar uma linha na tela, verifica se ela **sai dos limites**:

- Se a linha está 100% dentro da tela: desenha tudo
- Se está 100% fora: não desenha nada
- Se atravessa a borda: calcula matematicamente o ponto de interseção e desenha apenas a parte visível

**Por que fazer clipping?** Para economizar processamento e evitar desenhar pixels fora da tela!

---

## 5. Controle Interativo - O Loop Principal

### 5.1 A Estrutura do Loop Principal (main.py)

O programa é baseado em um **loop infinito** que se repete 60 vezes por segundo:

```python
while rodando:
    # 1. Processar entrada
    # 2. Atualizar estado
    # 3. Renderizar
    # 4. Mostrar na tela
    pygame.display.flip()
    clock.tick(60)  # 60 FPS
```

Essa é a estrutura padrão de **qualquer jogo ou aplicação gráfica interativa**.

### 5.2 Variáveis de Estado

Cada personagem tem um **conjunto de variáveis que definem seu estado**:

```python
# Billy
billy_x, billy_y = 270, 330       # Posição no mundo
billy_escala = 1.0                # Tamanho (1.0 = tamanho normal)
billy_angulo = 0                  # Ângulo de rotação em graus

# Clara
clara_x, clara_y = 100, 590
clara_escala = 0.9                # 90% do tamanho normal
clara_angulo = 0

# Menino
menino_x, menino_y = 200, 590
menino_escala = 1.0
menino_angulo = 0
```

**Por que armazenar assim?**
- Cada frame, essas variáveis podem ser modificadas pela entrada
- Elas servem como "memória" do estado do personagem
- A cada frame, calculamos novas coordenadas com base nelas

### 5.3 Processando a Entrada do Teclado

No início de cada frame, verificamos qual tecla o jogador pressionou:

```python
teclas = pygame.key.get_pressed()

# Movimentação Clara (Setas)
if teclas[pygame.K_LEFT]:   clara_x -= 15   # Move 15 pixels para esquerda
if teclas[pygame.K_RIGHT]:  clara_x += 15   # Move 15 pixels para direita
if teclas[pygame.K_UP]:     clara_y -= 15   # Move 15 pixels para cima
if teclas[pygame.K_DOWN]:   clara_y += 15   # Move 15 pixels para baixo

# Movimentação Billy (WASD)
if teclas[pygame.K_a]:  billy_x -= 15
if teclas[pygame.K_d]:  billy_x += 15
if teclas[pygame.K_w]:  billy_y -= 15
if teclas[pygame.K_s]:  billy_y += 15

# Rotação Billy (R)
if teclas[pygame.K_r]:  billy_angulo += 5
```

**A Lógica:**
- Quando a seta esquerda é pressionada, subtraímos 15 de `clara_x`
- No próximo frame, Clara estará 15 pixels mais à esquerda
- A cada frame, isso se repete, criando movimento suave

### 5.4 Calculando as Transformações

A cada frame, **recalculamos as matrizes** com os novos valores de entrada:

```python
m = calcularMatriz(billy_escala, billy_angulo, billy_x, billy_y)
n = calcularMatriz(clara_escala, clara_angulo, clara_x, clara_y)
t = calcularMatriz(menino_escala, menino_angulo, menino_x, menino_y)
```

Isso garante que:
- A matriz reflete a posição atual (após entrada do teclado)
- Quando renderizamos, o personagem aparece na posição correta

**Exemplo do que acontece:**
1. Jogador pressiona "A" → `billy_x -= 15`
2. `m = calcularMatriz(1.0, 0, 255, 330)` (nova posição)
3. Ao renderizar, Billy aparece 15 pixels mais à esquerda

### 5.5 Renderizando Tudo

```python
# Limpa a tela
definirAreaDeRecorte(0, 0, 1280, 720)
tela.fill((146, 255, 222))  # Céu azul
tela.fill((100, 100, 100), (0, 300, largura, 450))  # Chão cinza

# Desenha cenário (objetos estáticos)
desenhar_cenario(tela)

# Desenha os personagens com suas transformações atuais
renderizarPersonagem(tela, getBilly(), m)
renderizarPersonagem(tela, getMulher(), n)
renderizarPersonagem(tela, getMenino(), t)
```

A sequência é importante:
1. Limpa a tela (senão acumula imagens)
2. Desenha fundo (céu + chão)
3. Desenha cenário (atrás dos personagens)
4. Desenha personagens (na frente)

---

## 6. A Viewport - Mostrando o Mundo Inteiro no Canto

### 6.1 O Conceito de Viewport

Uma **viewport é uma "janela"** que mostra uma parte do mundo com **escala reduzida**. Como em um jogo com mapa-mundi:
- O mundo tem 1280×720 pixels
- A viewport no canto superior direito tem apenas 300×170 pixels
- Tudo que acontece no mundo é mostrado proporcionalizado nessa pequena janela

### 6.2 Calculando a Matriz da Viewport

```python
matriz_vp = calcularMatrizViewport(960, 20, 1260, 190, 1280, 720)
```

**Parâmetros:**
- `960, 20`: Canto superior esquerdo da viewport na tela
- `1260, 190`: Canto inferior direito da viewport na tela
- `1280, 720`: Tamanho do mundo em coordenadas

**O que essa função faz:**
1. Calcula a proporção de redução:
   - Largura viewport: 300 pixels (1260 - 960)
   - Largura mundo: 1280 pixels
   - Escala: 300 / 1280 ≈ 0.234 (reduz para ~23%)
2. Cria uma matriz que **escala e translada** tudo para caber na viewport

### 6.3 Renderizando a Viewport

```python
personagens_atuais = [
    (getBilly(), m),
    (getMulher(), n),
    (getMenino(), t),
]

renderizarViewport(tela, matriz_vp, personagens_atuais)
```

A função `renderizarViewport()`:
1. Desenha um **frame preto** ao redor (borda)
2. Desenha um **fundo escuro** dentro
3. **Define área de clipping** para não desenhar fora do frame
4. Desenha o cenário reduzido (aplicando matriz da viewport)
5. Desenha cada personagem reduzido (aplicando matriz da viewport)
6. **Restaura área de clipping** para a tela inteira

**Por que importante?**
- O jogador vê os 3 personagens se movimentando no mundo principal
- A viewport oferece uma **vista aérea** para orientação
- Usa o mesmo sistema de matrizes e renderização, apenas com escala diferente

---

## 7. Fluxo Completo de Um Frame

```
┌──────────────────────────────────────────────────────────────┐
│ 1. CAPTURA DE ENTRADA                                        │
│    - Verifica teclas pressionadas                            │
│    - Atualiza billy_x, clara_y, billy_angulo, etc           │
└──────────────────────────────────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────────┐
│ 2. CÁLCULO DE MATRIZES                                       │
│    - m = calcularMatriz(escala, angulo, x, y) para Billy    │
│    - n = calcularMatriz(...) para Clara                      │
│    - t = calcularMatriz(...) para Menino                     │
│    Cada matriz: Escala → Rotação → Translação               │
└──────────────────────────────────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────────┐
│ 3. LIMPEZA DA TELA                                           │
│    - tela.fill(azul) → Céu                                  │
│    - tela.fill(cinza) → Chão                                │
│    Define área de clipping para tela inteira                │
└──────────────────────────────────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────────┐
│ 4. RENDERIZAÇÃO DO CENÁRIO                                  │
│    - desenhar_cenario() desenha todos os objetos estáticos  │
│    - Árvores, carros, bancos, etc (sem transformação)       │
└──────────────────────────────────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────────┐
│ 5. RENDERIZAÇÃO DOS PERSONAGENS                             │
│    renderizarPersonagem(tela, getBilly(), m)                │
│    renderizarPersonagem(tela, getMulher(), n)               │
│    renderizarPersonagem(tela, getMenino(), t)               │
│                                                              │
│    Cada renderização:                                       │
│    - Para cada parte do personagem:                         │
│      * Aplica matriz de transformação                       │
│      * Preenche interior com scanline                       │
│      * Desenha contorno com Bresenham + Cohen-Sutherland   │
└──────────────────────────────────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────────┐
│ 6. RENDERIZAÇÃO DA VIEWPORT                                 │
│    - Desenha frame + fundo da viewport                      │
│    - Define clipping para apenas a viewport                 │
│    - Renderiza cenário reduzido (com matriz_vp)            │
│    - Renderiza personagens reduzidos (matriz_vp × matriz)  │
│    - Restaura clipping para tela inteira                    │
└──────────────────────────────────────────────────────────────┘
                        ↓
┌──────────────────────────────────────────────────────────────┐
│ 7. ATUALIZAÇÃO DO DISPLAY                                   │
│    - pygame.display.flip() → Mostra tudo na tela           │
│    - clock.tick(60) → Aguarda até 60 FPS                   │
└──────────────────────────────────────────────────────────────┘
                        ↓
              (Loop retorna ao passo 1)
```

---

## 8. Por Que Essa Arquitetura?

### Separação de Responsabilidades

| Arquivo | Responsabilidade |
|---------|------------------|
| `personagens.py` | Define **visualmente** como cada personagem é (getBilly, getMulher, etc) |
| `biblioteca.py` | Fornece **ferramentas gráficas** (primitivas, algoritmos) |
| `matrizes.py` | Lida com **transformações matemáticas** |
| `cenarios.py` | Define **objetos estáticos** do mundo |
| `main.py` | **Orquestra tudo** - loop, entrada, renderização |

### Vantagens dessa Estrutura

1. **Reutilização**: Funções gráficas podem ser usadas em qualquer personagem
2. **Manutenção**: Mudar visual de Billy não afeta renderização
3. **Escalabilidade**: Adicionar novo personagem é só escrever uma função nova
4. **Testabilidade**: Cada módulo pode ser testado independentemente
5. **Clareza**: Código é organizado por conceito, fácil de entender

---

## 9. Conceitos de Computação Gráfica Implementados

### Rasterização
Conversão de formas matemáticas (pontos, linhas) para pixels na tela:
- **Bresenham**: Escolhe melhor pixel para desenhar linha
- **Scanline**: Preenche polígonos eficientemente

### Transformações Afins
Modificações geométricas usando matrizes:
- **Escala**: Multiplica coordenadas por fator
- **Rotação**: Usa seno e cosseno
- **Translação**: Soma valores aos pontos

Todas podem ser compostas em **uma única matriz**.

### Clipping (Recorte)
Otimização que evita desenhar pixels fora da tela:
- **Cohen-Sutherland**: Algoritmo inteligente que calcula interseções
- Economiza processamento

### Transformação de Espaços
Conversão entre diferentes sistemas de coordenadas:
- **Espaço local**: Coordenadas do personagem (relativas à cabeça)
- **Espaço do mundo**: Coordenadas globais da tela
- **Espaço da viewport**: Coordenadas reduzidas do mini-mapa

---

## 10. Fluxo de Dados de Um Personagem

```
getBilly()
    ↓ Retorna lista de partes
[{"nome": "cabeca", "pontos": [...], "cor": (...), ...}, ...]
    ↓ Passa para renderizarPersonagem
renderizarPersonagem(tela, modelo, m)
    ↓ Para cada parte:
    ├─ Aplica matriz: aplicaTransformacao(m, pontos)
    ├─ Preenche: scanlineFill(tela, pts_trans, cor)
    └─ Contorna: setRetaRecortada(tela, p1, p2, cor) 60 vezes por segundo
    
Na viewport:
renderizarViewport(tela, matriz_vp, personagens)
    ↓ Para cada personagem:
    ├─ Compõe matrizes: m_final = matriz_vp × m
    └─ Renderiza: renderizarPersonagem(tela, modelo, m_final)
```

---

## 11. Conclusão

Este projeto demonstra que **computação gráfica é sobre:**
1. **Decomposição**: Dividir formas complexas em simples
2. **Transformação**: Usar matemática para manipular coordenadas
3. **Rasterização**: Converter matemática em pixels
4. **Otimização**: Evitar trabalho desnecessário (clipping)

E tudo isso funciona **em tempo real** a 60 FPS, permitindo **interação instantânea** com o que vemos na tela!

