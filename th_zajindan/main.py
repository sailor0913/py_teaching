import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("砸金蛋游戏")




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()