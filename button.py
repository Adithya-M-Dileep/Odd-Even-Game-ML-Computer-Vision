import pygame


class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 255), self.rect)
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        window.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
