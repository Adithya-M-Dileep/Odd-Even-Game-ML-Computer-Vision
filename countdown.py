import pygame
import threading
import time


class Countdown(threading.Thread):
    def __init__(self, window, width, height, gap_size):
        threading.Thread.__init__(self)
        self.window = window
        self.width = width
        self.height = height
        self.gap_size = gap_size
        self.countdown = 3
        self.stopped = threading.Event()

    def run(self):
        while not self.stopped.is_set():
            self.window.fill((0, 0, 0))

            # Display the countdown in the center gap
            font = pygame.font.Font(None, 100)
            text = font.render(str(self.countdown), True, (255, 255, 255))
            text_rect = text.get_rect(
                center=(self.width // 2, self.height // 2))
            self.window.blit(text, text_rect)

            pygame.display.update()

            time.sleep(1)  # Wait for 1 second
            self.countdown -= 1

            if self.countdown == 0:
                self.countdown = 3

    def stop(self):
        self.stopped.set()
