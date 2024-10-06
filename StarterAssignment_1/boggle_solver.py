'''
Name: Robel Bruk
SID: 003058826
'''


class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = set(dictionary)  # Convert dictionary to a set for fast lookup
        self.n = len(grid)  # Grid size (NxN)
        self.solution = set()  # To store found words, using a set to avoid duplicates
        self.visited = [[False for _ in range(self.n)] for _ in range(self.n)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # 8 possible directions

    def setGrid(self, grid):
        self.grid = grid
        self.n = len(grid)  # Reset grid size

    def setDictionary(self, dictionary):
        self.dictionary = set(dictionary)  # Reset dictionary as a set for quick lookup

    def is_valid(self, word):
        return len(word) >= 3 and word in self.dictionary

    def getSolution(self):
    # checks if grid is empty
      if self.n == 0 or len(self.grid[0]) == 0:
        return []  # returns an empty list if the grid is empty

      for i in range(self.n):
          for j in range(self.n):
              self.dfs(i, j, "")
              
      return sorted(list(self.solution))  # returns sorted list of found words

    def dfs(self, x, y, path):
        if not (0 <= x < self.n and 0 <= y < self.n) or self.visited[x][y]:
            return

        # Get the current letter (handling "Qu" and "St" tiles as special cases)
        current_char = self.grid[x][y]
        if current_char == "Qu":
            path += "Qu"
        elif current_char == "St":
            path += "St"
        else:
            path += current_char

        # Mark this tile as visited
        self.visited[x][y] = True

        # Check if this path forms a valid word
        if self.is_valid(path):
            self.solution.add(path)

        # Explore all 8 directions
        for dx, dy in self.directions:
            new_x, new_y = x + dx, y + dy
            self.dfs(new_x, new_y, path)

        # Backtrack: unmark this tile as visited
        self.visited[x][y] = False


def main():
    grid = [['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'], 
            ['I', 'J', 'K', 'L'], 
            ['A', 'B', 'C', 'D']]

    dictionary = ['ABEF', 'AFJIEB', 'DGKD', 'DGKA']

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()



