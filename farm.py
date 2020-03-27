import pygame as pg

class GameWindow:
    
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode([1280, 720])
        self.clock = pg.time.Clock()
        self.gm = GameManager(self.window)
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
            self.window.fill((0, 0, 0))
            self.gm.draw()
            pg.display.flip()
            self.clock.tick(60)

class GameManager:

    def __init__(self, window):
        self.scene = None #Rellenar
        self.window = window
        
    def update(self, dt):
        pass

    def draw(self):
        pass

    def event(self, event):
        pass

    
if __name__ == "__main__":
    GameWindow()