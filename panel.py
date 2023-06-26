import pygame
import time
import webcam
import controller
import finalPanel
import random
import handTracking


def open_panel(window, width, height, images):
    running = True
    gap_size = 50
    countdown = 4

    ctime = time.time()
    ptime = ctime
    snapBoolean = True

    GameManager = controller.GameController()

    aiImage = images[6]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if GameManager.GameEnded:
            finalPanel.open_panel(window, width, height,
                                  GameManager.getWinner())
            running = False
        img = webcam.currentFrame(width // 2 - gap_size, height)
        frame_surface = pygame.surfarray.make_surface(img.transpose(1, 0, 2))

        window.fill((0, 0, 0))

        # Display the live webcam feed on the left side
        window.blit(frame_surface, (0, 0))

        # Display the static image on the right side
        window.blit(pygame.transform.scale(
            aiImage, (width // 2 - gap_size, height)), (width // 2 + gap_size, 0))

        # Display the countdown in the center gap
        font = pygame.font.Font(None, 100)
        text = font.render(str(countdown), True, (255, 255, 255))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        window.blit(text, text_rect)

        # human score display
        text = font.render(
            str(GameManager.getHumanPoints()), True, (0, 0, 255))
        text_rect = text.get_rect(midtop=(width // 2, 0))
        window.blit(text, text_rect)

        # ai score display
        text = font.render(str(GameManager.getAiPoints()), True, (255, 0, 0))
        text_rect = text.get_rect(midbottom=(width // 2, height))
        window.blit(text, text_rect)

        ctime = time.time()

        tDiff = ctime-ptime
        if tDiff >= 1:
            countdown -= 1
            ptime = time.time()
        if countdown == 0 and tDiff >= 0.5 and snapBoolean:
            snapBoolean = False
            ai = random.randrange(6)
            human = handTracking.getHandReading(img)
            aiImage = images[ai]
            print(ai, human)
            GameManager.play(ai, human)
        if countdown < 0:
            snapBoolean = True
            countdown = 2

        pygame.display.update()

    pygame.quit()
