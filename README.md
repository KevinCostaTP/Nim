# Nim — Projeto de Inteligência Artificial

## Introdução

Este projeto implementa uma inteligência artificial capaz de jogar Nim
através de Q-learning, baseado no projeto "Nim" do curso CS50's
Introduction to Artificial Intelligence with Python, de Harvard
(https://cs50.ai/projects/4/nim/). A IA aprende a jogar unicamente através
da repetição — joga milhares de partidas contra si própria, ajustando
gradualmente as suas estimativas sobre quão boa é cada jogada possível em
cada situação do tabuleiro, sem qualquer conhecimento prévio das regras
estratégicas do jogo.

## Descrição do projeto

O jogo de Nim consiste em várias pilhas de objetos; cada jogador, na sua
vez, retira um ou mais objetos de uma única pilha; quem retirar o último
objeto vence.

### Componentes principais

- **`nim.py`** — lógica do jogo (`Nim`) e da IA (`NimAI`), incluindo as
  quatro funções de Q-learning implementadas como parte base do trabalho:
  `get_q_value`, `update_q_value`, `best_future_reward` e `choose_action`.
- **`play.py`** — versão original de terminal, fornecida pelo enunciado.
- **`nim_gui.py`** — interface gráfica desenvolvida como extra, descrita
  em detalhe nos ficheiros `FEATURE_*.md` correspondentes.

### Extras desenvolvidos

| Nível | Feature | Documentação |
|---|---|---|
| Complexa | Interface gráfica (clicar para jogar) | `FEATURE_gui_interface.md` |
| Regular | Histórico de jogadas | `FEATURE_historico_jogadas.md` |
| Simples | Análise do Q-value da IA | `FEATURE_analise_q_value.md` |

## Como correr

```bash
# Versão de terminal
python3 play.py

# Versão gráfica
python3 nim_gui.py
```

## Testes e estilo

`check50` e `style50` não funcionam nativamente no Windows (dependem do
módulo `termios`, exclusivo de Linux/macOS). É necessário correr através
do WSL (Windows Subsystem for Linux), com Ubuntu, e com Python 3.12
especificamente (versão testada pela equipa do CS50).

### Instalação (uma vez só)

Num PowerShell como Administrador:
```powershell
wsl --install -d Ubuntu
```
Reiniciar o PC se for pedido. Depois, abrir a aplicação "Ubuntu" e correr:
```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
sudo apt install pipx

sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv

pipx install check50 --python python3.12
pipx install submit50 --python python3.12
pipx install style50 --python python3.12
pipx ensurepath
```
Fechar e reabrir o terminal Ubuntu depois de instalar, para o PATH
atualizar.

### Correr os testes

Copiar o projeto para o sistema de ficheiros nativo do Linux (evita
problemas de permissões do mount do Windows):
```bash
mkdir -p ~/projects
cp -r "/mnt/c/Users/" ~/projects/nim
cd ~/projects/nim
```
Depois de qualquer alteração ao código (feita normalmente no lado
Windows), repetir o `cp -r` para atualizar esta cópia antes de testar.

```bash
check50 ai50/projects/2024/x/nim --local
style50 nim.py nim_gui.py
```

## Ferramentas de IA usadas

Todo o desenvolvimento deste projeto contou com apoio do **Claude**
(Anthropic), usado como assistente de programação e de aprendizagem ao
longo de todo o processo — desde a implementação das quatro funções base
de Q-learning até ao design e construção dos extras.

### Metodologia de trabalho com a IA

Para as quatro funções base, o processo seguido foi: pedir uma explicação
do conceito antes de qualquer código, tentar escrever a solução de forma
independente, e só depois pedir correção/validação. Para os extras
(interface gráfica), o processo foi inverso: planear em detalhe com a IA
antes de qualquer código ser escrito, aprovar o plano, e só depois gerar
a implementação.

### Exemplos de prompts e respetivos outputs

**Exemplo 1 — correção de um erro de lógica:**

> Código submetido (com bug):
> ```python
> best_reward = 0
> for action in Nim.available_actions(state):
>     best reward = max(best_reward, self.get_q_value(state, action))
>     return best reward
> ```
> Output do Claude: identificou dois problemas — `best reward` com espaço
> (inválido em Python; deveria ser `best_reward`) e o `return` colocado
> *dentro* do ciclo `for`, fazendo a função terminar após avaliar apenas
> a primeira ação, em vez de comparar todas.

**Exemplo 3 — planeamento antes da implementação da GUI:**

> Prompt: "I approve of that plan, before putting it to action write it
> in full please"
>
> Output do Claude: documento detalhado do plano da interface gráfica
> (estrutura de ficheiros, biblioteca escolhida — tkinter —, modelo de
> interação "clicar corta a fila", fluxo de turnos, e o que ficava
> propositadamente fora do âmbito), submetido para aprovação antes de
> qualquer linha de código ser escrita.

**Exemplo 4 — diagnóstico de um problema de ambiente (não relacionado
com o código do projeto):**

> O `check50` falhava com `TypeError: unsupported operand type(s) for /:
> 'NoneType' and 'str'` em todos os testes, mesmo após mudar o projeto
> para o sistema de ficheiros nativo do Linux (WSL). O Claude levantou a
> hipótese de incompatibilidade de versão do Python (3.14 vs. a versão
> testada pela equipa do CS50, 3.12), propôs instalar Python 3.12 via
> `deadsnakes` PPA e reinstalar as ferramentas CS50 com `pipx install
> check50 --python python3.12` — o que resolveu o problema.
