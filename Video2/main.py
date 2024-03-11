#!/usr/bin/env python
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member

import random
import pygame as pg  # type: ignore

pg.init()

WIDTH = 800
HEIGHT = 600
TITLE = "Background, Colors and Icon"
ICON = "images/python-logo.png"
FPS = 60


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)

        self.background = pg.image.load("images/background.png").convert_alpha()
        self.screen_color = (0, 0, 0)
        pg.display.set_icon(pg.image.load(ICON).convert_alpha())

        self.running = True

    def input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                elif event.key == pg.K_SPACE:
                    self.rand_color()

    def draw(self):
        self.screen.fill(self.screen_color)
        self.screen.blit(self.background, (0, 0))
        pg.display.flip()

    def rand_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.screen_color = (r, g, b)

    def run(self):
        while self.running:
            self.input()
            self.draw()

            pg.time.Clock().tick(FPS)


game = Game()
game.run()

pg.quit()
