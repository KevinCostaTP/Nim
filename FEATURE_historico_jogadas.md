# Feature: Histórico de Jogadas

**Branch:** `feature/historico-jogadas`
**Ficheiro:** `nim_gui.py` (extensão da GUI)
**Nível:** Regular

## Descrição

Adiciona um painel lateral à interface gráfica que regista, em tempo real,
todas as jogadas feitas ao longo da partida — tanto do jogador humano como
da IA — num formato de lista cronológica.

## Como funciona

Um widget `tk.Text` (`self.history_text`) é mantido como só-leitura
(`state="disabled"`), exceto no momento exato de lhe adicionar uma nova
linha, através da função auxiliar `log_move(texto)`. Esta função é chamada:

- Em `human_click`, logo após `game.move(...)`, registando quantos objetos
  o humano retirou e de que pilha.
- Em `ai_move`, no mesmo ponto, registando a jogada da IA.

O histórico é limpo automaticamente (`clear_history()`) sempre que um novo
jogo começa, incluindo ao clicar "Jogar Novamente".

Um detalhe técnico: o widget usa `.see(tk.END)` após cada inserção, para
que a vista role automaticamente até à linha mais recente, mesmo quando o
histórico cresce além do espaço visível.

## Ferramenta de IA usada

Desenvolvida com apoio do Claude (Anthropic), depois de uma explicação
pedida sobre como implementar a ideia sem alterar `nim.py`. O Claude
propôs a abordagem de um widget `tk.Text` com alternância entre estado
"normal" (para escrever) e "disabled" (para impedir edição pelo
utilizador), e integrou a função `log_move` nos dois pontos do código
onde uma jogada é concluída.

## Como testar

Jogar uma partida completa em `nim_gui.py` e confirmar que cada jogada
(humana e da IA) aparece corretamente listada no painel "Histórico:", e
que a lista é limpa ao recomeçar o jogo.
