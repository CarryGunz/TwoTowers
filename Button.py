import pygame

class Button:
    def __init__(self, posx, posy, button, m_on_button,screen_):
        self.posx = posx
        self.posy = posy
        self.is_glowing = True
        self.buttons = [button, m_on_button]
        self.screen = screen_
    def show(self):
        self.on_object()
        if self.is_glowing:
            self.screen.blit(self.buttons[0], (self.posx, self.posy))

        else:
            self.screen.blit(self.buttons[1], (self.posx, self.posy))

    def on_object(self):
        cx, cy = pygame.mouse.get_pos()
        if((cy > self.posy and cy < (self.posy + 50)) and (cx > self.posx and cx < self.posx + 300)):
            if self.is_glowing == True:
                self.is_glowing = False

        else:
            self.is_glowing = True
