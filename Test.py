import pygame,sys
from rocket import Rocket



class Game(object):
    def __init__(self):
        #config
        self.fps_max = 100.0

        #initialization
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.fpsclock = pygame.time.Clock()
        self.fps_delta = 0.0
        self.player = Rocket(self)

        while True:
            # take events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # ticking
            self.fps_delta += self.fpsclock.tick() / 1000.0
            while self.fps_delta > self.fps_max:
                self.tick()
                self.fps_delta-= self.fps_max
            #rendering
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()



    def tick(self):
        self.player.tick()
    def draw(self):
       self.player.draw()


if __name__=="__main__":
    Game()