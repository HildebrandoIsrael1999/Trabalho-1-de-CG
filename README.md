# Documentação do Projeto "Billy da Tapioca"

## Visão Geral

Este projeto é um jogo arcade 2D feito para demonstrar algoritmos de computação gráfica clássicos, como rasterização, preenchimento, transformações geométricas, clipping e renderização manual usando matrizes. O motor gráfico foi construído do zero, sem bibliotecas gráficas de alto nível.

---

## Arquitetura dos Arquivos

- **main.py**  
	Ponto de entrada do jogo. Inicializa o Pygame, gerencia o loop principal, música, menu e chama funções de atualização e renderização do estado do jogo.

- **interface.py**  
	Implementa o menu principal, botões e lógica de interação do usuário com a interface gráfica.

- **config.py**  
	Gerencia o estado do jogo, incluindo posições dos personagens, itens, lógica de eventos (teclado), atualização de variáveis e controle de fluxo do gameplay.

- **personagens.py**  
	Define os modelos dos personagens (Billy, Clara, Menino) como listas de primitivas geométricas (retângulos, linhas, círculos).

- **cenarios.py**  
	Define os objetos do cenário (moita, carrinho, banco, cachorro, etc.) usando funções de primitivas geométricas.

- **biblioteca.py**  
	Biblioteca gráfica principal. Implementa algoritmos de rasterização (Bresenham, Scanline), preenchimento, clipping (Cohen-Sutherland), funções para desenhar e transformar primitivas.

- **matrizes.py**  
	Implementa operações de matrizes 3x3 para transformações afins: identidade, translação, escala, rotação, multiplicação e aplicação de matriz em pontos.

- **colisao.py**  
	Gerencia colisão entre personagens e obstáculos usando bounding boxes (AABB).

- **textos.py**  
	Renderiza textos e balões de fala na tela usando fontes do Pygame.

- **clipping.py**  
	Implementa o algoritmo de Cohen-Sutherland para recorte de linhas.

---

## Fluxo Principal do Jogo

1. **Inicialização**  
	 - Carrega recursos, configura tela e música.
	 - Exibe menu principal ([interface.py](interface.py)).

2. **Loop do Jogo**  
	 - Captura eventos do usuário (teclado, mouse).
	 - Atualiza o estado do jogo ([config.py](config.py)).
	 - Renderiza cenário, personagens e itens ([biblioteca.py](biblioteca.py), [cenarios.py](cenarios.py), [personagens.py](personagens.py)).
	 - Aplica transformações geométricas via matrizes ([matrizes.py](matrizes.py)).
	 - Gerencia colisões ([colisao.py](colisao.py)).
	 - Exibe textos e balões ([textos.py](textos.py)).
	 - Atualiza a tela a 60 FPS.

---

## Principais Funções do Projeto

### 1. `criar_estado_inicial(largura, altura)`
**Descrição:**  
Inicializa o estado do jogo, criando um dicionário com todas as variáveis necessárias para controlar o gameplay, como posição dos personagens, tempo, itens coletados, status de vitória, etc.

**Exemplo de uso:**  
```python
estado_jogo = criar_estado_inicial(1280, 720)
```
**Principais variáveis criadas:**  
- Posições dos personagens
- Lista de itens no cenário
- Tempo inicial do jogo
- Flags de vitória/derrota

---

### 2. `processar_eventos_jogo(estado_jogo, eventos)`
**Descrição:**  
Processa os eventos capturados pelo Pygame (teclado, mouse) e atualiza o estado do jogo conforme as ações do jogador.  
Exemplo: movimentação do personagem, interação com objetos, pausar o jogo.

**Exemplo de uso:**  
```python
eventos = pygame.event.get()
processar_eventos_jogo(estado_jogo, eventos)
```
**Principais ações:**  
- Movimentação (setas/WASD)
- Interação com itens
- Fechar o jogo

---

### 3. `atualizar_estado_jogo(estado_jogo)`
**Descrição:**  
Atualiza as variáveis do estado do jogo a cada frame. Calcula novas posições, verifica colisões, atualiza animações, checa condições de vitória/derrota e controla o tempo de jogo.

**Exemplo de uso:**  
```python
atualizar_estado_jogo(estado_jogo)
```
**Principais tarefas:**  
- Atualizar posições dos personagens
- Verificar colisão com obstáculos e itens
- Atualizar tempo e status do jogo

---

### 4. `desenhar_jogo(tela, estado_jogo)`
**Descrição:**  
Renderiza todos os elementos do jogo na tela: cenário, personagens, itens, textos e balões de fala. Utiliza as funções de desenho da biblioteca gráfica para rasterizar cada objeto conforme seu modelo e matriz de transformação.

**Exemplo de uso:**  
```python
desenhar_jogo(tela, estado_jogo)
```
**Principais elementos desenhados:**  
- Cenário (moita, banco, carrinho, etc.)
- Personagens (Billy, Clara, Menino)
- Itens (tapioca, queijo, caixa)
- Textos e balões de fala

---

### 5. `renderizarPersonagem(modelo, matriz, tela)`
**Descrição:**  
Recebe o modelo do personagem (lista de primitivas geométricas), aplica a matriz de transformação (escala, rotação, translação) e desenha cada parte na tela usando algoritmos de rasterização.

**Exemplo de uso:**  
```python
renderizarPersonagem(modelo_billy, matriz_billy, tela)
```
**Principais etapas:**  
- Aplica matriz de transformação em cada ponto do modelo
- Chama funções de desenho para cada primitiva (retângulo, círculo, linha)

---

### 6. `scanlineFill(poligono, cor, tela)`
**Descrição:**  
Preenche um polígono na tela usando o algoritmo de scanline, que percorre linhas horizontais e determina os segmentos internos do polígono para colorir.

**Exemplo de uso:**  
```python
scanlineFill(poligono, (255,255,255), tela)
```
**Principais etapas:**  
- Calcula interseções das scanlines com as arestas do polígono
- Preenche os segmentos internos com a cor desejada

---

### 7. `setRetaBresenham(x1, y1, x2, y2, cor, tela)`
**Descrição:**  
Desenha uma linha entre dois pontos usando o algoritmo de Bresenham, eficiente para rasterização de linhas em grids de pixels.

**Exemplo de uso:**  
```python
setRetaBresenham(10, 20, 100, 200, (0,0,0), tela)
```
**Principais etapas:**  
- Calcula os pixels que formam a linha entre os pontos
- Colore cada pixel na tela

---

### 8. `cohenSutherlandClip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)`
**Descrição:**  
Recorta uma linha para garantir que ela seja desenhada apenas dentro dos limites da tela (viewport), usando o algoritmo de Cohen-Sutherland.

**Exemplo de uso:**  
```python
nova_linha = cohenSutherlandClip(x1, y1, x2, y2, 0, 0, largura, altura)
```
**Principais etapas:**  
- Verifica se a linha está dentro, fora ou parcialmente dentro da área visível
- Retorna os pontos ajustados para desenhar apenas a parte visível

---

### 9. `calcularMatriz(escala, rotacao, translacao)`
**Descrição:**  
Gera uma matriz de transformação 3x3 combinando escala, rotação e translação, usada para transformar modelos geométricos antes de desenhar.

**Exemplo de uso:**  
```python
matriz = calcularMatriz((1.0, 1.0), 45, (100, 200))
```
**Principais etapas:**  
- Cria matriz de escala
- Cria matriz de rotação
- Cria matriz de translação
- Multiplica as matrizes para obter a transformação final

---

### 10. Funções de Modelos (`getBilly`, `getMulher`, `getMenino`, `getMoita`, etc.)
**Descrição:**  
Cada função retorna uma lista de primitivas geométricas que compõem o personagem ou objeto do cenário. Cada primitiva tem cor, posição, tamanho e nome.

**Exemplo de uso:**  
```python
modelo_billy = getBilly()
modelo_moita = getMoita()
```
**Principais etapas:**  
- Define cada parte do objeto como retângulo, círculo, linha, etc.
- Retorna lista para ser usada na renderização

---

## Conceitos Implementados

- **Rasterização manual** (linhas, polígonos, círculos)
- **Preenchimento** (scanline, flood fill)
- **Transformações geométricas** (matrizes 3x3)
- **Clipping** (Cohen-Sutherland)
- **Colisão** (AABB)
- **Renderização de viewport** (mini-mapa)
- **Interface gráfica** (menu, botões)
- **Textos e balões de fala**

---

## Recomendações

Para entender detalhes de cada algoritmo e função, consulte [DOCUMENTACAO.md](DOCUMENTACAO.md), que traz exemplos, fluxos e explicações didáticas sobre cada parte do sistema.

---

## Demonstração em Vídeo

Assista à execução completa do projeto, incluindo tela de abertura e gameplay:

[👉 Assistir vídeo no YouTube](https://www.youtube.com/seu-link-aqui)

---

## Equipe

**Hildebrando Israel ** - email1@exemplo.com
**Samuel ** - email2@exemplo.com
**Clara ** - email3@exemplo.com

