import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen

        self.settings = ai_game.settings
        # 获取屏幕的rect属性(外接矩形)
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')

        #获取飞船图像的rect属性(外接矩形)
        self.rect = self.image.get_rect()

        # 飞船的外接矩形的底部中间位置的坐标设置为
        self.rect.midbottom = self.screen_rect.midbottom

        # 飞船是否右移
        self.moving_right = False

        # 飞船是否左移
        self.moving_left = False

        # 飞船速度是float
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # 实际最后的飞船坐标还是被取整了，四舍五入
        self.rect.x = self.x

    def blitme(self):
        """在指定位置绘制飞船"""
        # 传入贴图，还有位置
        self.screen.blit(self.image, self.rect)

    