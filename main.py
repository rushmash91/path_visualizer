import pygame

width, height = 800, 800
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)

# grid
gwidth, gheight, margin = 35, 35, 5
clock = pygame.time.Clock()

all_rects = []
for y in range(0, height, gheight + margin):
    row = []
    for x in range(0, width, gwidth + margin):
        rect = pygame.Rect(x, y, gwidth, gheight)
        row.append([rect, white])
    all_rects.append(row)


pygame.init()
screen = pygame.display.set_mode((width, height))
title = pygame.display.set_caption('Path Finder')
logo = pygame.image.load('maze.png')
pygame.display.set_icon(logo)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def intro():

    introduction = True
    btn = pygame.Rect(330, 570, 100, 60)
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn.collidepoint(pygame.mouse.get_pos()):
                    make_walls()

        screen.fill(white)
        text = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = text_objects("Pathfinding Visualizer", text)
        TextRect.center = ((width / 2), (height / 2))
        screen.blit(TextSurf, TextRect)

        pygame.draw.rect(screen, orange, btn)

        text = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Start", text)
        TextRect.center = (380, 600)
        screen.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(15)


def make_walls():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for row in all_rects:
                    for r in row:
                        rect, color = r
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            if color == white:
                                r[1] = black
                            else:
                                r[1] = white
        screen.fill(black)
        # drawing a grid
        for row in all_rects:
            for item in row:
                rect, color = item
                pygame.draw.rect(screen, color, rect)

        pygame.display.update()
        clock.tick(60)


intro()
pygame.quit()
quit()
