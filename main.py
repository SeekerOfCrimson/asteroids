import pygame
import sys
import random
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()


    while 1 == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

  
        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collide(player):
                print("Game over!")
                sys.exit()
            
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collide(shot):
                    asteroid.kill()
                    shot.kill()
                    if asteroid.radius <= ASTEROID_MIN_RADIUS:
                        pass
                    else:
                        angle = random.uniform(20,50)
                        v1 = asteroid.velocity.rotate(angle)
                        v2 = asteroid.velocity.rotate(-angle)
                        radius = asteroid.radius - ASTEROID_MIN_RADIUS
                        asteroid1 = Asteroid(asteroid.position.x, asteroid.position.y, radius)
                        asteroid2 = Asteroid(asteroid.position.x, asteroid.position.y, radius)
                        asteroid1.velocity = v1 * 1.2
                        asteroid2.velocity = v2 * 1.2
            
            

        screen.fill("black")
        for item in drawable:
            item.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()