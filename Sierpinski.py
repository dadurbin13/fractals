import math
# import time

import pygame

# Setup display
# Displays on attached monitor if available
pygame.init()
pygame.display.set_caption("Sierpinski Fractal")
WINDOW = pygame.display.set_mode(display=(pygame.display.get_num_displays() - 1))

# Set constants
FPS = 2
LINE_WIDTH = 0  # fills in a polygon
FRACTAL_DEPTH = 2
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
SCREEN_WIDTH = pygame.display.get_window_size()[0]
SCREEN_HEIGHT = pygame.display.get_window_size()[1]
WINDOW.fill(BLACK)

# To display FPS
fps_bg = pygame.Surface((108, 72))
fps_bg.fill(BLACK)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 72)


def get_event():
    run = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                run = False
                pygame.quit()
            if event.key == pygame.K_SPACE:
                # Pauses the iterations // Can still quit with q
                pause = True
                while pause:
                    for event_paused in pygame.event.get():
                        if event_paused.type == pygame.QUIT:
                            run = False
                            pygame.quit()

                        if event_paused.type == pygame.KEYDOWN:
                            if event_paused.key == pygame.K_q:
                                run = False
                                pygame.quit()
                            if event_paused.key == pygame.K_SPACE:
                                pause = False

    return run


def update_fps():
    fps_text = str(int(clock.get_fps()))
    fps_surface = font.render(fps_text, True, pygame.Color("coral"))
    WINDOW.blit(fps_bg, (SCREEN_WIDTH - 104, SCREEN_HEIGHT - 96))
    WINDOW.blit(fps_surface, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100))
    return


def get_left(top, hypotenuse):
    return (top[0] - hypotenuse / 2, math.sqrt(3) * hypotenuse / 2)


def get_right(top, hypotenuse):
    return (top[0] + hypotenuse / 2, math.sqrt(3) * hypotenuse / 2)


def draw_fractal(top, hypotenuse, color, depth):
    if not get_event():
        return False
    elif depth <= 0:
        return True
    else:
        pygame.draw.polygon(WINDOW, color, (top, get_left(top, hypotenuse), get_right(top, hypotenuse)), LINE_WIDTH)

        clock.tick(FPS)
        update_fps()
        pygame.display.update()

        depth -= 1
        hypotenuse /= 2

        draw_fractal(top, hypotenuse, (RED if color == BLACK else BLACK), depth)
        draw_fractal(get_left(top, hypotenuse), hypotenuse, (RED if color == BLACK else BLACK), depth)
        draw_fractal(get_right(top, hypotenuse), hypotenuse, (RED if color == BLACK else BLACK), depth)

    return True


def main():
    hypotenuse = SCREEN_HEIGHT * 2 / math.sqrt(3)

    run = True
    while run:
        run = draw_fractal((SCREEN_WIDTH / 2, 0), hypotenuse, RED, FRACTAL_DEPTH)


if __name__ == "__main__":
    main()
