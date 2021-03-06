import pygame
from math import sin


class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        """Create an entity

        Args:
            groups (list[pygame Group]): groups that this object belongs to, or game category
        """
        super().__init__(groups)

        # movement
        self.direction = pygame.math.Vector2()

        # graphics setup
        self.frame_index = 0
        self.animation_speed = 0.15

    def move(self, speed):
        # limit player speed when going diagonal
        # diagonal direction increases vector length
        # use normalize to set vector size to 1
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')

        self.rect.center = self.hitbox.center

    def collision(self, direction: str):
        if direction == 'horizontal':
            for sprite in self.obstacles_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # moving right
                        self.hitbox.right = sprite.hitbox.left  # colliding from left to right
                    elif self.direction.x < 0:  # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacles_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving right
                        self.hitbox.bottom = sprite.hitbox.top  # colliding from left to right
                    elif self.direction.y < 0:  # moving left
                        self.hitbox.top = sprite.hitbox.bottom

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0


if __name__ == '__main__':
    from main import run_game
    run_game()
