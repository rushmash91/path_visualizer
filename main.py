import pygame
from bfs import bfs
from matrix import Matrix

width, height = 800, 800
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
orange = (255, 165, 0)
dark_gray = (80, 80, 80)
green = (0, 255, 0)
brown = (156, 76, 0)

# grid
gwidth, gheight, margin = 155, 155, 5
clock = pygame.time.Clock()

bfs_points = []
walls = []

all_rects = []
for y in range(0, height, gheight + margin):
    row = []
    for x in range(0, width, gwidth + margin):
        rect = pygame.Rect(x, y, gwidth, gheight)
        row.append([rect, dark_gray])
    all_rects.append(row)


pygame.init()
screen = pygame.display.set_mode((width, height))
title = pygame.display.set_caption('Path Finder')
logo = pygame.image.load('maze.png')
pygame.display.set_icon(logo)


def execute_bfs(points):
    start_rect = points[0]
    end_rect = points[1]
    for row in all_rects:
        for item in row:
            rect, _ = item
            if rect == start_rect:
                si = all_rects.index(row)
                sj = row.index(item)
            if rect == end_rect:
                ei = all_rects.index(row)
                ej = row.index(item)

    start_point = [si, sj]
    end_point = [ei, ej]
    maze = Matrix(5, start_point, end_point)
    bfs(maze, start_point)
    return maze


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

        screen.fill(yellow)

        # heading
        text = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = text_objects("Path Visualizer", text)
        TextRect.center = (int(width / 2), int(height / 2) - 300)
        screen.blit(TextSurf, TextRect)

        # Description
        text = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Press Start to Select Start and End Points", text)
        TextRect.center = (int(width / 2), int(height / 2))
        screen.blit(TextSurf, TextRect)

        pygame.draw.rect(screen, orange, btn)

        # start button
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
                for row_rect in all_rects:
                    for r in row_rect:
                        rect, color = r
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            if color == dark_gray:
                                r[1] = black
                                bfs_points.append(rect)
                            else:
                                r[1] = dark_gray
            elif len(bfs_points) >= 2:
                make_walls_display()

        screen.fill(black)
        # drawing a grid
        for row in all_rects:
            for item in row:
                rect, color = item
                pygame.draw.rect(screen, color, rect)

        pygame.display.update()
        clock.tick(60)


def make_walls_display():

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

        screen.fill(yellow)

        # heading
        text = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = text_objects("Make Walls", text)
        TextRect.center = (int(width / 2), int(height / 2) - 300)
        screen.blit(TextSurf, TextRect)

        # Description
        text = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Press Start to Select the Wall Cells", text)
        TextRect.center = (int(width / 2), int(height / 2))
        screen.blit(TextSurf, TextRect)

        pygame.draw.rect(screen, orange, btn)

        # start button
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
                for row_rect in all_rects:
                    for r in row_rect:
                        rect, color = r
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            if color == dark_gray:
                                r[1] = black
                                walls.append(rect)
                                print(walls)
                            else:
                                r[1] = dark_gray

        screen.fill(black)
        # drawing a grid
        for row in all_rects:
            for item in row:
                rect, color = item
                pygame.draw.rect(screen, color, rect)
        for rect in bfs_points:
            pygame.draw.rect(screen, brown, rect)

        pygame.display.update()
        clock.tick(60)


def show_path():
    maze = execute_bfs(bfs_points)
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
                            r[1] = dark_gray
                        elif p == "1":
                            r[1] = green
                        else:
                            r[1] = brown

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
