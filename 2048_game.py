import tkinter as tk
import random

class Game2048:
    def __init__(self, master):
        self.master = master
        self.master.title("2048")
        self.master.geometry("350x400")
        self.master.bind("<Key>", self.handle_key)

        self.grid_size = 4
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.score = 0

        self.init_grid()
        self.add_tile()
        self.update_grid()
        self.update_score()

    def init_grid(self):
        self.tiles = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                tile = tk.Label(self.master, text="", font=("Helvetica", 32), width=4, height=2, relief="raised")
                tile.grid(row=i, column=j, padx=5, pady=5)
                row.append(tile)
            self.tiles.append(row)

        self.score_label = tk.Label(self.master, text="Score: 0", font=("Times New Roman", 20, "bold"), fg="lightblue")
        self.score_label.grid(row=self.grid_size, columnspan=self.grid_size, pady=10)

    def add_tile(self):
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def update_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.grid[i][j]
                if value == 0:
                    self.tiles[i][j].configure(text="", bg="lightgray")
                else:
                    self.tiles[i][j].configure(text=str(value), bg="lightblue")
        self.master.update_idletasks()

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")
        self.master.update_idletasks()

    def handle_key(self, event):
        if event.keysym in ['Up', 'Down', 'Left', 'Right']:
            self.move_tiles(event.keysym)
            self.add_tile()
            self.update_grid()
            self.update_score()
            if self.check_game_over():
                print("Game Over! Score:", self.score)

    def move_tiles(self, direction):
        moved = False
        if direction == 'Up':
            for j in range(self.grid_size):
                for i in range(1, self.grid_size):
                    if self.grid[i][j] != 0:
                        k = i
                        while k > 0 and (self.grid[k - 1][j] == 0 or self.grid[k - 1][j] == self.grid[i][j]):
                            if self.grid[k - 1][j] == self.grid[i][j]:
                                self.grid[k - 1][j] *= 2
                                self.grid[i][j] = 0
                                self.score += self.grid[k - 1][j]
                                moved = True
                                self.update_grid()  # Update grid after merge
                                self.update_score()  # Update score after merge
                                self.master.after(10)  # Add delay for transition
                                break
                            else:
                                self.grid[k - 1][j] = self.grid[i][j]
                                self.grid[i][j] = 0
                                k -= 1
                                moved = True
                                self.update_grid()  # Update grid after move
                                self.master.after(10)  # Add delay for transition
        elif direction == 'Down':
            for j in range(self.grid_size):
                for i in range(self.grid_size - 2, -1, -1):
                    if self.grid[i][j] != 0:
                        k = i
                        while k < self.grid_size - 1 and (self.grid[k + 1][j] == 0 or self.grid[k + 1][j] == self.grid[i][j]):
                            if self.grid[k + 1][j] == self.grid[i][j]:
                                self.grid[k + 1][j] *= 2
                                self.grid[i][j] = 0
                                self.score += self.grid[k + 1][j]
                                moved = True
                                self.update_grid()  # Update grid after merge
                                self.update_score()  # Update score after merge
                                self.master.after(10)  # Add delay for transition
                                break
                            else:
                                self.grid[k + 1][j] = self.grid[i][j]
                                self.grid[i][j] = 0
                                k += 1
                                moved = True
                                self.update_grid()  # Update grid after move
                                self.master.after(10)  # Add delay for transition
        elif direction == 'Left':
            for i in range(self.grid_size):
                for j in range(1, self.grid_size):
                    if self.grid[i][j] != 0:
                        k = j
                        while k > 0 and (self.grid[i][k - 1] == 0 or self.grid[i][k - 1] == self.grid[i][j]):
                            if self.grid[i][k - 1] == self.grid[i][j]:
                                self.grid[i][k - 1] *= 2
                                self.grid[i][j] = 0
                                self.score += self.grid[i][k - 1]
                                moved = True
                                self.update_grid()  # Update grid after merge
                                self.update_score()  # Update score after merge
                                self.master.after(10)  # Add delay for transition
                                break
                            else:
                                self.grid[i][k - 1] = self.grid[i][j]
                                self.grid[i][j] = 0
                                k -= 1
                                moved = True
                                self.update_grid()  # Update grid after move
                                self.master.after(10)  # Add delay for transition
        elif direction == 'Right':
            for i in range(self.grid_size):
                for j in range(self.grid_size - 2, -1, -1):
                    if self.grid[i][j] != 0:
                        k = j
                        while k < self.grid_size - 1 and (self.grid[i][k + 1] == 0 or self.grid[i][k + 1] == self.grid[i][j]):
                            if self.grid[i][k + 1] == self.grid[i][j]:
                                self.grid[i][k + 1] *= 2
                                self.grid[i][j] = 0
                                self.score += self.grid[i][k + 1]
                                moved = True
                                self.update_grid()  # Update grid after merge
                                self.update_score()  # Update score after merge
                                self.master.after(10)  # Add delay for transition
                                break
                            else:
                                self.grid[i][k + 1] = self.grid[i][j]
                                self.grid[i][j] = 0
                                k += 1
                                moved = True
                                self.update_grid()  # Update grid after move
                                self.master.after(10)  # Add delay for transition
        if moved:
            self.move_tiles(direction)


    def check_game_over(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == 0:
                    return False
                if j < self.grid_size - 1 and self.grid[i][j] == self.grid[i][j+1]:
                    return False
                if i < self.grid_size - 1 and self.grid[i][j] == self.grid[i+1][j]:
                    return False
        return True

def main():
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()

if __name__ == "__main__":
    main()
