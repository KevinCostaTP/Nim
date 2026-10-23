import tkinter as tk
import random
from nim import Nim, NimAI, train


class NimGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nim - Humano vs IA")

        self.status_label = tk.Label(root, text="A treinar a IA, aguarde...", font=("Arial", 14))
        self.status_label.pack(pady=10)

        # Contentor horizontal: tabuleiro à esquerda, histórico à direita
        self.content_frame = tk.Frame(root)
        self.content_frame.pack(pady=10)

        self.board_frame = tk.Frame(self.content_frame)
        self.board_frame.pack(side="left", padx=10, anchor="n")

        self.history_frame = tk.Frame(self.content_frame)
        self.history_frame.pack(side="left", padx=10, anchor="n")

        history_label = tk.Label(self.history_frame, text="Histórico:", font=("Arial", 12, "bold"))
        history_label.pack(anchor="w")

        self.history_text = tk.Text(self.history_frame, width=30, height=15, state="disabled")
        self.history_text.pack()

        self.play_again_button = None
        self.ai = None
        self.game = None
        self.human_player = None
        self.squares = []

        self.root.after(100, self.start_training)

    def start_training(self):
        """Treina a IA uma vez e começa o primeiro jogo."""
        self.ai = train(10000)
        self.new_game()

    def new_game(self):
        """Cria um novo jogo, escolhe quem começa aleatoriamente e desenha o tabuleiro."""
        self.human_player = random.randint(0, 1)
        self.game = Nim()
        self.clear_history()
        self.draw_board()
        self.update_status()

        if self.game.player != self.human_player:
            self.root.after(1000, self.ai_move)

    def clear_history(self):
        """Limpa o histórico de jogadas (chamado ao iniciar um novo jogo)."""
        self.history_text.config(state="normal")
        self.history_text.delete("1.0", tk.END)
        self.history_text.config(state="disabled")

    def log_move(self, text):
        """Adiciona uma linha ao histórico de jogadas."""
        self.history_text.config(state="normal")
        self.history_text.insert(tk.END, text + "\n")
        self.history_text.see(tk.END)  # scroll automático para a última linha
        self.history_text.config(state="disabled")

    def draw_board(self):
        """Redesenha todas as pilhas como linhas de quadrados clicáveis."""
        for widget in self.board_frame.winfo_children():
            widget.destroy()

        self.squares = []
        for pile_index, pile in enumerate(self.game.piles):
            row_frame = tk.Frame(self.board_frame)
            row_frame.pack(anchor="w", pady=2)

            label = tk.Label(row_frame, text=f"Pilha {pile_index}: ", width=10, anchor="w")
            label.pack(side="left")

            row_squares = []
            for position in range(pile):
                btn = tk.Button(
                    row_frame,
                    text="\u25a0",
                    width=3,
                    command=lambda p=pile_index, pos=position: self.human_click(p, pos)
                )
                btn.pack(side="left", padx=1)
                row_squares.append(btn)
            self.squares.append(row_squares)

    def human_click(self, pile_index, position):
        """Chamado quando o humano clica num quadrado. Remove esse quadrado e todos os seguintes na mesma pilha."""
        if self.game.winner is not None:
            return
        if self.game.player != self.human_player:
            return  # não é a vez do humano, ignora o clique

        count = self.game.piles[pile_index] - position
        self.game.move((pile_index, count))
        self.log_move(f"Tu: tiraste {count} da pilha {pile_index}")
        self.draw_board()
        self.update_status()

        if self.game.winner is not None:
            self.end_game()
        else:
            self.root.after(1000, self.ai_move)

    def ai_move(self):
        """A IA escolhe e faz a sua jogada (sem aleatoriedade, sempre a melhor ação conhecida)."""
        if self.game.winner is not None:
            return

        pile, count = self.ai.choose_action(self.game.piles, epsilon=False)
        self.game.move((pile, count))
        self.log_move(f"IA: tirou {count} da pilha {pile}")
        self.draw_board()
        self.status_label.config(text=f"A IA tirou {count} da pilha {pile}.")

        if self.game.winner is not None:
            self.end_game()
        else:
            self.update_status()

    def update_status(self):
        if self.game.player == self.human_player:
            self.status_label.config(text="A tua vez.")
        else:
            self.status_label.config(text="Vez da IA...")

    def end_game(self):
        """Desativa o tabuleiro e mostra o resultado, com um botão para jogar novamente."""
        for row in self.squares:
            for btn in row:
                btn.config(state="disabled")

        winner_text = "Ganhaste!" if self.game.winner == self.human_player else "A IA ganhou!"
        self.status_label.config(text=winner_text)

        if self.play_again_button is None:
            self.play_again_button = tk.Button(
                self.root, text="Jogar Novamente", command=self.reset_game
            )
            self.play_again_button.pack(pady=10)

    def reset_game(self):
        """Começa um novo jogo sem retreinar a IA."""
        self.new_game()


if __name__ == "__main__":
    root = tk.Tk()
    app = NimGUI(root)
    root.mainloop()
