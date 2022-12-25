import pygame
from services.grid import Grid
from services.minesweeper import Minesweeper
from repository.save_file import SaveFile
from repository.highscore_repository import highscore_repository
from .tile import Tile




class GUI:
    """Class for graphical interface for Minesweeper.

        Default game is on 10x10 grid with 5 mines.

        Attributes:
            size: size of the grid (tiles in a row)
            mines: amount of mines
            wins: counter for wins in a row
            grid: a Grid object for Minesweeper
            msweep: a Minesweeper object
            tiles: a list of Tile objects for making an interactable grid in the UI
            menu: a list of Tile objects for sidebar buttons
    """

    def __init__(self, size=10, mines=5, wins=0):

        # if savefile exists, load game. Ignores any errors
        try:
            save = SaveFile.load()
        except:
            save = None

        if save:
            self.size = save.minesweeper.grid.width
            self.mines = save.minesweeper.grid.mines
            self.msweep = save.minesweeper
            self.wins = save.wins
        else:
            self.size = size
            self.mines = mines
            self.wins = wins

            grid = Grid(size)
            grid.set_up_grid(mines)
            self.msweep = Minesweeper(grid)
        self.tiles = []
        self.menu = []

        pygame.init()

        self.init_tiles(size)
        self.init_menu()

    def init_tiles(self, size):
        """Initializes list "tiles" which makes the game grid.

            Makes a list of tiles so an nxn grid can be drawn.

            Args:
                size: width of an nxn grid
        """
        for y in range(size):
            for x in range(size):
                index = x + y*self.msweep.grid.width
                rec = pygame.Rect(x*30, y*30, 30, 30)
                t = Tile(rec, index)
                self.tiles.append(t)

    def init_menu(self):
        """Initializes list "menu" which makes the side bar buttons.

        """
        i = 0
        values = ["restart", "size", "quit"]
        for x in [0, 50, 100]:
            rect = pygame.Rect(300, 0+x, 50, 30)
            button = Tile(rect, i)
            button.value = values[i]
            self.menu.append(button)
            i += 1

    def handle_tile_click(self, mouse_pos):
        """Handles grid tile left clicks.

            Adds clicked tile to opened tiles and changes
            the value of the tile object to the value of the grid.

            Args:
                mouse_pos: mouse position event, event.pos
        """
        for i in range(len(self.tiles)):
            if self.tiles[i].rect.collidepoint(mouse_pos):
                self.msweep.add_shown_tiles(i)
                self.tiles[i].value = str(self.msweep.get_shown_tile(i))

    def save_game_state(self):
        pass

    def set_up_custom_game(self, size, mines):
        try:
            SaveFile.remove()
            self.__init__(size, mines)
        except:
            pass

    def handle_menu(self, mouse_pos):
        """Handles menu button left clicks.

            Handles restart, size and quit buttons of the side bar.
            Right now the "size" doesn't work.
            Saves game on quit.

            Args:
                mouse_pos: mouse position event, event.pos

        """
        for i in range(len(self.menu)):
            if self.menu[i].rect.collidepoint(mouse_pos):
                if self.menu[i].value == "restart":
                    SaveFile.remove()
                    self.__init__(self.size, self.mines)

                elif self.menu[i].value == "size":
                    print("clicked size, now just 10x10 grid with 10 mines")
                    self.set_up_custom_game(10,10)

                elif self.menu[i].value == "quit":
                    print("clicked quit")
                    save = SaveFile(self.msweep, self.wins)
                    save.save()
                    pygame.quit()
                    raise SystemExit

    def toggle_flag(self, mouse_pos):
        """Toggles flag on/off in a tile if mouse position is correct.

            Doesn't add a flag if can't be added (because of Minesweeper-class methods).

            Args:
                mouse_pos: mouse position event, event.pos
        """
        for i in range(len(self.tiles)):
            if self.tiles[i].rect.collidepoint(mouse_pos):
                if i in self.msweep.flags:
                    self.msweep.remove_flag(i)
                else:
                    self.msweep.set_flag(i)
                self.tiles[i].value = self.msweep.get_shown_tile(i)

    def draw_tiles(self, screen):
        """Draws the tiles of the game grid on the GUI.

            Also sets the borders and tile values as is supposed to.

            Args:
                screen: pygame display
        """
        for t in self.tiles:
            t.value = str(self.msweep.get_shown_tile(t.index))
            t.draw_tile(screen)
            t.draw_border(screen)

            if t.value == "0":
                t.value = " "
            shown = " " + t.value
            screen.blit(t.font.render(shown, True, "darkgreen"), t.rect)

    def blit_menu(self, screen, shown, rect):
        """Blits the side bar in right font size for menu.

            Adds text to a rectangle with Comic Sans, in dark green.

            Args:
                screen: pygame display
                shown: string with the text for the rectangle
                rect: rectangle size and position

        """
        screen.blit(pygame.font.SysFont('Comic Sans', 13).render(
            shown, True, "darkgreen"), rect)

    def draw_menu(self, screen):
        """Draws menu buttons on the side bar.

            Args:
                screen: pygame display

        """
        for t in self.menu:
            t.draw_tile(screen)
            t.draw_border(screen)
            shown = " " + t.value
            self.blit_menu(screen, shown, t.rect)

    
    def blit_stats(self, screen, shown, y):
        """Blits the side bar with stats.

            Adds text to a rectangle with Comic Sans, in dark green.

            Args:
                screen: pygame display
                shown: string with the text for the rectangle
                y: stat position on the y axis in the side bar-

        """
        screen.blit(pygame.font.SysFont('Comic Sans', 13).render(
            shown, True, "darkgreen"), pygame.Rect(300, y, 50, 30))


    def draw_stats(self, screen):
        """Shows the stats on the side bar.

            Stats consist of the best 3 highscores (consecutive wins),
            current amount of flags, total amount of mines and the amount of wins in a row.

            Args:
                screen: pygame display
        """

        self.blit_stats(screen, "Best:", 140)

        best = highscore_repository.find_top_3()

        for i in range(len(best)):
            shown = f"#{i+1}: {best[i][1]}, {best[i][0]}"       
            self.blit_stats(screen, shown, 160+20*i)

        flags_left = self.msweep.grid.mines - len(self.msweep.flags)
        shown = f"flags: {flags_left}"
        self.blit_stats(screen, shown, 230)

        shown = f"mines: {self.msweep.grid.mines}"
        self.blit_stats(screen, shown, 250)

        shown = f"wins: {self.wins}"
        self.blit_stats(screen, shown, 270)

    def handle_loss(self, screen):
        """Marks the losing tile red with an X, and starts the game over after a while.

            Win counter is set to default (zero) and save file is destroyed if exists.

            Args:
                screen: pygame display
        """
        losing_tiles = [obj for obj in self.tiles if obj.value == "9"]
        tile = losing_tiles[0]

        SaveFile.remove()

        pygame.draw.rect(screen, "darkred", tile.rect)
        screen.blit(tile.font.render(
            "X", True, "black"), tile.rect)
        pygame.display.flip()
        pygame.time.delay(1000)
        self.__init__(self.size, self.mines)

    def handle_win(self, screen):
        """Draws a happy face in the side bar and starts the game over after a while.

            Win counter goes up by 1, earlier save is removed.
            New row added to highscore database.

            Args:
                screen: pygame display
        """

        #add more users later
        highscore_repository.add("User", self.wins)
        SaveFile.remove()

        print("wins", self.wins)

        rect = (300, 150, 50, 50)
        pygame.draw.rect(screen, "green", rect)
        screen.blit(pygame.font.SysFont('Comic Sans', 30).render(
            ":)", True, "black"), rect)

        pygame.display.flip()
        pygame.time.delay(1500)
        self.__init__(self.size, self.mines, self.wins + 1)

    def pygame_loop(self):
        """ Runs the game loop and the game.

        """
        screen = pygame.display.set_mode([400, 300])
        clock = pygame.time.Clock()
        pygame.display.set_caption("Minesweeper")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save = SaveFile(self.msweep, self.wins)
                    save.save()
                    pygame.quit()
                    raise SystemExit

                # left click
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.handle_tile_click(event.pos)
                    self.handle_menu(event.pos)

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
                self.handle_loss(screen)

            if self.msweep.check_win():
                self.handle_win(screen)

            pygame.display.flip()
            clock.tick(60)
