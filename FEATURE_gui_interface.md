# Feature: Interface Gráfica (GUI)

**Branch:** `feature/gui-interface`
**Ficheiro:** `nim_gui.py`
**Nível:** Complexa

## Descrição

Substitui a interação por terminal (`play()` em `nim.py`, com `input()` para
escolher pilha e quantidade) por uma interface gráfica construída com
`tkinter`, onde o jogador clica diretamente no tabuleiro para jogar.

## Como funciona

Cada pilha é desenhada como uma fila de quadrados clicáveis, um por objeto
restante. Clicar num quadrado remove esse quadrado e todos os seguintes na
mesma fila — por exemplo, numa pilha com 5 objetos, clicar no 3º quadrado
remove 3 objetos (o clicado e os dois seguintes). Esta é a forma clássica de
apresentar visualmente o jogo de Nim.

Fluxo de uma partida:
1. Ao iniciar o programa, a IA é treinada uma vez (`train(10000)`).
2. É escolhido aleatoriamente quem começa (humano ou IA), tal como no
   `play()` original.
3. No turno do humano, um clique num quadrado aplica a jogada.
4. No turno da IA, a jogada acontece automaticamente após 1 segundo
   (usando `root.after`, para não bloquear a interface, ao contrário de
   `time.sleep`), através de `ai.choose_action(state, epsilon=False)`.
5. No fim do jogo, o tabuleiro é desativado e aparece um botão "Jogar
   Novamente", que reinicia a partida sem retreinar a IA.

## Relação com `nim.py`

Este ficheiro **não altera** `nim.py` — apenas importa `Nim`, `NimAI` e
`train` e reutiliza-os tal como estão. Toda a lógica do jogo e da IA
(incluindo as quatro funções implementadas: `get_q_value`,
`update_q_value`, `best_future_reward`, `choose_action`) permanece
inalterada.

## Ferramenta de IA usada

Desenvolvida com apoio do Claude (Anthropic). O plano da interface
(estrutura de ficheiros, escolha do tkinter, modelo de interação
"clicar corta a fila", fluxo de turnos) foi primeiro discutido e aprovado
antes da escrita de qualquer código, seguindo o pedido: "antes de pôr em
ação, escreva o plano por completo". O código foi gerado a partir desse
plano aprovado.

## Como testar

```bash
python3 nim_gui.py
```


