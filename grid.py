from random import randint, choice


class MapGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = [] # or initialize it with walls using get_walls()


def draw_grid(graph, width=2):
    for y in range(graph.height):
        for x in range(graph.width):
            if (x, y) in graph.walls:
                print("%%-%ds" % width % '#', end="")
            else:
                print("%%-%ds" % width % '.', end="")
        print()


def get_walls(g, pct=.3):
    #pct is the percentage of the map covered by walls
    out = []
    for i in range(int(g.height*g.width*pct)//2):

        x = randint(1, g.width-1)
        y = randint(1, g.height-2)
        """ We make two pieces of wall based on the same random x and y
            but adding a bit of noise in order to have passages and more
            cave-looking walls"""
        
        out.append((x, y))
        out.append((x + choice([-1, 0, 1]), y + choice([-1, 0, 1])))
    return out


def main():
    g = MapGrid(30, 15)
    draw_grid(g)


if __name__ == '__main__':
    main()        