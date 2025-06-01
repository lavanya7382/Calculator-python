
from tkinter import *
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("300x300")
        self.player_turn = "X"
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = Button(self.root, command=lambda row=i, column=j: self.click(row, column), height=3, width=6)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def click(self, row, column):
        if self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.check_win():
                messagebox.showinfo("Game Over", f"Player {self.player_turn} wins!")
                self.root.quit()
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.root.quit()
            self.player_turn = "O" if self.player_turn == "X" else "X"

    def check_win(self):
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button['text'] == "":
                    return False
        return True

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
