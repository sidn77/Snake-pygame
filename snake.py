import random
import pygame
import copy
from pygame.locals import *

WIDTH = 640
HEIGHT = 480

FRUIT_SIZE = 1

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

GREEN = [50, 125, 25]
BROWN = [90, 10, 0]
RED = [200, 0, 0]

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
    snake.draw_snake(snake.get_head(), snake.get_body())
    fruit.draw_fruit()


def draw_map():
    (x, y) = (40, 40)
    (x1, y1) = (560, 400)
    pygame.draw.rect(SCREEN, GREEN, Rect(x, y, x1, y1))


class Unit_Snake:
    snake_pos_x = custom_rand_int()
    snake_pos_y = custom_rand_int()
    accretion = 1
    counter = 0
    accelaration = 10
    direction_of_movement = -1

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

    def set_direction_of_movement(self, direction_of_movement):
        self.direction_of_movement = direction_of_movement

    def draw_snake(self):
        pygame.draw.rect(SCREEN, BROWN,
                         Rect(self.snake_pos_x,
                              self.snake_pos_y,
                              SNAKE_UNIT_LENGTH, SNAKE_UNIT_WIDTH))

    def move(self):
        if(self.direction_of_movement == K_UP):
            if (self.snake_pos_y - 10) < 40:
                self.snake_pos_y = 430
            else:
                self.snake_pos_y = self.snake_pos_y - self.accelaration
        if(self.direction_of_movement == K_DOWN):
            if (self.snake_pos_y + 10) > 430:
                self.snake_pos_y = 40
            else:
                self.snake_pos_y = self.snake_pos_y + self.accelaration
        if(self.direction_of_movement == K_LEFT):
            if (self.snake_pos_x - 10) < 40:
                self.snake_pos_x = 590
            else:
                self.snake_pos_x = self.snake_pos_x - self.accelaration
        if(self.direction_of_movement == K_RIGHT):
            if (self.snake_pos_x + 10) > 590:
                self.snake_pos_x = 40
            else:
                self.snake_pos_x = self.snake_pos_x + self.accelaration


class Fruit:
    fruit_pos_x = custom_rand_int()
    fruit_pos_y = custom_rand_int()

    def draw_fruit(self):
        pygame.draw.rect(SCREEN, RED,
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
        # snake.eat_fruit()
        fruit.set_fruit_pos_x(custom_rand_int())
        fruit.set_fruit_pos_y(custom_rand_int())


class Snake:
    head = Unit_Snake()
    body = []

    def __init__(self):
        self.head = Unit_Snake()
        self.head.set_snake_pos_x(custom_rand_int())
        self.head.set_snake_pos_y(custom_rand_int())
        self.body.append(self.head)

    def draw_snake(self, head, body):
        # Pop snake_unit from body to pop it
        self.head.draw_snake()

    def move_snake(self, direction):
        # Pop snake_unit from body to move it
        self.head.set_direction_of_movement(direction)
        self.head.move()

    def get_snake_pos_x(self):
        return self.head.get_snake_pos_x()

    def get_snake_pos_y(self):
        return self.head.get_snake_pos_y()

    def get_head(self):
        return self.head

    def get_body(self):
        return self.body


def play_game(snake, direction):
    snake.move_snake(direction)
    eat_fruit_action(snake, fruit)
    draw_map()
    fruit.draw_fruit()
    copy_body = [copy.deepcopy(snake.get_body())]
    snake.draw_snake(snake.get_head(), copy_body)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Welcome to Twirly Snake')
    snake = Snake()
    fruit = Fruit()
    direction = -1
    initialize_game(snake)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if (event.type == pygame.KEYDOWN):
                direction = event.key
        play_game(snake, direction)
        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(9)
        # print clock
