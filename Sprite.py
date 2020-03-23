class Sprite:
    def __init__(self, img):
        self.image = img
        self.x = 0
        self.y = 0
        self.width = img.get_width()
        self.height = img.get_height()
    def checkMouseOn(self, m_x, m_y):
        if self.x + self.width > m_x > self.x \
                and self.y + self.height > m_y > self.y:
            return True
        else:
            return False

    def drawSprite(self, screen):
        screen.blit(self.image, (self.x,self.y))
