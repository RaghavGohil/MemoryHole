import pygame
import scene

class SceneSequencer:
    def __init__(self,scenes)->None:
        self.scenes = scenes
        self.index = 0

    def draw_scene(self)->None:
        finished = None
        try:
            finished = self.scenes[self.index].draw()
            if finished:
                self.__build_index()
        except Exception as e:
            print(f'Scene index {self.index} method \'draw\' doesn\'t return a boolean, instead returns a {type(finished)}: {e}')

    def __build_index(self)->None:
        if self.index < len(self.scenes)-1:
            self.index += 1