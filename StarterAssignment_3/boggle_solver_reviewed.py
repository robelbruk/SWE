# Reviewed code

class Boggle:
    def __init__(self, grid, dictionary):
        """
        Initializes the Boggle game with a grid and dictionary.
        
        Args:
            grid (List[List[str]]): 2D grid of letters representing the Boggle board
            dictionary (List[str]): List of valid words to search for
        
        Note: The grid is assumed to be square (N x N)
        """
        self.grid = [[cell.upper() for cell in row] for row in grid]
        self.dictionary = set(word.upper() for word in dictionary)
        self.prefixes = self._get_prefixes(self.dictionary)
        self.grid_size = len(grid)
        self.found_words = set()
        
        # All possible movement directions in the grid
        self.directions = [
            (-1, 0),   # Up
            (1, 0),    # Down
            (0, -1),   # Left
            (0, 1),    # Right
            (-1, -1),  # Up-Left
            (-1, 1),   # Up-Right
            (1, -1),   # Down-Left
            (1, 1)     # Down-Right
        ]

    def _get_prefixes(self, dictionary):
        """
        Generate a set of all valid prefixes from the dictionary for prefix pruning.
        
        Args:
            dictionary (Set[str]): Set of valid words
            
        Returns:
            Set[str]: Set of all possible prefixes from the dictionary words
        """
        prefixes = set()
        for word in dictionary:
            for i in range(1, len(word)):
                prefixes.add(word[:i])
        return prefixes

    def _is_valid_prefix(self, path):
        """
        Checks if the current path is a valid prefix for any dictionary word.
        
        Args:
            path (str): Current sequence of letters being checked
            
        Returns:
            bool: True if the path is a valid prefix, False otherwise
        """
        return path in self.prefixes

    def _is_valid_word(self, word):
        """
        Checks if the word is valid based on the dictionary and minimum length.
        
        Args:
            word (str): Word to validate
            
        Returns:
            bool: True if word is valid (≥3 letters and in dictionary), False otherwise
        """
        MIN_WORD_LENGTH = 3
        return len(word) >= MIN_WORD_LENGTH and word in self.dictionary

    def is_valid_grid(self):
        """
        Validate the grid to ensure only valid characters are used.
        Specifically checks for proper handling of special tiles (QU, ST).
        
        Returns:
            bool: True if grid contains only valid characters, False otherwise
        """
        VALID_SPECIAL_TILES = ["QU", "ST"]
        SPECIAL_FIRST_LETTERS = {"Q", "S"}
        
        for row in self.grid:
            for cell in row:
                # Invalid cases:
                # 1. Cell length > 2 characters
                # 2. Two-letter combination not in valid special tiles
                # 3. Single Q or S (must be QU or ST)
                if (len(cell) > 2 or 
                    (len(cell) == 2 and cell not in VALID_SPECIAL_TILES) or
                    (len(cell) == 1 and cell in SPECIAL_FIRST_LETTERS)):
                    return False
        return True

    def get_solutions(self):
        """
        Finds and returns all valid words from the grid using DFS.
        
        Returns:
            List[str]: Sorted list of all valid words found in the grid
        """
        # Validate grid before processing
        if not self.is_valid_grid():
            return []
            
        # Check for empty grid
        if self.grid_size == 0 or len(self.grid[0]) == 0:
            return []

        # Start DFS from each cell in the grid
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                self._dfs(row, col, "", set())
                
        return sorted(list(self.found_words))

    def _dfs(self, row, col, current_word, visited_cells):
        """
        Depth First Search from the given cell (row, col) to form words.
        
        Args:
            row (int): Current row position
            col (int): Current column position
            current_word (str): Word formed up to current position
            visited_cells (Set[Tuple]): Set of already visited cell coordinates
        """
        # Check boundary conditions and already visited cells
        if not (0 <= row < self.grid_size and 0 <= col < self.grid_size) or (row, col) in visited_cells:
            return

        # Get current cell's letter(s) and add to current word
        current_cell = self.grid[row][col]
        new_word = current_word + current_cell

        # Mark current cell as visited
        visited_cells.add((row, col))

        # If we've found a valid word, add it to our solutions
        if self._is_valid_word(new_word):
            self.found_words.add(new_word)

        # If current word path could still form valid words, continue DFS
        if self._is_valid_prefix(new_word):
            # Explore all possible directions
            for delta_row, delta_col in self.directions:
                next_row, next_col = row + delta_row, col + delta_col
                self._dfs(next_row, next_col, new_word, visited_cells)

        # Backtrack: remove current cell from visited set
        visited_cells.remove((row, col))


def main():
    """
    Main function to demonstrate the Boggle game functionality with special tiles.
    """
    # Example Boggle board configuration with special tiles
    example_grid = [
        ['A', 'B', 'QU', 'D'],
        ['E', 'F', 'G', 'H'],
        ['I', 'ST', 'K', 'L'],
        ['A', 'B', 'C', 'D']
    ]

    # Example dictionary of valid words to find
    example_dictionary = ['ABEF', 'AFSTK', 'DGKD', 'QUGH']

    # Create and run the Boggle game
    boggle_game = Boggle(example_grid, example_dictionary)
    
    # Find and print all valid words in the grid
    found_words = boggle_game.get_solutions()
    print("Found words:", found_words)


if __name__ == "__main__":
    main()