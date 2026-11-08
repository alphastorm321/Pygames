import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))

x = 100
y = 150

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x - 1
    if keys[pygame.K_RIGHT]:
        x = x + 1
    if keys[pygame.K_UP]:
        y = y - 1
    if keys[pygame.K_DOWN]:
        y = y + 1

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (x, y, 50, 50))
    pygame.draw.rect(screen, (255, 0, 0), (400, 150, 50, 50))
    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()