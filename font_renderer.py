import pygame
import config

class FontRenderer:
    def __init__(self,win:pygame.surface.Surface)->None:
        pygame.font.init()
        self.__win = win 
    
    def create_font(self,size)->pygame.font.Font:
        font = pygame.font.Font(config.FONT_LOCATION, size)
        return font

    def render_font(self,font:pygame.font.Font,message:str,color:tuple,x=0,y=0,align_center=False,change_alpha=None)->None:
        text = font.render(message,config.FONT_ANTIALIAS,color) #dynamic font
        if align_center:
            text_rect = text.get_rect(center=(config.WIN_SIZE[0]/2, config.WIN_SIZE[1]/2))
            self.__win.blit(text,text_rect)
        else:
            text_rect = text.get_rect(topleft=(x,y))
            self.__win.blit(text,text_rect)