import pygame
import config

class FontRenderer:
    def __init__(self,win:pygame.surface.Surface)->None:
        pygame.font.init()
        self.__win = win 
    
    def createFont(self,size)->pygame.font.Font:
        font = pygame.font.Font(config.FONT_LOCATION, size)
        return font

    def renderFont(self,font:pygame.font.Font,message:str,color:tuple,x,y)->None:
        text = font.render(message,config.FONT_ANTIALIAS,color)
        self.__win.blit(text,(x,y))