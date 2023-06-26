import pygame


def open_panel(window, width, height, winner):
    running = True

    window.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)
    text = font.render(str(winner[0]), True, winner[1])
    text_rect = text.get_rect(center=(width // 2, height // 2))
    window.blit(text, text_rect)
    pygame.display.update()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
