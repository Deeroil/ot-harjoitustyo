import pygame
from services.grid import Grid
from services.minesweeper import Minesweeper


###TODO:
# move font placements
# add Minesweeper functionality hahah
#   - check win
#   - flags
# add later some other than 3x3 grid, but with pygame we'll start with only that

class Tile:
    def __init__(self, rect):
        self.rect = rect
        self.color = "darkblue"
        self.value = ""
        self.font = pygame.font.SysFont('Comic Sans', 30)

    # on every movement of the mouse, maybe necessary, maybe a bad idea?
    def handle_hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = "yellow"
        else:
            self.color = "darkblue"

    # def draw_tile(self):
    #     pygame.draw.rect(screen, self.color, self.rect, width=2, border_radius=2,
    #                      border_top_left_radius=-1, border_top_right_radius=-1,
    #                      border_bottom_left_radius=-1, border_bottom_right_radius=-1)


#not used, just chilling here
class RectGrid:
    def __init__(self, x):
        self.x = x

def pygame_play():
    n = 3
    grid = Grid(n)
    grid.set_mines(3)
    grid.set_neighbors()
    msweep = Minesweeper(grid)

    pygame.init()
    screen = pygame.display.set_mode([500, 500])
    clock = pygame.time.Clock()

    tiles = []

    for y in range(n):
        for x in range(n):
            # print(f"y: {y} x:{x} y+x", y+x)
            rec = pygame.Rect(x*100, y*100, 80, 80)
            t = Tile(rec)
            tiles.append(t)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        # left click
        # TODO: use showntiles instead of just setting value? or?
        # TODO: open neighbors
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            for i in range(len(tiles)):
                if tiles[i].rect.collidepoint(mouse_pos):
                    tiles[i].value = str(msweep.grid.list[i])
        
        # right click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mouse_pos = event.pos
            print("Right click")
            # do flag stuff here, set or remove flag


        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            for i in tiles:
                i.handle_hover(mouse_pos)

        screen.fill("lightgreen")

        for t in tiles:
            if t.value == "9":
                pygame.display.flip()
                pygame.draw.rect(screen, "darkred", t.rect)
                screen.blit(t.font.render("Hävisit", True, "black"), t.rect)
                pygame.display.flip()
                pygame.time.delay(1000)
                return

            pygame.draw.rect(screen, t.color, t.rect, width=2, border_radius=2,
                            border_top_left_radius=-1, border_top_right_radius=-1,
                            border_bottom_left_radius=-1, border_bottom_right_radius=-1)

            screen.blit(t.font.render(t.value, True, "darkgreen"), t.rect)

        pygame.display.flip()
        clock.tick(60)
