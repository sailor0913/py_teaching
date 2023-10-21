import pygame
import random

# 初始化pygame
pygame.init()

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# 设置窗口大小
SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("砸金蛋游戏")

# 加载和缩放图片
egg_image = pygame.transform.scale(pygame.image.load("黑蛋完整.png"), (250, 375))
broken_egg_image = pygame.transform.scale(pygame.image.load("黑蛋破裂.png"), (250, 375))
jumper_image = pygame.transform.scale(pygame.image.load("拿剑小人.png"), (180, 180))


# 定义金蛋类
class Egg(pygame.sprite.Sprite):
    def __init__(self, number, x, y, activity):
        super().__init__()
        self.number = number
        self.image = egg_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.activity = activity # 金蛋是否被砸破

    def draw_number(self):
        font = pygame.font.SysFont('arial', 40)
        text = font.render(str(self.number), True, BLACK)
        screen.blit(text, (self.rect.x + self.rect.width/2 - 20, self.rect.y + self.rect.height/2 - 20))

    def break_egg(self):
        self.image = broken_egg_image

def reset_game(eggs, egg_positions):
    eggs.empty()
    # activities = ["下去玩", "打游戏", "吃好吃的", "看动画片"]
    # activities = ["吃好吃的", "吃好吃的", "吃好吃的", "吃好吃的"]
    activities = ["跳绳200", "英语一篇", "4页数学无错", "拼音2页"]
    random.shuffle(activities) # 随机排序活动
    for i, (pos, activity) in enumerate(zip(egg_positions, activities)):
        egg = Egg(i+1, pos[0], pos[1], activity)
        eggs.add(egg)
    return 0, random.randint(5, 8), False, False, None

# 主游戏循环
def game_loop():
    clock = pygame.time.Clock()
    eggs = pygame.sprite.Group()
    egg_positions = [(100, 300), (400, 300), (700, 300), (1000, 300)]
    for i, pos in enumerate(egg_positions):
        egg = Egg(i+1, pos[0], pos[1], None)
        eggs.add(egg)

    jumper_index, jump_times, jumping, game_over, broken_egg_activity = reset_game(eggs, egg_positions)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_over:
                        # 如果游戏结束，则重置游戏状态
                        jumper_index, jump_times, jumping, game_over, broken_egg_activity = reset_game(eggs, egg_positions)
                    elif not jumping:
                        jumping = True

        screen.fill(WHITE)

        if jumping:
            jumper_index += 1
            if jumper_index >= len(egg_positions):
                jumper_index = 0
            jump_times -= 1
            if jump_times <= 0:
                jumping = False
                eggs.sprites()[jumper_index].break_egg()  # 破裂对应的金蛋
                game_over = True
                broken_egg_activity = eggs.sprites()[jumper_index].activity  # 获取破裂金蛋的活动

        jumper_x, jumper_y = egg_positions[jumper_index]
        jumper_y -= 100  # 适当地调整小人的位置
        screen.blit(jumper_image, (jumper_x+30, jumper_y-40))  # 这里的-40是为了使小人的中心对准金蛋的顶部

        for egg in eggs:
            egg.draw_number()

        eggs.draw(screen)

        clock.tick(2)  # 控制跳跃速度
        
        if game_over and broken_egg_activity:
            font = pygame.font.SysFont('simhei', 60)
            activity_text = font.render(broken_egg_activity, True, BLACK)
            text_rect = activity_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            screen.blit(activity_text, text_rect)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    game_loop()
