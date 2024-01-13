class Scene:
    def __init__(self):
        self.scene_is_finished = False
    def draw(self)->bool:
        print('Scene object doesn\t have a draw function. Skipping.')
        return False