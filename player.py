from settings import *

class Player(pygame.sprite.Sprite):
    # Creating Constructor for Class
    def __init__(self, pos, size=(40, 35), colour=colours['green']):
        # Calling the Parent Classe's Constructor
        super().__init__()
        
        # Creating Core Sprite Attributes
        self.image = pygame.Surface(size)
        self.image.fill(colour)
        self.rect = self.image.get_rect(topleft=pos)
        
        # Creating Core Movement Attributes
        self.grv = .1
        self.jmpsp = -2.5
        self.dir = pygame.math.Vector2(0, 0)
    
    # Creating a Function to Run every Frame
    def update(self):
        # Getting all the Pressed Keys
        keys = pygame.key.get_pressed()
                
        jump = keys[pygame.K_SPACE] or keys[pygame.K_UP]
        
        self.dir.y += self.grv
        if jump: self.dir.y = self.jmpsp
        
        self.rect.x += self.dir.x
        self.rect.y += self.dir.y