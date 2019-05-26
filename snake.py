import random
import pygame
import time
from pygame.locals import *

WIDTH = 640
HEIGHT = 480

SNAKE_LENGTH = 10
FRUIT_SIZE = 1

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

GREEN = [50, 125, 25]
BROWN = [90, 10, 0]

SNAKE_LENGTH = 10
SNAKE_WIDTH = 10


def custom_rand_int():
    rand = random.randint(100, 200)
    remainder = rand % 10
    result = rand if remainder == 0 else rand - remainder
    return result


def initialize_game(snake):
    # TODO: Three diff thread for each ?
    draw_map()
    snake.draw_snake()
    fruit.draw_fruit()


def draw_map():
    (x, y) = (40, 40)
    (x1, y1) = (560, 400)
    pygame.draw.rect(SCREEN, GREEN, Rect(x, y, x1, y1))


class Snake:
    snake_pos_x = custom_rand_int()
    snake_pos_y = custom_rand_int()
    accretion = 1
    move_up = False
    move_down = False
    move_left = False
    move_right = False
    counter = 0

    # def __init__():

    def get_snake_pos_x(self):
        return self.snake_pos_x

    def get_snake_pos_y(self):
        return self.snake_pos_y

    def draw_snake(self):
        pygame.draw.rect(SCREEN, BROWN,
                         Rect(self.snake_pos_x, self.snake_pos_y,
                              SNAKE_LENGTH * self.accretion, SNAKE_WIDTH))

    def move_snake(self, event):
        if(event.type == pygame.KEYDOWN):
            if(event.key == K_DOWN):
                self.move_down = True
                self.move_up = False
                self.move_left = False
                self.move_right = False
            if(event.key == K_UP):
                self.move_up = True
                self.move_down = False
                self.move_left = False
                self.move_right = False
            if(event.key == K_LEFT):
                self.move_left = True
                self.move_up = False
                self.move_down = False
                self.move_right = False
            if(event.key == K_RIGHT):
                self.move_right = True
                self.move_up = False
                self.move_left = False
                self.move_down = False

    def move(self):
        self.counter += 1
        if(self.counter % 400 == 0):
            if(self.move_up):
                self.snake_pos_y = 430 if (self.snake_pos_y - 10) < 40 else self.snake_pos_y - 10
            if(self.move_down):
                self.snake_pos_y = 40 if (self.snake_pos_y + 10) > 430 else self.snake_pos_y + 10
            if(self.move_left):
                self.snake_pos_x = 590 if (self.snake_pos_x - 10) < 40 else self.snake_pos_x - 10
            if(self.move_right):
                self.snake_pos_x = 40 if (self.snake_pos_x + 10) > 590 else self.snake_pos_x + 10

    def eat_fruit(self):
        self.accretion += 1


class Fruit:
    fruit_pos_x = custom_rand_int()
    fruit_pos_y = custom_rand_int()

    def draw_fruit(self):
        pygame.draw.rect(SCREEN, BROWN,
                         Rect(self.fruit_pos_x, self.fruit_pos_y,
                              SNAKE_LENGTH, SNAKE_WIDTH))


def play_game():
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            snake.move_snake(event)
    snake.move()
    draw_map()
    fruit.draw_fruit()
    snake.draw_snake()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Welcome to Twirly Snake')
    snake = Snake()
    fruit = Fruit()
    initialize_game(snake)
    while True:
        play_game()
        pygame.display.update()
