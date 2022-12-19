import pygame
from services.grid import Grid
from services.minesweeper import Minesweeper
from .tile import Tile


###TODO:
# Visual:
#   - move font placements
#   - show amount of flags ("mines") left
# Minesweeper functionality
#
# choices: some other than only 3x3 grid

class GUI:
    """Class for graphical interface for Minesweeper.
    """

    def __init__(self):
        n = 3
        self.grid = Grid(n)
        self.grid.set_up_grid(2)
        self.msweep = Minesweeper(self.grid)
        self.tiles = []

        pygame.init()

        for y in range(n):
            for x in range(n):
                index = x + y*self.grid.width
                rec = pygame.Rect(x*100, y*100, 80, 80)
                t = Tile(rec, index)
                self.tiles.append(t)

    def open_tile(self, mouse_pos):
        for i in range(len(self.tiles)):
            if self.tiles[i].rect.collidepoint(mouse_pos):
                # tiles[i].value = str(msweep.grid.list[i])
                self.msweep.add_shown_tiles(i)
                self.tiles[i].value = str(self.msweep.get_shown_tile(i))

    def toggle_flag(self, mouse_pos):
        for i in range(len(self.tiles)):
            if self.tiles[i].rect.collidepoint(mouse_pos):
                if i in self.msweep.flags:
                    self.msweep.remove_flag(i)
                else:
                    self.msweep.set_flag(i)
                self.tiles[i].value = self.msweep.get_shown_tile(i)

                if self.tiles[i].value == "_":
                    self.tiles[i].value = ""

    def pygame_loop(self):
        screen = pygame.display.set_mode([300, 300])
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

                # left click
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.open_tile(event.pos)

                # right click
                if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                    self.toggle_flag(event.pos)

                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
                    for i in self.tiles:
                        i.handle_hover(mouse_pos)

            screen.fill("lightgreen")

            for t in self.tiles:
                t.value = str(self.msweep.get_shown_tile(t.index))
                if t.value == "_":
                    t.value = ""
                pygame.draw.rect(screen, "aquamarine1", t.rect)

                pygame.draw.rect(screen, t.color, t.rect, width=2, border_radius=2,
                                border_top_left_radius=-1, border_top_right_radius=-1,
                                border_bottom_left_radius=-1, border_bottom_right_radius=-1)

                screen.blit(t.font.render(t.value, True, "darkgreen"), t.rect)

            if self.msweep.check_loss():
                losing_tiles = [obj for obj in self.tiles if obj.value == "9"]
                tile = losing_tiles[0]
                pygame.draw.rect(screen, "darkred", tile.rect)
                screen.blit(tile.font.render("Hävisit", True, "black"), tile.rect)
                pygame.display.flip()
                pygame.time.delay(1000)
                return

            if self.msweep.check_win():
                rect = (100, 100, 150, 100)
                pygame.draw.rect(screen, "green", rect)
                screen.blit(pygame.font.SysFont('Comic Sans', 30).render("Voitit! :)", True, "black"), rect)
                # pysäytä peli? anna mahdollisuus aloittaa alusta?

            pygame.display.flip()
            clock.tick(60)
