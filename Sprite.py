class Sprite:
    def __init__(self, img):
        self.image = img
        self.x = 0
        self.y = 0
        self.width = img.get_width()
        self.height = img.get_height()
    def checkMouseOn(self, m_x, m_y):
        return True

    def drawSprite(self, screen):
        screen.blit(self.image, (self.x,self.y))
