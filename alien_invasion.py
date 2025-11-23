import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("AlienInvasion")
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self.__check_event()
            self.ship.update()
            self.__update_screen()
            # 限制帧率为60，tick()返回delta_time，单位毫秒
            self.clock.tick(60)

    def __check_event(self):
        """监听键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
            

    def __update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        # 每次循环重绘屏幕
        self.screen.fill(self.settings.bg_color) 
        # 绘制飞船 
        self.ship.blitme()      
        # 让最近绘制的屏幕可见
        pygame.display.flip()        

if __name__  == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()