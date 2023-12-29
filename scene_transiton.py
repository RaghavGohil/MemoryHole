import pygame
import animator

class SceneTransition(pygame.sprite.Sprite):
    def __init__(self):
        self.animator = animator.Animator()
        self.animation_fps = 10 #frames to play in a sec

        self.scene_transition_animation = []

        self.animator.add_animation('scene_transition_animation',self.scene_transition_animation) 
 
        self.image = self.animator.image
        self.rect = self.image.get_rect()
        
        self.scene_has_changed = False # level load function is called

    @staticmethod
    def animate(self):
        self.scene_has_changed = True

    def update(self):
        if self.scene_has_changed:
            pass

