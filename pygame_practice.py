# Game screen/pygame

import pygame

pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT=800, 800

display_surface=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Practice.")

background_img=pygame.transform.scale(pygame.image.load("grid1.jpg").convert(),(SCREEN_WIDTH,SCREEN_HEIGHT))

yellow_img=pygame.transform.scale(pygame.image.load("wave.jpg").convert_alpha(),(200,200))
wave_rect=yellow_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))

text=pygame.font.Font(None,36).render("Hello World",True,pygame.Color('black'))
text_rect=text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 130))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background_img, (0, 0))
        display_surface.blit(wave_img, penguin_rect)
        display_surface.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()