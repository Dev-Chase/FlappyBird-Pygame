from settings import *

class Pipe(pygame.sprite.Sprite):
    # Creating Class Constructor
    def __init__(self, pos, size, colour=colours['green']):
        # Calling Parent Classe's Constructor
        super().__init__()
        
        # Creating Core Variables
        self.image = pygame.Surface(size)
        self.image.fill(colour)
        self.rect = self.image.get_rect(topleft=pos)
        
    def move(self, n):
        self.rect.x -= n