from scenes.scene import GenericEntity
from resources.manager import ResourceManager
import pygame as pg

class PlayerEntity(GenericEntity):

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.sprite = ResourceManager().get_image("player")
        self.acceleration = {
            pg.K_LEFT: 0,
            pg.K_RIGHT: 0,
            pg.K_UP: 0,
            pg.K_DOWN: 0
        }
    
    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y))
    
    def update(self, event):
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.acceleration[pg.K_LEFT] += 1
            self.x -= self.acceleration[pg.K_LEFT]
        else:
            self.acceleration[pg.K_LEFT] = 0

        if keys[pg.K_RIGHT]:
            self.acceleration[pg.K_RIGHT] += 1
            self.x += self.acceleration[pg.K_RIGHT]
        else:
            self.acceleration[pg.K_RIGHT] = 0

        if keys[pg.K_UP]:
            self.acceleration[pg.K_UP] += 1
            self.y -= self.acceleration[pg.K_UP]
        else:
            self.acceleration[pg.K_UP] = 0

        if keys[pg.K_DOWN]:
            self.acceleration[pg.K_DOWN] += 1
            self.y += self.acceleration[pg.K_DOWN]
        else:
            self.acceleration[pg.K_DOWN] = 0