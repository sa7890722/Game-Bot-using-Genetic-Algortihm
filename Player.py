import pygame
from time import sleep

height = 30
score = 0

dino_image = pygame.image.load(r'C:\Users\dino.png')


class Player:
    def __init__(self, direction, y_coord, done, screen):
        self.direction = direction
        self.y_coord = y_coord
        self.done = done
        self.score = 0
        self.made_jump = True
        self.screen = screen

    def make_the_jump(self):
        self.done = False
        if self.direction == 0 and not self.done:
            self.y_coord = self.y_coord - 10
            if self.y_coord == 400 - (4 * height):
                self.direction = 1
        elif self.direction == 1 and not self.done:
            self.y_coord = self.y_coord + 10
            if self.y_coord == 400:
                self.direction = 0
                self.done = True
        # pygame.draw.rect(screen, black, (50, self.y_coord - height, 15, 30))
        self.screen.blit(dino_image, (50, self.y_coord - height))
        #sleep(0.003)
        return self.done

    def collided(self, left_bound, right_bound):
        if left_bound <= 75 and right_bound >= 50 and self.y_coord >= 380:
            return True

        else:
            return False

    def collided2(self, left, right, hgt):
        if hgt == 1 and self.y_coord >= 360 and left >= 50 and right <= 70:
            return True
        elif hgt == 0 and 280 <= self.y_coord <= 310 and left >= 50 and right <= 70:
            return True
        else:
            return False

    def update_score(self, scr):
        self.score = scr

    def get_score(self):
        return self.score

    def update_made_jump(self, value):
        self.made_jump = value

    def get_made_jump(self):
        return self.made_jump
