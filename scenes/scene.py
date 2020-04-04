from uuid import uuid4

class Scene:

    def __init__(self, gm):
        self.gm = gm 
        self.entities = {} 
        

    def update(self, dt):
        for entity in self.entities.copy().values():
            entity.update(dt)

    def draw(self):
        for entity in self.entities.values():
            entity.draw(self.gm.window)

    def event(self, event):
        for entity in self.entities.values():
            entity.event(event)

    def register_entity(self, entity):
        uid = uuid4()
        self.entities[uid] = entity
        return uid

    def deregister_entity(self, id):
        if self.entities.get(id, False):
            self.entities.pop(id)
        else:
            raise Exception(f"entity not registered: ${id}")

    def get_entity(self, id):
        entity = self.entities.get(id, False)
        if entity:
            return entity
        else:
            raise Exception(f"entity not registered: ${id}")
            

class GenericEntity:
    
    def __init__(self):
        pass
    
    def draw(self, surface):
        pass

    def update(self, dt):
        pass

    def event(self, event):
        pass

    def garbage_collect(self):
        return False