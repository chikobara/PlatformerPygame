import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super.image = pygame.surface((size, size))
        super.rect
