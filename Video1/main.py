#!/usr/bin/env python
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=no-member

import pygame as pg  # type: ignore

pg.init()

WIDTH = 800
HEIGHT = 600
TITLE = "Open and Close"
FPS = 60


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)

        self.running = True

    def input(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill("BLACK")
        pg.display.flip()

    def run(self):
        while self.running:
            self.input()
            self.draw()

            pg.time.Clock().tick(FPS)


game = Game()
game.run()

pg.quit()
