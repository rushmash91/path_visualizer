import pygame
from bfs import bfs
from matrix import Matrix

width, height = 800, 800
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)

# grid
gwidth, gheight, margin = 155, 155, 5
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
bfs_points = []

# temp
start_point = [1, 3]
end_point = [4, 4]
maze = Matrix(5, start_point, end_point)
maze.print_matrix()
bfs(maze, start_point)
maze.print_matrix()


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
                    select_points()

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


def select_points():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if len(bfs_points) >= 1:
                    make_walls()
                for row_rect in all_rects:
                    for r in row_rect:
                        rect, color = r
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            if color == white:
                                r[1] = black
                                bfs_points.append(rect)
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


def make_walls():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            else:
                for row_rect, row_maze in zip(all_rects, maze.get_matrix()):
                    for r, p in zip(row_rect, row_maze):
                        if p == "0":
                            r[1] = white
                        else:
                            r[1] = black

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
