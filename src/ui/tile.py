import pygame


class Tile:
    """Tile for making a minesweeper grid and buttons.

        A rectangle to draw, with a border that changes color on hover.
        Used for game grid and menu buttons.

        Attributes:
            rect: a rectangle (x, y, width, height)
            border_color: current color of the border, yellow on hover.
            value: string to be shown on the UI.
            index: index of the Tile in a list, or the index corresponding this tile
            font: font used in the Tile.
    """

    def __init__(self, rect, i):
        self.rect = rect
        self.border_color = "darkblue"
        self.value = ""
        self.index = i
        self.font = pygame.font.SysFont('Comic Sans', 20)

    def draw_tile(self, screen):
        """Draws tile without values, color depends on the value.

            Args:
                screen: pygame display
        """
        if self.value == "F":
            pygame.draw.rect(screen, "lightseagreen", self.rect)
        elif self.value == "_":
            if self.value == "_":
                self.value = ""
            pygame.draw.rect(screen, "lightseagreen", self.rect)
        else:
            pygame.draw.rect(screen, "aquamarine2", self.rect)

    def draw_border(self, screen):
        """Draws the tile border with the current color.

            Args:
                screen: pygame display
        """
        pygame.draw.rect(screen, self.border_color, self.rect, width=2, border_radius=2,
                         border_top_left_radius=-1, border_top_right_radius=-1,
                         border_bottom_left_radius=-1, border_bottom_right_radius=-1)

    def handle_hover(self, mouse_pos):
        """Changes Tile border color on hover.

            Args:
                mouse_pos: mouse position, event.pos
        """
        if self.rect.collidepoint(mouse_pos):
            self.border_color = "yellow"
        else:
            self.border_color = "darkblue"
