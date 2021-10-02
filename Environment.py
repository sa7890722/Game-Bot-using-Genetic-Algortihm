# just a sample

import sys

sys.path.append('.')

import pygame
import random
from time import sleep
from Population import build_population
from Player import Player
from NN import Brain
from Natural_Selection import new_population
from Mutation import mutation

pops = []

make_pops = build_population(pops)
pops = make_pops.make_pop()

n = len(pops)
players = []

height = 30
score = 0

birdie = pygame.image.load(r'C:\Users\bird.png')
dino_image = pygame.image.load(r'C:\Users\dino.png')
one = pygame.image.load(r'C:\Users\one_small.png')
two = pygame.image.load(r'C:\Users\one.png')
three = pygame.image.load(r'C:\Users\many.png')

one = pygame.transform.scale(one, (15, height))
two = pygame.transform.scale(two, (30, height))
three = pygame.transform.scale(three, (60, height))
birdie = pygame.transform.scale(birdie, (30, 20))


class Walls:
    def __init__(self, counter):
        self.counter = counter
        self.t = 0

    def draw_rect(self, x):
        self.t = x
        # pygame.draw.rect(screen, red, (x, 400 - height, 15 * self.counter, height))
        if self.counter == 1:
            screen.blit(one, (x, 400 - height))
        elif self.counter == 2:
            screen.blit(two, (x, 400 - height))
        else:
            screen.blit(three, (x, 400 - height))

    def get(self):
        return self.t, self.t + (15 * self.counter)

    def get_width(self):
        return self.counter


class Birds:
    def __init__(self, height):
        self.height = height
        self.t = 0

    def draw_bird(self, x):
        self.t = x
        if self.height == 1:
            screen.blit(birdie, (x, 375))

        else:
            screen.blit(birdie, (x, 280))

    def get(self):
        return self.t, self.height


def get_speed():
    if score < 4000:
        return 10
    elif score < 8000:
        return 12
    elif score < 12000:
        return 14
    elif score < 20000:
        return 16
    else:
        return 20


pygame.init()
screen = pygame.display.set_mode((600, 600))

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
x_coord = 600

best_score = 0
generation = 1


def get_the_fitness(popu, gen, rrd):
    running = True
    score = 0

    x_coord = 600

    for i in range(n):
        players.append(Player(0, 400, False, screen))

    brain_player = []
    for i in range(n):
        brain_player.append((players[i], popu[i]))

    mat = [-1, -1, -1, -1, -1, 1]
    dead = 0
    dead_players = [int(0) for u in range(n)]
    tt = 0
    xr = 300

    rr = 0
    print(gen)
    while running:
        score = score + 1
        screen.fill((173, 216, 210))
        if x_coord == 600:
            obstacle = Walls(random.randint(1, 4))
            mat[1] = obstacle.get_width() * 15
        if random.random() >= 0.1 and xr >= 570 and xr - x_coord >= 200 and rr == 0 and rrd % 2 == 0:
            brd = Birds(random.randint(0, 1))
            brd.draw_bird(xr)
            rr = 1

        if rr == 1:
            bird_data = brd.get()
            altitude = bird_data[1]
            mat[3] = xr - 50
            mat[4] = altitude

        mat[0] = x_coord - 50
        mat[2] = get_speed()

        # print(mat)

        actions = []
        for item in brain_player:
            actions.append(item[1].get_action(mat))

        # print(actions)

        ground = pygame.draw.rect(screen, black, (0, 400, 600, 5))
        idx = -1
        # print("Players alive : " + str(n - dead))
        for item in brain_player:
            idx = idx + 1
            if dead_players[idx] != 0:
                continue
            dino = item[0]
            if dino.get_made_jump():
                # pygame.draw.rect(screen, black, (50, 400 - height, 15, 30))
                screen.blit(dino_image, (50, 400 - height))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    tt = 1
            if actions[idx]:
                if dino.get_made_jump():
                    dino.update_made_jump(dino.make_the_jump())
            if not dino.get_made_jump():
                dino.update_made_jump(dino.make_the_jump())

            obstacle.draw_rect(x_coord)
            if rr == 1:
                brd.draw_bird(xr)
            pygame.display.update()
            # sleep(0.003)
            if x_coord > 0:
                got = obstacle.get()
                if dino.collided(got[0], got[1]):
                    dino.update_score(score)
                    # print("Players alive : " + str(n - 1 - dead))
                    dead_players[idx] = score
                    dead = dead + 1
            if xr > 0 and rr == 1:
                got2 = brd.get()
                if dino.collided2(got2[0], got2[0] + 20, got2[1]):
                    dino.update_score(score)
                    # print("Players alive : " + str(n - 1 - dead))
                    dead_players[idx] = score
                    dead = dead + 1

        sleep(0.005)
        if dead == n:
            running = False
        x_coord = x_coord - get_speed()
        xr = xr - get_speed()

        if xr < -100:
            xr = 600
            rr = 0

        if x_coord < -100:
            x_coord = 600
            rrd = rrd + 1
        # print(score)
        if score > 20000:
            break

    print(score)
    if tt == 1:
        exit(0)
        return [], False
    # pygame.quit()
    print("BEST SCORE ==> " + str(score))

    if score > 20000:
        print("Reached the goal")
        found_the_best = True
        print("ALL SCORES : ")
        for i in range(len(dead_players)):
            if dead_players[i] == 0:
                dead_players[i] = 100000000
        print(dead_players)

        for i in range(n):
            brain_player[i] = (dead_players[i], brain_player[i][0], brain_player[i][1])

        for i in range(n):
            for j in range(i + 1, n):
                if brain_player[i][0] < brain_player[j][0]:
                    ddr1 = brain_player[i]
                    ddr2 = brain_player[j]
                    temp = ddr1
                    ddr1 = ddr2
                    ddr2 = temp
                    brain_player[i] = ddr1
                    brain_player[j] = ddr2

        # print(brain_player)
        # pygame.quit()
        return brain_player, True

    print("ALL SCORES : ")
    print(dead_players)

    for i in range(n):
        brain_player[i] = (dead_players[i], brain_player[i][0], brain_player[i][1])

    for i in range(n):
        for j in range(i + 1, n):
            if brain_player[i][0] < brain_player[j][0]:
                ddr1 = brain_player[i]
                ddr2 = brain_player[j]
                temp = ddr1
                ddr1 = ddr2
                ddr2 = temp
                brain_player[i] = ddr1
                brain_player[j] = ddr2

    # print(brain_player)
    return brain_player, False


found_the_best = False
mr = 0

while True:
    mr, done = get_the_fitness(pops, generation, 0)
    generation = generation + 1
    if done:
        break
    new_pops = new_population(mr)
    mutated_pops = mutation(new_pops)
    populated = build_population(mutated_pops)
    pops = populated.make_pop()
    # print(pops)

for i in range(len(mr)):
    if mr[i][0] == 0:
        mr[i] = (100000000, mr[i][1], mr[i][2])

print(mr)
pygame.quit()
