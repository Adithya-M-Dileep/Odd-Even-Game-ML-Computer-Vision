import pygame
import button
import panel


def main_game_loop():
    pygame.init()

    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Game Panel")

    button_obj = button.Button(300, 200, 200, 100, "Start Game")
    images = []
    for i in range(7):
        images.append(pygame.image.load("Images/"+str(i)+".jpg"))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_obj.is_clicked(mouse_pos):
                    panel.open_panel(window, width, height, images)

        window.fill((0, 0, 0))
        button_obj.draw(window)
        pygame.display.update()

    pygame.quit()


main_game_loop()
