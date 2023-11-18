import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player/player.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        self.jump_amt = 30
    
    def set_player(self,pos:tuple)->None:
        self.rect.topleft= pos 
    
    def update(self):
        self.__move_player()

    def draw(self,win:pygame.surface.Surface)->None:
        win.blit(self.image, self.rect)

    def __move_player(self)->None:
        pos = [self.rect.topleft[0],self.rect.topleft[1]]
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w or e.key == pygame.K_UP:
                    pos[1] -= self.jump_amt
                elif e.key == pygame.K_s or e.key == pygame.K_DOWN:
                    pos[1] += self.jump_amt
                elif e.key == pygame.K_a or e.key == pygame.K_LEFT:
                    pos[0] -= self.jump_amt
                elif e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                    pos[0] += self.jump_amt
        self.rect.topleft = tuple(pos)

    def draw_and_update_sprite(self,win:pygame.surface.Surface)->None:
        self.update()
        self.draw(win)