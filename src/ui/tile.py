import pygame

class Tile:
    def __init__(self, rect, i):
        self.rect = rect
        self.color = "darkblue"
        self.value = ""
        self.index = i
        self.font = pygame.font.SysFont('Comic Sans', 30)

    # on every movement of the mouse, maybe necessary, maybe a bad idea?
    def handle_hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = "yellow"
        else:
            self.color = "darkblue"