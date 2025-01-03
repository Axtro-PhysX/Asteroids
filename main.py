import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    # Initialize pygame
    pygame.init()

    # Set Delta Time to 60 frames per second to not stress CPU
    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0, 0, 0) # the color black for screen fill

    # spawn the player ship before the game loop
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # instantiate asteroid group

    # instantiate groups before the game loop
    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        updatable.update(dt)
        for obj in asteroids:
            if obj.collision(player):
                sys.exit("Game over!")
            for shot in shots:
                if obj.collision(shot):
                    shot.kill()
                    obj.split()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()