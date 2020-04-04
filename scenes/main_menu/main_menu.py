from scenes.scene import Scene, GenericEntity
from scenes.game.game import SceneGame
import pygame as pg
from random import randrange

class SceneMainMenu(Scene):

    def __init__(self, gm):
        super().__init__(gm)
        self.font = pg.font.SysFont('Comic Sans MS', 16)
        self.current_option = 0
        self.options_menu = [
            {"text": "Start game", "function": lambda gm: gm.change_scene(SceneGame)},
            {"text": "Options", "function": lambda gm: gm.change_scene(SceneMainMenu)},
            {"text": "Quit", "function": lambda gm: exit()}
            ]
        self.options_len = len(self.options_menu)
        for index, option in enumerate(self.options_menu):
            self.options_menu[index]["uid"] = self.register_entity(Boton(option["text"], 100, 200 + index*30, self.font, option["function"]))
        self.get_entity(self.options_menu[0]["uid"]).is_selected = True
        self.bg_fx_gen_uid = self.register_entity(BackgroundEffectGenerator(self))

    def update(self, dt):
        super().update(dt)
        new_entities = dict()
        for entity_id, entity in self.entities.items():
            if not entity.garbage_collect():
                new_entities[entity_id] = entity

    def draw(self):
        super().draw()

    def event(self, event):
        super().event(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN and self.current_option != self.options_len - 1:
                self.get_entity(self.options_menu[self.current_option]["uid"]).is_selected = False
                self.current_option += 1
                self.get_entity(self.options_menu[self.current_option]["uid"]).is_selected = True
            if event.key == pg.K_UP and self.current_option != 0:
                self.get_entity(self.options_menu[self.current_option]["uid"]).is_selected = False
                self.current_option -= 1
                self.get_entity(self.options_menu[self.current_option]["uid"]).is_selected = True
            if event.key == pg.K_RETURN:
                self.get_entity(self.options_menu[self.current_option]["uid"]).execute(self.gm) 

class Boton(GenericEntity):

    def __init__(self, text, x, y, font, function):
        self.x, self.y = x, y
        self.text = font.render(text, False, (100, 100, 100))
        self.is_selected = False
        self.function = function

    def draw(self, surface):
        surface.blit(self.text, (self.x, self.y))
        if self.is_selected:
            surface.blit(self.text, (self.x + 3, self.y + 3))

    def execute(self, gm):
        self.function(gm)
  
class BackgroundEffect(GenericEntity):

    def __init__(self, x, y, y_speed):
        self.x = x
        self.y = y
        self.y_speed = y_speed
        self.opacity = 255

    def draw(self, surface):
        if self.opacity > 0:
            pg.draw.circle(surface, (255, 255, 255, self.opacity), (self.x, self.y), 5) 

    def update(self, dt):
        self.y += self.y_speed
        self.opacity -= 5

    def garbage_collect(self):
        return self.opacity <= 0

class BackgroundEffectGenerator(GenericEntity):
    
    def __init__(self, scene):
        self.time_to_spawn = 0
        self.scene = scene

    def update(self, dt):
        self.time_to_spawn -= 1
        if self.time_to_spawn <= 0:
            self.time_to_spawn = 2
            for _ in range(4):
                x1, x2 = randrange(0, 1280), randrange(0, 1280)
                self.scene.register_entity(BackgroundEffect(x1, -10, randrange(3, 8)))
                self.scene.register_entity(BackgroundEffect(x2, 730, randrange(-8, -3)))
