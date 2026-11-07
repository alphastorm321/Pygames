import pygame

pygame.init()

screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Color changing cube!")

colors = [
    pygame.Color("white"),
    pygame.Color("red"),
    pygame.Color("green"),
    pygame.Color("blue"),
    pygame.Color("yellow"),
]
color_index = 0

size = 60
x, y = 100, 50
speed_x = 5
speed_y = 4

clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Move by itself
    x += speed_x
    y += speed_y

    # Bounce off the walls and switch color on every hit
    if x <= 0 or x >= screen_width - size:
        speed_x = -speed_x
        color_index = (color_index + 1) % len(colors)
    if y <= 0 or y >= screen_height - size:
        speed_y = -speed_y
        color_index = (color_index + 1) % len(colors)

    # Keep the cube on the screen
    x = min(max(0, x), screen_width - size)
    y = min(max(0, y), screen_height - size)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, colors[color_index], (x, y, size, size))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()