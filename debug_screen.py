import pygame
import colors
import config
import font_renderer

class DebugScreen:
    def __init__(self,win:pygame.surface.Surface)->None:
        self.font_size = 15 
        self.renderer = font_renderer.FontRenderer(win)
        self.font = self.renderer.create_font(self.font_size)
        self.text_pos = 0
                
    def __get_text_pos(self)->int:    
        self.text_pos += 20
        return self.text_pos
    
    def __reset_text_pos(self)->None:
        self.text_pos = 0

    def draw_debug_info(self,curr_fps:float)->None:
        if config.DRAW_DEBUG:
            self.renderer.render_font(self.font,f'FPS: {str(curr_fps)}',colors.WHITE,20,self.__get_text_pos())
            self.renderer.render_font(self.font,f'DRIVER: {pygame.display.get_driver()}',colors.WHITE,20,self.__get_text_pos())
            self.renderer.render_font(self.font,f'WINSIZE: {pygame.display.get_window_size()}',colors.WHITE,20,self.__get_text_pos())
            for info in pygame.display.get_wm_info().keys():
                self.renderer.render_font(self.font,f'{info}: {pygame.display.get_wm_info()[info]}',colors.WHITE,20,self.__get_text_pos())
            self.__reset_text_pos()