import pygame

class Background(): # no need to create a sprite

    def __init__(self,win:pygame.surface.Surface)->None:
        self.win = win
        self.__backgrounds = [
            pygame.image.load('assets/backgrounds/background1.png').convert(),
        ]
        self.num_backgrounds = len(self.__backgrounds)
    
    def draw_bg(self,background_id:int)->None:
        try:
            bg_img = self.__backgrounds[background_id]
            if bg_img != None:
                self.win.blit(bg_img ,(0,0))
            else:
                raise Exception(f"Unable to draw background with id: {background_id}.")
        except Exception as e:
            print(e)
