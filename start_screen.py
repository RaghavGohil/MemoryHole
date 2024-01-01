import pygame
import tween
import my_math
import colors
import config
import font_renderer

class StartScreen:

    deltatime = 0.0

    def __init__(self,win:pygame.surface.Surface,message_time:int,fade_time:int)->None:
        self.win = win
        self.font_size = 40
        self.renderer = font_renderer.FontRenderer(win)
        self.font = self.renderer.create_font(self.font_size)
        self.message_time = message_time
        self.current_message = ''
        self.message_counter = 0
        self.fade = False
        self.fade_time = fade_time 
        self.surface = pygame.Surface((config.WIN_SIZE[0],config.WIN_SIZE[1]))
        self.surface.fill(colors.BLACK)
        self.tween_fade = tween.Tween()
        self.messages = ['Welcome','to memory holes.','This is a','challenge.','A really,','really','hard challenge','But I see','there are holes','in your memory.','Anyway.','Your job is','simple.','Reach black hole.','Avoid red places.']
        self.message_tween_dict = {x: tween.Tween() for x in self.messages}

    def draw_start_screen(self):
        if self.message_counter < len(self.messages):
            if not self.message_tween_dict[self.messages[self.message_counter]].finished:
                self.message_tween_dict[self.messages[self.message_counter]].count(self.message_time)
                self.current_message = self.messages[self.message_counter]
            else:
                self.message_counter += 1
        else:
            self.fade = True

        if self.fade == True:
            self.surface.set_alpha(self.tween_fade.value(255,0,self.fade_time))
        self.win.blit(self.surface,(0,0))
        self.__render_font()
    
    def __render_font(self)->None:
        self.renderer.render_font(self.font,self.current_message,colors.WHITE,config.WIN_SIZE[0],config.WIN_SIZE[1],align_center=True,change_alpha=lambda:self.surface.get_alpha())