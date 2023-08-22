import pygame
from plane_sprites import *

class PlanGame(object):

    def __init__(self):
        print('游戏初始化')
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprite()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)


    def start_game(self):
        while True:
            self.clock.tick(FRAME_PER_SEC)
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_RIGHT]:
            self.hero.rect.x += 2
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.rect.x += -2

    def __create_sprite(self):
        bg = Background()
        bg2 = Background(is_alt=True)
        self.back_group = pygame.sprite.Group(bg, bg2)

        #enemy = Enemy()
        self.enemy_group = pygame.sprite.Group()

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        self.bullet_group = pygame.sprite.Group()

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies):
            self.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()




if __name__ == '__main__':

    # 创建游戏对象
    game = PlanGame()

    # 启动游戏
    game.start_game()

