import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
is_blue = True
x = 30
y = 30
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
    pressed = pygame.key.get_pressed()
    screen.fill((0,0,0))
    surface = pygame.Surface((100, 100))
    if pressed[pygame.K_UP]: y -= 6
    if pressed[pygame.K_DOWN]: y += 6
    if pressed[pygame.K_LEFT]: x -= 6
    if pressed[pygame.K_RIGHT]: x += 6
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 30, 30))
    pygame.display.flip()
    clock.tick(60)