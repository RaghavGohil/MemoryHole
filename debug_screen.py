import pygame
import colors
import config
import font_renderer

class DebugScreen:
    
    win = None
    instance = None
    info_dict = {}

    def __init__(self,win:pygame.surface.Surface)->None:
        DebugScreen.instance = self
        DebugScreen.win = win 
        self.font_size = 15 
        self.renderer = font_renderer.FontRenderer(DebugScreen.win)
        self.font = self.renderer.create_font(self.font_size)
        self.text_pos = 0
        DebugScreen.info_dict.update({'DRIVER ':pygame.display.get_driver()})
        DebugScreen.info_dict.update({'WINSIZE ':pygame.display.get_window_size()})
        DebugScreen.info_dict.update(pygame.display.get_wm_info())
                
    def __get_text_pos(self)->int:    
        self.text_pos += 20
        return self.text_pos
    
    def __reset_text_pos(self)->None:
        self.text_pos = 0

    @staticmethod
    def watch(key,value)->None:
        DebugScreen.info_dict.update({key:value}) 
    
    @staticmethod
    def draw_rect(rect:pygame.rect.Rect)->None:
        if config.DRAW_DEBUG:
            pygame.draw.rect(DebugScreen.win,colors.DEBUG,rect,1)

    def draw_debug_info(self)->None:
        if config.DRAW_DEBUG:
            for info in DebugScreen.info_dict.keys():
                self.renderer.render_font(self.font,f'{info}: {DebugScreen.info_dict[info]}',colors.WHITE,20,self.__get_text_pos())
            self.__reset_text_pos()