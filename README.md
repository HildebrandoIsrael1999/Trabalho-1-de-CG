# "Billy da Tapioca"

## Visão Geral


Este projeto é um jogo arcade 2D desenvolvido como parte de uma avaliação acadêmica de Computação Gráfica. O objetivo principal é demonstrar, de forma prática e visual, a implementação de algoritmos clássicos da área, como rasterização de linhas e polígonos, preenchimento, transformações geométricas, clipping e renderização manual utilizando matrizes de pixels. Todo o motor gráfico foi construído do zero, sem o uso de bibliotecas gráficas de alto nível, o que evidencia o domínio dos conceitos fundamentais de gráficos computacionais.

---

## Arquitetura dos Arquivos


- **main.py**  
	Ponto de entrada do jogo, responsável por inicializar o Pygame e todos os módulos do sistema. Gerencia o loop principal, controle de FPS, música de fundo e transições entre telas. Realiza a chamada das funções de atualização do estado do jogo e renderização dos elementos gráficos. Controla o fluxo entre menu, gameplay e tela de ranking. Também faz o tratamento de encerramento do jogo e recursos.

- **interface.py**  
	Implementa o menu principal, botões, telas de instrução e ranking. Gerencia a navegação entre diferentes telas do jogo, detectando cliques e interações do usuário. Responsável pelo layout visual dos menus, animações de entrada e saída, e feedback visual dos botões. Realiza a integração com o sistema de ranking e exibe informações do jogador. Permite customização de opções e configurações básicas.

- **config.py**  
	Gerencia o estado global do jogo, incluindo posições dos personagens, itens, obstáculos e variáveis de controle. Processa eventos do teclado e mouse, atualizando o estado conforme as ações do jogador. Controla o fluxo do gameplay, como início, pausa, vitória e derrota. Realiza a lógica de atualização de variáveis, como tempo, pontuação e itens coletados. Centraliza a comunicação entre os módulos e mantém o estado sincronizado.

**personagens.py**  
	Responsável apenas por definir os pontos dos personagens (Billy, Clara, Menino) através das funções get. Não realiza renderização direta, apenas retorna listas de pontos para serem usados na função renderizarPersonagem da biblioteca. Permite fácil alteração de aparência e adição de novos personagens. Organiza os dados para renderização eficiente e serve de base para colisão.

**cenarios.py**  
	Define os pontos dos objetos do cenário (moita, carrinho, banco, cachorro, etc.) usando funções get. Não realiza renderização direta, apenas retorna listas de pontos para facilitar a organização e uso na renderização. Permite composição de cenários variados e dinâmicos, além de servir de referência para colisão.

**biblioteca.py**  
	Biblioteca gráfica principal do projeto, implementando algoritmos de rasterização de linhas (Bresenham), polígonos (Scanline), círculos e preenchimento. Contém funções para desenhar e transformar primitivas geométricas, além de aplicar clipping (Cohen-Sutherland) em linhas. Gerencia a renderização manual dos elementos na matriz de pixels, incluindo a função renderizarPersonagem que utiliza os dados de personagens.py e a renderização do cenário a partir dos pontos definidos em cenarios.py. Implementa também a renderização da viewport (mini-mapa) e centraliza utilitários gráficos para uso em todo o sistema.

- **matrizes.py**  
	Implementa operações de matrizes 3x3 para transformações afins: identidade, translação, escala, rotação, multiplicação e aplicação de matriz em pontos. Permite compor múltiplas transformações em uma única matriz. Facilita a manipulação geométrica de personagens e objetos do cenário. Garante precisão e eficiência nas operações gráficas. Serve de base para animações e movimentações complexas.

**colisao.py**  
	Gerencia colisão entre personagens, itens e obstáculos usando bounding boxes (AABB). Implementa funções para detectar sobreposição e calcular respostas de colisão. Permite bloquear movimentos, coletar itens e interagir com o ambiente. Otimiza o desempenho do jogo evitando cálculos desnecessários. Centraliza toda a lógica de colisão do sistema.

- **textos.py**  
	Renderiza textos, balões de fala e informações na tela usando fontes do Pygame. Permite exibir diálogos, instruções, pontuação e mensagens do sistema. Gerencia estilos, cores e posicionamento dos textos. Facilita a comunicação visual com o jogador. Suporta animações e efeitos visuais em textos.

**clipping.py**  
	Implementa o algoritmo de Cohen-Sutherland para recorte de linhas (linhaRecortada), garantindo que apenas segmentos visíveis sejam desenhados na tela. Permite otimizar a renderização e evitar artefatos fora da área útil. Facilita a implementação da viewport (mini-mapa). Centraliza utilitários de recorte geométrico para todo o sistema.

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
Recebe o modelo do personagem (lista de primitivas geométricas), aplica a matriz de transformação (escala, rotação, translação) e desenha cada parte na tela usando algoritmos de rasterização. Para polígonos, utiliza o algoritmo ScanlineFill para realizar o preenchimento das formas, garantindo renderização eficiente e visualmente correta.

**Exemplo de uso:**  
```python
renderizarPersonagem(modelo_billy, matriz_billy, tela)
```
**Principais etapas:**  
- Aplica matriz de transformação em cada ponto do modelo
- Chama funções de desenho para cada primitiva (retângulo, círculo, linha)
- Utiliza ScanlineFill para preencher polígonos do personagem

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
Recorta uma linha para garantir que ela seja desenhada apenas dentro dos limites da tela (viewport), usando o algoritmo de Cohen-Sutherland. No projeto, essa função é utilizada dentro de setLinhaRecortada, que recebe os valores da linha e da área de recorte, aplica o algoritmo e, se a linha estiver visível, chama setLinhaBresenham para desenhar o segmento recortado.

**Exemplo de uso:**  
```python
setLinhaRecortada(x1, y1, x2, y2, 0, 0, largura, altura, tela)
```
**Principais etapas:**  
- Verifica se a linha está dentro, fora ou parcialmente dentro da área visível
- Retorna os pontos ajustados para desenhar apenas a parte visível
- Chama setLinhaBresenham para desenhar o segmento recortado

---

### 9. `calcularMatriz(escala, rotacao, translacao)`
**Descrição:**  
Gera uma matriz de transformação 3x3 combinando escala, rotação e translação, usada para transformar modelos geométricos antes de desenhar. No projeto, o correto é primeiro transladar o objeto para a origem (0,0), aplicar a escala e rotação, e só então realizar a translação final para posicionar o objeto no local desejado da tela. Esse contexto garante que as transformações ocorram de forma previsível e correta para todos os elementos.

**Exemplo de uso:**  
```python
matriz = calcularMatriz((1.0, 1.0), 45, (100, 200))
```
**Principais etapas:**  
- Cria matriz de translação para levar o objeto à origem
- Cria matriz de escala
- Cria matriz de rotação
- Cria matriz de translação final para posicionar o objeto
- Multiplica as matrizes na ordem correta para obter a transformação final

---

### 10. Funções de Modelos (`getBilly`, `getMulher`, `getMenino`, `getMoita`, etc.)
**Descrição:**  
Cada função retorna uma lista de pontos compõem o personagem ou objeto do cenário. Cada primitiva tem cor, posição, tamanho e nome.

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

## Como executar o projeto

1. **Pré-requisitos:**
   - Python 3.8 ou superior instalado.
   - Recomenda-se o uso de ambiente virtual (venv).
   - Instale as dependências necessárias:
     ```bash
     pip install pygame
     ```

2. **Baixe/clique no repositório** e certifique-se de que todos os arquivos e pastas (incluindo a pasta `Músicas/` e `Fontes/`) estejam no mesmo diretório.

3. **Execute o jogo:**
   - No terminal, navegue até a pasta do projeto e rode:
     ```bash
     python main.py
     ```

4. **Controles:**
   - Use as setas do teclado para movimentar o personagem.
   - Siga as instruções exibidas na tela para interagir com menus e objetos.

5. **Observações:**
   - O jogo foi desenvolvido para rodar em Windows, mas pode funcionar em outros sistemas com Python e Pygame instalados.
   - Certifique-se de que os arquivos de música estejam no caminho correto para evitar erros de áudio.

---

## Demonstração em Vídeo

Assista à execução completa do projeto, incluindo tela de abertura e gameplay:

[👉 Assistir vídeo no YouTube](https://www.youtube.com/seu-link-aqui)

---

## Equipe

**Hildebrando Israel ** - email1@exemplo.com
**Samuel ** - email2@exemplo.com
**Clara ** - email3@exemplo.com

