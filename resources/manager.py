from pygame import image

class Resource:

    def __init__(self, filename):
        self.filename = filename
        self.instance = None

    def get_resource(self):
        raise NotImplementedError

class ImageResource(Resource):

    def get_resource(self):
        if self.instance:
            return self.instance
        else:
            self.instance = image.load(self.filename)
            return self.instance

class ResourceManager:

    # TODO: Cargar todos los archivos de resources/images automáticamente
    resources = {
        "images": {
            "pastito": ImageResource("resources/images/pastito.png"),
            "player": ImageResource("resources/images/player.png")
        },
        "sound": {}
    }

    def get_image(self, image):
        return ResourceManager.resources["images"][image].get_resource()

    def get_sound(self, sound):
        # TODO: Implementar para sonidos, y hacer clase SoundResource
        raise NotImplementedError




