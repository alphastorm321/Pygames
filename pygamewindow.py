import pygame

pygame.init()

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Penguin")

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (400, 500))

penguin = pygame.image.load("penguin.jpg")
penguin = pygame.transform.scale(penguin, (100, 100))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background, (0, 0))
    screen.blit(penguin, (150, 350))

    pygame.display.flip()

pygame.quit()