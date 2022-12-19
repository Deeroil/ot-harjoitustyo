import pygame
from services.grid import Grid
from services.minesweeper import Minesweeper
from .tile import Tile


# TODO:
# Visual:
#   - show amount of flags ("mines") left
# choices: some other than only one size of grid

class GUI:
    """Class for graphical interface for Minesweeper.
    """

    def __init__(self):
        size = 10
        self.grid = Grid(size)
        self.grid.set_up_grid(5)
        self.msweep = Minesweeper(self.grid)
        self.tiles = []
        self.menu = []

        pygame.init()

        # fill tiles
        for y in range(size):
            for x in range(size):
                index = x + y*self.grid.width
                rec = pygame.Rect(x*30, y*30, 30, 30)
                t = Tile(rec, index)
                self.tiles.append(t)

        # fill menu
        i = 0
        values = ["restart", "size", "quit"]
        for x in [0,50, 100]:
            rect = pygame.Rect(300, 0+x, 50, 30)
            button = Tile(rect, i)
            button.value = values[i]
            self.menu.append(button)
            i += 1

    def open_tile(self, mouse_pos):
        for i in range(len(self.tiles)):
            if self.tiles[i].rect.collidepoint(mouse_pos):
                self.msweep.add_shown_tiles(i)
                self.tiles[i].value = str(self.msweep.get_shown_tile(i))
        
        self.click_menu(mouse_pos)

    def click_menu(self, mouse_pos):
        for i in range(len(self.menu)):
            if self.menu[i].rect.collidepoint(mouse_pos):
                if self.menu[i].value == "restart":
                    print("clicked restart")
                    self.__init__()

                elif self.menu[i].value == "size":
                    print("clicked size")
                    self.__init__()

                elif self.menu[i].value == "quit":
                    print("clicked quit")
                    pygame.quit()
                    raise SystemExit

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

    def draw_tiles(self, screen):
         for t in self.tiles:
                t.value = str(self.msweep.get_shown_tile(t.index))

                if t.value == "F":
                    pygame.draw.rect(screen, "lightseagreen", t.rect)
                elif t.value == "_":
                    if t.value == "_":
                        t.value = ""
                    pygame.draw.rect(screen, "lightseagreen", t.rect)
                else:
                    pygame.draw.rect(screen, "aquamarine2", t.rect)

                if t.value == "0":
                    t.value = " "

                # border
                pygame.draw.rect(screen, t.color, t.rect, width=2, border_radius=2,
                                 border_top_left_radius=-1, border_top_right_radius=-1,
                                 border_bottom_left_radius=-1, border_bottom_right_radius=-1)

                shown = " " + t.value
                screen.blit(t.font.render(shown, True, "darkgreen"), t.rect)

    def draw_menu(self, screen):
        for t in self.menu:
            pygame.draw.rect(screen, "aquamarine2", t.rect)
            pygame.draw.rect(screen, t.color, t.rect, width=2, border_radius=2,
                                    border_top_left_radius=-1, border_top_right_radius=-1,
                                    border_bottom_left_radius=-1, border_bottom_right_radius=-1)

            shown = " " + t.value
            screen.blit(pygame.font.SysFont('Comic Sans', 13).render(shown, True, "darkgreen"), t.rect)

    def draw_stats(self, screen):
        """waa.
        """

        flags_left = self.grid.mines - len(self.msweep.flags)
        shown = f"flags: {flags_left}"
        screen.blit(pygame.font.SysFont('Comic Sans', 13).render(shown, True, "darkgreen"), pygame.Rect(300, 250, 50, 30))

        shown = f"mines: {self.msweep.grid.mines}"
        screen.blit(pygame.font.SysFont('Comic Sans', 13).render(shown, True, "darkgreen"), pygame.Rect(300, 270, 50, 30))


    def pygame_loop(self):
        screen = pygame.display.set_mode([350, 300])
        clock = pygame.time.Clock()
        pygame.display.set_caption("Minesweeper")

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

                    for i in self.menu:
                        i.handle_hover(mouse_pos)

            screen.fill("lightgreen")

            self.draw_menu(screen)

            self.draw_tiles(screen)

            self.draw_stats(screen)

            if self.msweep.check_loss():
                losing_tiles = [obj for obj in self.tiles if obj.value == "9"]
                tile = losing_tiles[0]

                pygame.draw.rect(screen, "darkred", tile.rect)
                screen.blit(tile.font.render(
                    "X", True, "black"), tile.rect)
                pygame.display.flip()
                pygame.time.delay(1000)
                self.__init__()
                # return

            if self.msweep.check_win():
                rect = (300, 150, 50, 50)
                pygame.draw.rect(screen, "green", rect)
                screen.blit(pygame.font.SysFont('Comic Sans', 30).render(
                    ":)", True, "black"), rect)

                pygame.display.flip()
                pygame.time.delay(1500)
                self.__init__()

            pygame.display.flip()
            clock.tick(60)
