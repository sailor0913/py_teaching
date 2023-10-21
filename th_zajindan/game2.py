import pygame
import random

# 初始化pygame
pygame.init()

# 隐藏鼠标指针
pygame.mouse.set_visible(False)

# 定义颜色
WHITE = (255, 255, 255)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)
MOVE_SPEED = 10

# 设置窗口大小
SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("砸金蛋游戏")

# 加载和缩放图片
egg_image = pygame.transform.scale(pygame.image.load("黑蛋完整.png"), (250, 375))
broken_egg_image = pygame.transform.scale(pygame.image.load("黑蛋破裂.png"), (250, 375))
hammer_image = pygame.transform.scale(pygame.image.load("锤子.png"), (180, 180))
hammer_rect = hammer_image.get_rect()
# 设置字体
font = pygame.font.SysFont('simhei', 30)

# 定义四个蛋的位置
egg_positions = [(100, 300), (400, 300), (700, 300), (1000, 300)]
egg_broken = [False, False, False, False]

states = ["跳绳200", "英语一篇", "4页数学无错", "拼音2页"]
egg_states = random.sample(states, len(states))

moving = False
display_states = True

def move_towards(source, target, step):
    dx = target[0] - source[0]
    dy = target[1] - source[1]
    distance = (dx**2 + dy**2)**0.5

    if distance <= step:
        return target

    move_x = dx / distance * step
    move_y = dy / distance * step

    return (source[0] + move_x, source[1] + move_y)

move_count = 0
MAX_MOVES = 5

running = True
while running:
    screen.fill(WHITE)

    for idx, pos in enumerate(egg_positions):
        if egg_broken[idx]:
            screen.blit(broken_egg_image, pos)
        else:
            screen.blit(egg_image, pos)
        if display_states:
            text_surface = font.render(egg_states[idx], True, BLACK)
            text_rect = text_surface.get_rect(center=(pos[0] + egg_image.get_width() / 2, pos[1] - 20))
            screen.blit(text_surface, text_rect)

    screen.blit(hammer_image, hammer_rect.topleft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not moving: 
                display_states = False
                target_positions = egg_positions.copy()
                random.shuffle(target_positions)
                moving = True
                egg_broken = [False, False, False, False]
        if event.type == pygame.MOUSEMOTION:
            hammer_rect.topleft = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            hammer_center = hammer_rect.center
            for idx, pos in enumerate(egg_positions):
                egg_rect = egg_image.get_rect(topleft=pos)
                if egg_rect.collidepoint(hammer_center):
                    egg_broken[idx] = True
                    display_states = True

    if moving:
        egg_positions = [move_towards(current, target, MOVE_SPEED) for current, target in zip(egg_positions, target_positions)]
        if egg_positions == target_positions:
            move_count += 1
            if move_count >= MAX_MOVES:
                moving = False
                move_count = 0
            else:
                target_positions = target_positions.copy()
                random.shuffle(target_positions)

    pygame.display.flip()

pygame.quit()
