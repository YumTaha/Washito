import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft= pos)
        
        self.speed = 5
        self.gravity = 0
        self.initial_rect_y = self.rect.y

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]: self.rect.x += 1 *self.speed
        elif keys[pygame.K_LEFT]: self.rect.x -= 1 *self.speed
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]: self.gravity = -20

    def apply_gravity(self):
        if self.rect.y < self.initial_rect_y + 20: self.gravity += 1
        self.rect.y += self.gravity



    def update(self, x_shift):
        self.apply_gravity()
        self.movement()
        self.rect.x += x_shift