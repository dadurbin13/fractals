import pygame

# Setup display
# Displays on attached monitor if available
pygame.init()
pygame.display.set_caption("H-Tree Fractal")
WINDOW = pygame.display.set_mode(display=(pygame.display.get_num_displays() - 1))

# Set constants
FPS = 10
LINE_WIDTH = 1  # generally, this should be an odd number
FRACTAL_DEPTH = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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


def draw_fractal(middle, line_width, line_height, depth):
    if not get_event():
        return False
    elif depth <= 0:
        return True
    else:
        left_middle = (middle[0] - line_width / 2, middle[1])
        right_middle = (middle[0] + line_width / 2, middle[1])
        left_top = (middle[0] - line_width / 2, middle[1] - line_height / 2)
        left_bottom = (middle[0] - line_width / 2, middle[1] + line_height / 2)
        right_top = (middle[0] + line_width / 2, middle[1] - line_height / 2)
        right_bottom = (middle[0] + line_width / 2, middle[1] + line_height / 2)
        color = (middle[0] % 255, middle[1] % 255, (line_width + line_height) % 255, depth / FRACTAL_DEPTH)

        pygame.draw.line(WINDOW, color, left_middle, right_middle, LINE_WIDTH)
        pygame.draw.line(WINDOW, color, left_top, left_bottom, LINE_WIDTH)
        pygame.draw.line(WINDOW, color, right_top, right_bottom, LINE_WIDTH)

        clock.tick(FPS)
        update_fps()
        pygame.display.update()

        depth -= 1
        line_height /= 2
        line_width /= 2

        draw_fractal(left_top, line_width, line_height, depth)
        draw_fractal(right_top, line_width, line_height, depth)
        draw_fractal(left_bottom, line_width, line_height, depth)
        draw_fractal(right_bottom, line_width, line_height, depth)

    return True


def main():
    line_width = SCREEN_WIDTH / 2
    line_height = SCREEN_HEIGHT / 2

    run = True
    while run:
        run = draw_fractal((SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5), line_width, line_height, FRACTAL_DEPTH)


if __name__ == "__main__":
    main()
