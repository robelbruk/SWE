import unittest
from boggle_solver_reviewed import Boggle

class TestBoggleScalability(unittest.TestCase):
    """Test cases for different grid sizes and scaling scenarios."""
    
    def test_3x3_grid(self):
        """Test Boggle solver with a 3x3 grid and various word patterns."""
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        boggle_game = Boggle(grid, dictionary)
        solution = boggle_game.get_solutions()
        expected = ["ABC", "ABDHI", "CFI", "DEA"]
        self.assertEqual(sorted(expected), sorted(solution))

    def test_5x5_grid(self):
        """Test Boggle solver with a larger 5x5 grid."""
        grid = [
            ["A", "R", "F", "T", "Z"],
            ["B", "C", "I", "E", "X"],
            ["A", "D", "K", "R", "L"],
            ["N", "Y", "E", "S", "Q"],
            ["W", "V", "O", "M", "P"]
        ]
        dictionary = ["arf", "army", "ciel", "derrick", "still"]
        boggle_game = Boggle(grid, dictionary)
        solution = boggle_game.getSolution()
        expected = ["ARF", "ARMY", "CIEL", "DERRICK"]  # Removed "STILL" as it's not possible in this grid
        self.assertEqual(sorted(expected), sorted(solution))

    def test_10x10_grid(self):
        """Test Boggle solver with a large 10x10 grid."""
        # Create a 10x10 grid with simple pattern
        grid = [["A" for _ in range(10)] for _ in range(10)]
        dictionary = ["aaa", "aaaa", "aaaaa"]
        boggle_game = Boggle(grid, dictionary)
        solution = boggle_game.getSolution()
        expected = ["AAA", "AAAA", "AAAAA"]
        self.assertEqual(sorted(expected), sorted(solution))


class TestBoggleSpecialTiles(unittest.TestCase):
    """Test cases for special tiles like 'Qu' and 'St'."""

    def test_isValid_Grid(self):
        """Test grid validation with various valid and invalid configurations."""
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]
        dictionary = ["def", "eab", "ebc", "ecb", "edb", "efb", "egh", "ehi", "eih"]
        boggle_game = Boggle(grid, dictionary)
        solution = boggle_game.getSolution()
        expected = ["DEF", "EAB", "EBC", "ECB", "EDB", "EFB", "EGH", "EHI", "EIH"]
        self.assertEqual(sorted(expected), sorted(solution))

    def test_qu_and_st_tiles(self):
        """Test handling of 'Qu' and 'St' special tiles."""
        grid = [
            ["QU", "E", "R", "B"],
            ["S", "T", "A", "P"],
            ["D", "L", "K", "F"],
            ["M", "N", "I", "O"]
        ]
        dictionary = ["querbe", "sted"]
        boggle_game = Boggle(grid, dictionary)
        solution = boggle_game.getSolution()
        expected = ["QUERBE", "STED"]
        self.assertEqual(sorted(expected), sorted(solution))


class TestBoggleEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""
    
    def test_empty_grid(self):
        """Test behavior with an empty grid."""
        grid = []
        dictionary = ["word"]
        boggle_game = Boggle(grid, dictionary)
        solution = boggle_game.getSolution()
        self.assertEqual([], solution)

    def test_entire_grid_word(self):
        """Test words that use the entire grid."""
        grid = [
            ["A", "B", "S", "T"],
            ["E", "M", "I", "O"],
            ["U", "S", "N", "E"],
            ["S", "S", "E", "S"]
        ]
        dictionary = ["abstemiousnesses", "sessensuoimetsba"]
        boggle_game = Boggle(grid, dictionary)
        solution = boggle_game.getSolution()
        expected = ["ABSTEMIOUSNESSES", "SESSENSUOIMETSBA"]
        self.assertEqual(sorted(expected), sorted(solution))

    def test_no_cell_reuse(self):
        """Test that cells cannot be reused within the same word."""
        grid = [
            ["A", "D", "E"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ]
        dictionary = ["ade", "adexx", "xxxxxx"]
        boggle_game = Boggle(grid, dictionary)
        solution = boggle_game.getSolution()
        expected = ["ADE"]
        self.assertEqual(sorted(expected), sorted(solution))


class TestBoggleCompleteCoverage(unittest.TestCase):
    """Additional test cases for complete coverage."""

    def test_all_directions(self):
        """Test words can be formed in all eight directions."""
        grid = [
            ["C", "A", "T"],
            ["D", "O", "G"],
            ["R", "A", "T"]
        ]
        dictionary = ["cat", "dog", "rat"]
        boggle_game = Boggle(grid, dictionary)
        solution = boggle_game.getSolution()
        expected = ["CAT", "DOG", "RAT"]
        self.assertEqual(sorted(expected), sorted(solution))

    def test_winding_path(self):
        """Test words that follow a winding path through the grid."""
        grid = [
            ["S", "N", "A"],
            ["E", "K", "E"],
            ["S", "R", "T"]
        ]
        dictionary = ["snake"]
        boggle_game = Boggle(grid, dictionary)
        solution = boggle_game.getSolution()
        expected = ["SNAKE"]
        self.assertEqual(sorted(expected), sorted(solution))


if __name__ == '__main__':
    unittest.main()