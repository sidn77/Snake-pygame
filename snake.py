import random
import pygame
from pygame.locals import *

WIDTH = 640
HEIGHT = 480

FRUIT_SIZE = 1

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

GREEN = [50, 125, 25]
BROWN = [90, 10, 0]

SNAKE_UNIT_LENGTH = 10
SNAKE_UNIT_WIDTH = 10


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


class Unit_Snake:
    snake_pos_x = custom_rand_int()
    snake_pos_y = custom_rand_int()
    accretion = 1
    direction_of_movement = -1
    counter = 0
    draw_dict = {}

    def __init__(self):
        self.draw_dict = {-1: lambda acc: pygame.draw.rect(SCREEN, BROWN,
                                               Rect(self.snake_pos_x, self.snake_pos_y,
                                                    SNAKE_UNIT_LENGTH, SNAKE_UNIT_WIDTH)),
                          0: lambda acc: pygame.draw.rect(SCREEN, BROWN,
                                              Rect(self.snake_pos_x, self.snake_pos_y - acc,
                                                   SNAKE_UNIT_LENGTH, SNAKE_UNIT_WIDTH)),
                          1: lambda acc: pygame.draw.rect(SCREEN, BROWN,
                                              Rect(self.snake_pos_x, self.snake_pos_y + acc,
                                                   SNAKE_UNIT_LENGTH, SNAKE_UNIT_WIDTH)),
                          2: lambda acc: pygame.draw.rect(SCREEN, BROWN,
                                              Rect(self.snake_pos_x + acc, self.snake_pos_y,
                                                   SNAKE_UNIT_LENGTH, SNAKE_UNIT_WIDTH)),
                          3: lambda acc: pygame.draw.rect(SCREEN, BROWN,
                                              Rect(self.snake_pos_x - acc, self.snake_pos_y,
                                                   SNAKE_UNIT_LENGTH, SNAKE_UNIT_WIDTH))
                          }

    def get_snake_pos_x(self):
        return self.snake_pos_x

    def get_snake_pos_y(self):
        return self.snake_pos_y

    def set_snake_pos_x(self, snake_pos_x):
        self.snake_pos_x = snake_pos_x

    def set_snake_pos_y(self, snake_pos_y):
        self.snake_pos_y = snake_pos_y

    def get_direction_of_movement():
        return direction_of_movement

    def set_direction_of_movement(direction_of_movement):
        self.direction_of_movement = direction_of_movement

    def draw_snake(self):
        for x in xrange(self.accretion):
            self.draw_dict[self.direction_of_movement](x)

    def move(self):
        self.counter += 1
        if(self.counter % 400 == 0):
            if(self.direction_of_movement == 1):
                self.snake_pos_y = 430 if (self.snake_pos_y - 10) < 40 else self.snake_pos_y - 10
            if(self.direction_of_movement == 0):
                self.snake_pos_y = 40 if (self.snake_pos_y + 10) > 430 else self.snake_pos_y + 10
            if(self.direction_of_movement == 2):
                self.snake_pos_x = 590 if (self.snake_pos_x - 10) < 40 else self.snake_pos_x - 10
            if(self.direction_of_movement == 3):
                self.snake_pos_x = 40 if (self.snake_pos_x + 10) > 590 else self.snake_pos_x + 10


class Fruit:
    fruit_pos_x = custom_rand_int()
    fruit_pos_y = custom_rand_int()

    def draw_fruit(self):
        pygame.draw.rect(SCREEN, BROWN,
                         Rect(self.fruit_pos_x, self.fruit_pos_y,
                              SNAKE_UNIT_LENGTH, SNAKE_UNIT_WIDTH))

    def get_fruit_pos_x(self):
        return self.fruit_pos_x

    def get_fruit_pos_y(self):
        return self.fruit_pos_y

    def set_fruit_pos_x(self, fruit_pos_x):
        self.fruit_pos_x = fruit_pos_x

    def set_fruit_pos_y(self, fruit_pos_y):
        self.fruit_pos_y = fruit_pos_y


def eat_fruit_action(snake, fruit):
    snake_pos_x = snake.get_snake_pos_x()
    snake_pos_y = snake.get_snake_pos_y()
    fruit_pos_x = fruit.get_fruit_pos_x()
    fruit_pos_y = fruit.get_fruit_pos_y()

    if snake_pos_x == fruit_pos_x and snake_pos_y == fruit_pos_y:
        snake.eat_fruit()
        fruit.set_fruit_pos_x(custom_rand_int())
        fruit.set_fruit_pos_y(custom_rand_int())


class Snake:
    head = Unit_Snake()
    body = []

    def __init__():
        head.set_snake_pos_x = custom_rand_int()
        head.set_snake_pos_y = custom_rand_int()

    def draw_snake(head, body):
        # Pop snake_unit from body to pop it
        if(body.len < 2):
            return
        else:
            head.draw_snake()
            return draw_snake(body.pop(), body)

    def move_snake(self, event):
        # Pop snake_unit from body to move it
        if(event.type == pygame.KEYDOWN):
            if(event.key == K_DOWN):
                self.direction_of_movement = 0
            if(event.key == K_UP):
                self.direction_of_movement = 1
            if(event.key == K_LEFT):
                self.direction_of_movement = 2
            if(event.key == K_RIGHT):
                self.direction_of_movement = 3


def play_game():
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            snake.move_snake(event)
    snake.move()
    eat_fruit_action(snake, fruit)
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
