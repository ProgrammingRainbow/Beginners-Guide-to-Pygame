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
TITLE = "Sound and Music"
ICON = "images/python-logo.png"
FPS = 60


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)

        self.background = pg.image.load("images/background.png").convert_alpha()
        self.screen_color = (0, 0, 0)
        pg.display.set_icon(pg.image.load(ICON).convert_alpha())

        self.text_vel = 3
        self.text_xvel = self.text_vel
        self.text_yvel = self.text_vel
        self.font = pg.font.Font("fonts/freesansbold.ttf", 60)
        self.text = self.font.render("PyGame", True, (255, 255, 255)).convert_alpha()
        self.text_rect = self.text.get_rect()
        self.text_rect.x = 200

        self.sprite_vel = 5
        self.sprite = pg.image.load("images/python-logo.png").convert_alpha()
        self.sprite_rect = self.sprite.get_rect()

        self.python = pg.mixer.Sound("sounds/python.ogg")
        self.pygame = pg.mixer.Sound("sounds/pygame.ogg")
        self.music = pg.mixer.music.load("music/freesoftwaresong-8bit.ogg")

        self.running = True

    def input(self):
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    self.running = False
                case pg.KEYDOWN:
                    match event.key:
                        case pg.K_ESCAPE:
                            self.running = False
                        case pg.K_SPACE:
                            self.rand_color()
                        case pg.K_m:
                            self.pause_music()

    def draw(self):
        self.screen.fill(self.screen_color)
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.sprite, self.sprite_rect)
        pg.display.flip()

    def rand_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.screen_color = (r, g, b)
        pg.mixer.Sound.play(self.python)

    def update_text(self):
        self.text_rect.x += self.text_xvel
        self.text_rect.y += self.text_yvel
        if self.text_rect.right > WIDTH:
            self.text_xvel = -self.text_vel
            pg.mixer.Sound.play(self.pygame)
        if self.text_rect.left < 0:
            self.text_xvel = self.text_vel
            pg.mixer.Sound.play(self.pygame)
        if self.text_rect.bottom > HEIGHT:
            self.text_yvel = -self.text_vel
            pg.mixer.Sound.play(self.pygame)
        if self.text_rect.top < 0:
            self.text_yvel = self.text_vel
            pg.mixer.Sound.play(self.pygame)

    def update_sprite(self):
        keyboard = pg.key.get_pressed()
        if keyboard[pg.K_LEFT]:
            self.sprite_rect.x -= self.sprite_vel
        if keyboard[pg.K_RIGHT]:
            self.sprite_rect.x += self.sprite_vel
        if keyboard[pg.K_UP]:
            self.sprite_rect.y -= self.sprite_vel
        if keyboard[pg.K_DOWN]:
            self.sprite_rect.y += self.sprite_vel

    def pause_music(self):
        if pg.mixer.music.get_busy():
            pg.mixer.music.pause()
        else:
            pg.mixer.music.unpause()

    def run(self):
        pg.mixer.music.play(-1)
        while self.running:
            self.input()
            self.update_text()
            self.update_sprite()
            self.draw()

            pg.time.Clock().tick(FPS)


game = Game()
game.run()

pg.quit()
