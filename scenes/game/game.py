from scenes.scene import Scene
from resources.manager import ResourceManager
from scenes.game.player import PlayerEntity

class SceneGame(Scene):

    def __init__(self, gm):
        super().__init__(gm)
        self.player_uid = self.register_entity(PlayerEntity(100, 100))

    def update(self, dt):
        super().update(dt)

    def draw(self):
        super().draw()
        
    def event(self, event):
        super().event(event)