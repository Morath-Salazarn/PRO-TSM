import random

class Minesweeper:
    def __init__(self, rows=9, cols=9, mines=10):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.visible = [[False for _ in range(cols)] for _ in range(rows)]
        self.mine_positions = set()
        self._place_mines()
        self._calculate_numbers()
        self.game_over = False

    def _place_mines(self):
        while len(self.mine_positions) < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            self.mine_positions.add((r, c))
        for r, c in self.mine_positions:
            self.board[r][c] = 'M'

    def _calculate_numbers(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == 'M':
                    continue
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            if self.board[nr][nc] == 'M':
                                count += 1
                self.board[r][c] = str(count) if count > 0 else ' '

    def reveal(self, r, c):
        if self.game_over or self.visible[r][c]:
            return
        self.visible[r][c] = True
        if self.board[r][c] == 'M':
            self.game_over = True
            print("Game Over! You hit a mine.")
            self._show_board(reveal_all=True)
            return
        if self.board[r][c] == ' ':
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        if not self.visible[nr][nc]:
                            self.reveal(nr, nc)

    def _show_board(self, reveal_all=False):
        print("   " + " ".join(str(c) for c in range(self.cols)))
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                if reveal_all or self.visible[r][c]:
                    row.append(self.board[r][c])
                else:
                    row.append('#')
            print(f"{r:2} " + " ".join(row))

    def check_win(self):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != 'M' and not self.visible[r][c]:
                    return False
        return True

def main():
    game = Minesweeper()
    while not game.game_over:
        game._show_board()
        try:
            move = input("Enter row and column (e.g. 3 4): ")
            r, c = map(int, move.strip().split())
            if 0 <= r < game.rows and 0 <= c < game.cols:
                game.reveal(r, c)
                if game.check_win():
                    print("Congratulations! You won!")
                    game._show_board(reveal_all=True)
                    break
            else:
                print("Invalid coordinates.")
        except Exception:
            print("Invalid input.")
            
if __name__ == "__main__":
    main()