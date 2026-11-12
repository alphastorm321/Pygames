import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("press space to change the colours")
clock = pygame.time.Clock()
CHANGE_COLOUR = pygame.USEREVENT + 1
colours = ["red", "green", "blue", "yellow", "purple"]
class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill(colours[0])
        self.rect = self.image.get_rect(center=(x, y))
    def change_colour(self, colour):
        self.image.fill(colour)
box1 = Box(180, 200)
box2 = Box(420, 200)
sprites = pygame.sprite.Group(box1, box2)
number = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pygame.event.post(pygame.event.Event(CHANGE_COLOUR))
        if event.type == CHANGE_COLOUR:
            number = number + 1
            if number == len(colours):
                number = 0
            box1.change_colour(colours[number])
            box2.change_colour(colours[len(colours) - 1 - number])
    screen.fill("black")
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()