import pygame as pg
from scenes.main_menu.main_menu import SceneMainMenu

class GameWindow:
    
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode([1280, 720])
        self.surface = pg.Surface([1280, 720], pg.SRCALPHA, 32)
        pg.display.set_caption('Farm Farm yumi')
        self.clock = pg.time.Clock()
        self.gm = GameManager(self.surface)
        self.fullscreen = False
        self.loop()

    def loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_F11:
                    if self.fullscreen:
                        pg.display.set_mode([1280, 720])
                    else:
                        pg.display.set_mode([1280, 720], pg.FULLSCREEN)
                    self.fullscreen = not self.fullscreen
                else:
                    self.gm.event(event)
            self.gm.update(1)
            self.surface.fill((0, 0, 0))
            self.gm.draw()
            self.window.blit(self.surface, (0, 0))
            pg.display.flip()
            self.clock.tick(60)

class GameManager:

    def __init__(self, window):
        self.scene = SceneMainMenu(self) #Rellenar
        self.window = window
        
    def update(self, dt):
        self.scene.update(dt)

    def draw(self):
        self.scene.draw()

    def event(self, event):
        self.scene.event(event)

    def change_scene(self, scene):
        self.scene = scene(self)
    
if __name__ == "__main__":
    GameWindow()