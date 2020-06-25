import os,sys
import pygame
from pygame.locals import *


class App:
    def __init__(self):
        pass
    def start(self):
        FPS = 60
        W = 500  # ширина экрана
        H = 500  # высота экрана
        WHITE = (255, 255, 255)
        BLUE = (0, 70, 225)

        pygame.init()
        sc = pygame.display.set_mode((W, H))
        clock = pygame.time.Clock()
        
        self.player = Player(100,100, "sprites/player")
        self.terrain = Terrain(100, 100)
        # rect1 = pygame.Rect((0, 0, 30, 30))
        # rect1.

        while 1:
        
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
                elif i.type == pygame.KEYDOWN:
                    self.player.update(i.key)
                    CollisionDetector.check_collision(self.player, self.terrain)
                    
            sc.fill(WHITE)
            sc.blit(self.terrain.image, self.terrain.rect)
            sc.blit(self.player.image, self.player.rect)

            pygame.display.update()
            clock.tick(FPS)

class CollisionDetector():
    def __init__(self, first, second):
        pass
    @classmethod
    def check_collision(cls, first, second):
        if pygame.sprite.collide_rect(first, second) == 1:
            print('COLLISION')
        
        

class Terrain(pygame.sprite.Sprite):
    def __init__(self, x ,y):
        self.image = pygame.image.load("sprites/terrain/grass_terrain.png").convert() #load a sprite image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class ObjectActionModel():
    def __init__(self, spriteFolder):
        self.starting_stance = None                 #TODO ЗАМУТИТИТЬ СЮДА стандартну PNGшку якшо фолдер буде пустий
        self.parse_object_folder(spriteFolder)

    def parse_object_folder(self, spriteFolder):
        self.left_moving = []
        self.right_moving = []
        self.up_moving = []
        self.down_moving = []
        
        # if len(sys.argv) == 2:
        #     path = sys.argv[1]
        
        files = os.listdir(spriteFolder)
        for file_name in files:
            if 'down' in file_name:
                if 'rest' in file_name:
                    down_rest = spriteFolder + "/" + file_name
                else:
                    self.down_moving.append(spriteFolder + "/" + file_name)
            elif 'up' in file_name:
                if 'rest' in file_name:
                    up_rest = spriteFolder + "/" + file_name
                else:
                    self.up_moving.append(spriteFolder + "/" + file_name)
            elif 'left' in file_name:
                if 'rest' in file_name:
                    left_rest = spriteFolder + "/" + file_name
                else:
                    self.left_moving.append(spriteFolder + "/" + file_name)
            elif 'right' in file_name:
                if 'rest' in file_name:
                    right_rest = spriteFolder + "/" + file_name
                else:
                    self.right_moving.append(spriteFolder + "/" + file_name)

        self.down_moving_iterator = iter(self.down_moving)
        self.up_moving_iterator = iter(self.up_moving)
        self.right_moving_iterator = iter(self.right_moving)
        self.left_moving_iterator = iter(self.left_moving)
        self.starting_stance = down_rest

    def downMovingSprite(self):
        try:
            return next(self.down_moving_iterator)
        except:
            self.down_moving_iterator = iter(self.down_moving)
            return next(self.down_moving_iterator)
    
    def upMovingSprite(self):
        try:
            return next(self.up_moving_iterator)
        except:
            self.up_moving_iterator = iter(self.up_moving)
            return next(self.up_moving_iterator)
    
    def rightMovingSprite(self):
        try:
            return next(self.right_moving_iterator)
        except:
            self.right_moving_iterator = iter(self.right_moving)
            return next(self.right_moving_iterator)
    
    def leftMovingSprite(self):
        try:
            return next(self.left_moving_iterator)
        except:
            self.left_moving_iterator = iter(self.left_moving)
            return next(self.left_moving_iterator)

class Human(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, spriteFolder):
        pygame.sprite.Sprite.__init__(self)
        self.moving_model = ObjectActionModel(spriteFolder)
        self.image = pygame.image.load(self.moving_model.starting_stance).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self, event):
        if event == pygame.K_LEFT:
            self.move_left()
        elif event == pygame.K_RIGHT:
            self.move_right()
        elif event == pygame.K_UP:
            self.move_up()
        elif event == pygame.K_DOWN:
            self.move_down()

    def move_up(self):
        self.image = pygame.image.load(self.moving_model.upMovingSprite()).convert_alpha()
        self.rect.y -= 10
    def move_down(self):
        self.image = pygame.image.load(self.moving_model.downMovingSprite()).convert_alpha()
        self.rect.y += 10
    def move_left(self):
        self.image = pygame.image.load(self.moving_model.leftMovingSprite()).convert_alpha()
        self.rect.x -= 10
    def move_right(self):
        self.image = pygame.image.load(self.moving_model.rightMovingSprite()).convert_alpha()
        self.rect.x += 10

    def checkCollision(self, terrain):
        col = pygame.sprite.collide_rect(self.rect, terrain)
        if col == True:
            print('hi')

class Player(Human):
    def __init__(self, pos_x, pos_y, spriteFolder):
        super(Player, self).__init__(pos_x, pos_y, spriteFolder)
        pass

    
