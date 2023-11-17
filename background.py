import pygame

class Background:

    def __init__(self):
        self.__backgrounds = [
            pygame.image.load('assets/backgrounds/bg1.png'),
        ]
    
    def draw_bg(self,win:pygame.Surface,num_bg:int)->None:
        try:
            bg_img = self.__backgrounds[num_bg]
            if bg_img != None:
                win.blit(bg_img ,(0,0))
            else:
                raise Exception(f"Unable to render {num_bg}")
        except Exception as e:
            print(e)