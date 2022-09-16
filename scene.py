class Scene:
    """ Collection of all data required for the raytracing engine"""
    def __init__(self, camera, objects, width, height):
        self.camera = camera
        self.objects = objects
        self.width = width
        self.height = height
