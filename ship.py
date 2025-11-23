import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        # 获取屏幕的rect属性(外接矩形)
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像
        self.image = pygame.image.load('images/ship.bmp')

        #获取飞船图像的rect属性(外接矩形)
        self.rect = self.image.get_rect()

        # 飞船的外接矩形的底部中间位置的坐标设置为
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在指定位置绘制飞船"""
        # 传入贴图，还有位置
        self.screen.blit(self.image, self.rect)

    