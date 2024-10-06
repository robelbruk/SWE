import unittest
from boggle_solver2 import Boggle

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

    def test_Normal_case_3x3(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["ABC", "ABDHI", "CFI", "DEA"]  # Correct expected result
        solution = sorted([x.upper() for x in solution])
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_Normal_case_5x5(self):
        grid = [["A", "R", "F", "T", "Z"], ["B", "C", "I", "E", "X"], 
                ["A", "D", "K", "R", "L"], ["N", "Y", "E", "S", "Q"], ["W", "V", "O", "M", "P"]]
        dictionary = ["arf", "army", "ciel", "derrick", "still"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["ARF", "ARMY", "CIEL", "DERRICK", "STILL"]
        solution = sorted([x.upper() for x in solution])
        expected = sorted(expected)
        self.assertEqual(expected, solution)

class TestSuite_Qu(unittest.TestCase):

    def test_Qu_and_St_Count_As_Two_Chars(self):
        grid = [["QU", "E", "R", "B"], ["S", "T", "A", "P"], ["D", "L", "K", "F"], ["M", "N", "I", "O"]]
        dictionary = ["querbe", "sted"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["QUERBE", "STED"]
        solution = sorted([x.upper() for x in solution])
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_Simple_St_Case(self):
        grid = [["S", "T", "A"], ["R", "N", "E"], ["T", "G", "O"]]
        dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "rat", "start", "tar", "tarp", "ten", "went", "wet"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["ART", "EGO", "GENT", "GET", "NET", "NEW", "NEWT", "PRAT", "PRY", "RAT", "START", "TAR", "TARP", "TEN", "WENT", "WET"]
        solution = sorted([x.upper() for x in solution])
        expected = sorted(expected)
        self.assertEqual(expected, solution)

    def test_Words_Cant_End_With_a_Q(self):
        grid = [["I", "R", "A", "Q"], ["U", "Q", "A", "R"], ["I", "Q", "A", "R"], ["Q", "U", "A", "Q"]]
        dictionary = ["iraq", "quaa", "quari", "ququququ"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = []  # No valid words can end with Q
        self.assertEqual(expected, solution)

    def test_Words_Cant_End_With_a_S(self):
        grid = [["I", "R", "A", "S"], ["U", "S", "A", "R"], ["I", "S", "A", "R"], ["S", "U", "A", "S"]]
        dictionary = ["iras", "saa", "sari", "sssssss"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = []  # No valid words can end with S
        self.assertEqual(expected, solution)

class TestSuite_Simple_Edge_Cases(unittest.TestCase):

    def test_Words_Cant_Cell_More_Than_Once(self):
        grid = [["A", "D", "E"], ["X", "X", "X"], ["X", "X", "X"]]
        dictionary = ["ade", "adexx", "xxxxxx"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = []  # No cell should be used more than once in the same word
        self.assertEqual(expected, solution)

    def test_Words_That_Only_Are_3_or_More_Chars(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "ghefi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        expected = ["ABC", "GHEFI"]  # Words that are 3 or more characters
        solution = sorted([x.upper() for x in solution])
        expected = sorted(expected)
        self.assertEqual(expected, solution)

if __name__ == '__main__':
    unittest.main()