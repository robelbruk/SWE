class Boggle:
  def __init__(self, grid, dictionary):



    def main():
        grid = [['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'], 
            ['I', 'J', 'K', 'L'], 
            ['A', 'B', 'C', 'D']]

        dictionary = ['ABEF', 'AFJIEB', 'DGKD', 'DGKA']

        mygame = Boggle(grid, dictionary)
        print(mygame.solution())

        if __name__ == "__main__":
            main()


