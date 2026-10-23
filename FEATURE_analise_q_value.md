# Feature: Análise do Q-value da IA

**Branch:** `feature/analise-ia`
**Ficheiro:** `nim_gui.py` (extensão da GUI)
**Nível:** Simples

## Descrição

Mostra, logo abaixo do histórico de jogadas, qual a ação que a IA escolheu
na sua última jogada e o Q-value associado a essa ação — tornando visível
o raciocínio interno do Q-learning, que de outra forma fica "escondido"
dentro de `choose_action`.

## Como funciona

Dentro de `ai_move`, antes de `game.move(...)` alterar o estado do
tabuleiro, o estado atual é copiado (`state_before = self.game.piles.copy()`).
A cópia é necessária porque `game.move(...)` modifica a lista `self.piles`
diretamente — sem copiar, `state_before` deixaria de representar o estado
anterior à jogada assim que `move()` fosse chamado.

A partir desse estado guardado:
- `self.ai.choose_action(state_before, epsilon=False)` devolve a ação
  escolhida (`pile`, `count`).
- `self.ai.get_q_value(state_before, (pile, count))` devolve o Q-value
  dessa ação específica.

Ambas as funções já estavam implementadas em `nim.py` como parte do
trabalho base — esta feature não introduz lógica de aprendizagem nova,
apenas lê e apresenta informação já existente em `self.ai.q`.

O valor é mostrado formatado a duas casas decimais (`f"{value:.2f}"`) num
`tk.Label` fixo, atualizado a cada jogada da IA.

## Ferramenta de IA usada

Desenvolvida com apoio do Claude (Anthropic). Foi inicialmente proposta
como mostrar *todas* as ações consideradas pela IA, mas simplificada, a
pedido explícito, para mostrar apenas a ação escolhida e o seu valor —
reduzindo a implementação a uma leitura direta via `get_q_value`, sem
necessidade de percorrer todas as ações disponíveis.

## Como testar

Jogar uma partida em `nim_gui.py` e confirmar que, após cada jogada da
IA, a secção "Análise da IA:" mostra a pilha, a quantidade retirada e um
valor numérico correspondente.
