import random

class Mapgrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

def draw_map(graph, width = 3): # funkcja rysuje matrycę mapy
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % '.', end="") # można zamienić kropkę na dowolny znak
        print()

def main():
    g = Mapgrid(15, 10)
    draw_map(g)



if __name__ == '__main__':
    main()


