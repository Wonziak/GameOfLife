import pygame
import sys
from game_window_class import *
from button_class import *

WIDTH, HEIGHT = 800, 800
BACKGROUND = (199, 199, 199)
FPS = 30


# ----------------------------SETTING---------------------------------#
def get_events():
    global running
    global window_width
    global window_height
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            window_width = event.w
            window_height = event.h
            window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
            window.fill(background)
            reset_game_resize(window_width, window_height)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos, window_width, window_height):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()


def update():
    for button in buttons:
        button.update(mouse_pos)
    game_window.update()
    t = font.render('Iterations: {}'.format(iterations), True, font_color, font_background)
    t_rect = t.get_rect()
    t_rect.centerx, t_rect.centery = WIDTH // 2+5, 155
    window.blit(t, t_rect)
    s = font.render('State: {}'.format(state), True, font_color, font_background)
    s_rect = s.get_rect()
    s_rect.centerx, s_rect.centery = WIDTH // 5, 155
    window.blit(s, s_rect)

def draw():
    for button in buttons:
        button.draw()
    game_window.draw()


# ----------------------------RUNNING---------------------------------#
def running_get_events():
    global running
    global window_width
    global window_height
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            window_width = event.w
            window_height = event.h
            window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
            window.fill(background)
            reset_game_resize(window_width, window_height)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos, window_width, window_height):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()


def running_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)
    game_window.evaluate()
    t = font.render('Iterations: {}'.format(iterations), True, font_color, font_background)
    t_rect = t.get_rect()
    t_rect.centerx, t_rect.centery = WIDTH // 2+5, 155
    window.blit(t, t_rect)
    s = font.render('State: {}'.format(state), True, font_color, font_background)
    s_rect = s.get_rect()
    s_rect.centerx, s_rect.centery = WIDTH // 5, 155
    window.blit(s, s_rect)


def running_draw():
    for button in buttons:
        button.draw()
    game_window.draw()


# ----------------------------PAUSED---------------------------------#
def paused_get_events():
    global running
    global window_width
    global window_height
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            window_width = event.w
            window_height = event.h
            window = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
            window.fill(background)
            reset_game_resize(window_width, window_height)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_on_grid(mouse_pos, window_width, window_height):
                click_cell(mouse_pos)
            else:
                for button in buttons:
                    button.click()


def paused_update():
    game_window.update()
    for button in buttons:
        button.update(mouse_pos)
    t = font.render('Iterations: {}'.format(iterations), True, font_color, font_background)
    t_rect = t.get_rect()
    t_rect.centerx, t_rect.centery = WIDTH // 2+5, 155
    window.blit(t, t_rect)
    s = font.render('State: {}'.format(state), True, font_color, font_background)
    s_rect = s.get_rect()
    s_rect.centerx, s_rect.centery = WIDTH // 5, 155
    window.blit(s, s_rect)


def paused_draw():
    for button in buttons:
        button.draw()
    game_window.draw()


def mouse_on_grid(pos, width=800, height=800):
    if 100 < pos[0] < (width - 100) and 180 < pos[1] < (height - 20):
        return True
    else:
        return False


def click_cell(pos):
    grid_pos = [pos[0] - 100, pos[1] - 180]
    grid_pos[0] = grid_pos[0] // 20
    grid_pos[1] = grid_pos[1] // 20
    if game_window.grid[grid_pos[1]][grid_pos[0]].alive:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = False
    else:
        game_window.grid[grid_pos[1]][grid_pos[0]].alive = True


def make_buttons(width):
    buttons = []
    buttons.append(
        Button(window, width // 5 - 50, 40, 100, 30, text='Run', bgcolor=(28, 111, 51), hovercolor=(48, 161, 81),
               function=run_game))

    buttons.append(
        Button(window, width // 2 - 50, 40, 100, 30, text='Pause', bgcolor=(18, 104, 135), hovercolor=(51, 168, 214),
               function=pause_game))

    buttons.append(
        Button(window, width // 1.2 - 50, 40, 100, 30, text='Reset', bgcolor=(114, 14, 14), hovercolor=(161, 34, 34),
               function=reset_game))

    buttons.append(
        Button(window, width // 5 - 30, 90, 130, 30, text='Niezmienny', bgcolor=(220, 20, 220), hovercolor=(255, 0, 255),
               function=niezmienny))
    buttons.append(
        Button(window, width // 5 + 110, 90, 130, 30, text='Glider', bgcolor=(220, 20, 220), hovercolor=(255, 0, 255),
               function=glider))

    buttons.append(
        Button(window, width // 5 + 250, 90, 130, 30, text='Oscylator', bgcolor=(220, 20, 220), hovercolor=(255, 0, 255),
               function=oscylator))

    buttons.append(
        Button(window, width // 5 + 390, 90, 130, 30, text='Losowe', bgcolor=(220, 20, 220), hovercolor=(255, 0, 255),
               function=losowe))

    buttons.append(
        Button(window, width // 2 - 125, 140, 70, 30, text='+', bgcolor=(220, 20, 220), hovercolor=(255, 0, 255),
               function=iterationincrement))

    buttons.append(
        Button(window, width // 2 + 65, 140, 70, 30, text='-', bgcolor=(220, 20, 220), hovercolor=(255, 0, 255),
               function=iterationdecrement))
    return buttons


def iterationincrement():
    global state
    state = 'setting'
    global iterations
    iterations += 1
    print(iterations)


def iterationdecrement():
    global state
    state = 'setting'
    global iterations
    if iterations > 0:
        iterations -= 1


def niezmienny():
    global state
    state = 'setting'
    mouse_pos = [(393, 470), (419, 472), (432, 489), (366, 489), (389, 510), (411, 511)]
    for pos in mouse_pos:
        click_cell(pos)
    update()
    draw()


def glider():
    global state
    state = 'setting'
    mouse_pos = [(388, 431), (388, 444), (388, 465), (406, 469), (429, 447)]
    for pos in mouse_pos:
        click_cell(pos)
    update()
    draw()


def oscylator():
    global state
    state = 'setting'
    mouse_pos = [(388, 431), (388, 444), (388, 465)]
    for pos in mouse_pos:
        click_cell(pos)
    update()
    draw()


def losowe():
    global state
    state = 'setting'
    mouse_pos = []
    count = random.randint(2, 30)
    for i in range(count):
        mouse_pos.append((random.randint(100, window_width - 100), random.randint(180, window_height - 150)))
    for pos in mouse_pos:
        click_cell(pos)
    update()
    draw()


def run_game():
    global state
    state = 'running'


def pause_game():
    global state
    state = 'paused'


def reset_game():
    global state
    state = 'setting'
    global game_window
    game_window = Game_window(window, 100, 180, window_width=window_width, window_height=window_height)
    global iterations
    iterations = 0
    global counter
    counter = 0


def reset_game_resize(width, height):
    global state
    state = 'setting'
    global game_window
    game_window = Game_window(window, 100, 180, window_width=width, window_height=height)
    global iterations
    iterations = 0
    global counter
    counter = 0


global window_width
global window_height
global counter
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
game_window = Game_window(window, 100, 180)
active = False
iterations = 0

font = pygame.font.SysFont('arial', 20, True)
font_color = (0, 0, 0)
font_background = (255, 0, 255)
buttons = make_buttons(WIDTH)
background = (102, 102, 102)
state = 'setting'
window.fill(background)
running = True
counter = 0

while running:
    mouse_pos = pygame.mouse.get_pos()
    if state == 'setting':
        get_events()
        update()
        draw()
    if state == 'running':
        running_get_events()
        running_update()
        running_draw()
        if iterations != 0:
            counter += 1
    if state == 'paused':
        paused_get_events()
        paused_update()
        paused_draw()
    clock.tick(FPS)
    pygame.display.update()
    if counter == iterations and iterations != 0:
        state = 'paused'
        counter = 0
pygame.quit()
sys.exit()
