import random
import pygame
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


class Unit_Snake:
    snake_pos_x = custom_rand_int()
    snake_pos_y = custom_rand_int()
    snake_prev_x = 0
    snake_prev_y = 0
    accelaration = 10
    direction_of_movement = -1

    def get_snake_pos_x(self):
        return self.snake_pos_x

    def set_snake_pos_x(self, snake_pos_x):
        self.snake_pos_x = snake_pos_x

    def get_snake_pos_y(self):
        return self.snake_pos_y

    def set_snake_pos_y(self, snake_pos_y):
        self.snake_pos_y = snake_pos_y

    def get_snake_prev_x(self):
        return self.snake_prev_x

    def set_snake_prev_x(self, snake_prev_x):
        self.snake_prev_x = snake_prev_x

    def get_snake_prev_y(self):
        return self.snake_prev_y

    def set_snake_prev_y(self, snake_prev_y):
        self.snake_prev_y = snake_prev_y

    def get_direction_of_movement(self):
        return self.direction_of_movement

    def set_direction_of_movement(self, direction_of_movement):
        self.direction_of_movement = direction_of_movement

    def get_accelaration(self):
        return self.accelaration

    def set_accelaration(self, accelaration):
        self.accelaration = accelaration

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
        snake.eat_fruit()
        fruit.set_fruit_pos_x(custom_rand_int())
        fruit.set_fruit_pos_y(custom_rand_int())


class Snake:
    head = Unit_Snake()
    tail = None
    body = []
    accelaration = 10

    def __init__(self):
        self.head = Unit_Snake()
        self.head.set_snake_pos_x(custom_rand_int())
        self.head.set_snake_pos_y(custom_rand_int())
        self.body.append(self.head)

    def draw_snake(self):
        for unit in self.body:
            unit.draw_snake()

    def move_snake(self, direction):
        body_length = len(self.body)
        leader_x = self.head.get_snake_pos_x()
        leader_y = self.head.get_snake_pos_y()
        self.head.set_direction_of_movement(direction)
        self.head.move()

        for index in xrange(1, body_length):
            unit = self.body[index]
            unit.set_snake_prev_x(unit.get_snake_pos_x())
            unit.set_snake_prev_y(unit.get_snake_pos_y())
            unit.set_snake_pos_x(leader_x)
            unit.set_snake_pos_y(leader_y)
            leader_x = unit.get_snake_prev_x()
            leader_y = unit.get_snake_prev_y()

    def eat_fruit(self):
        new_unit = Unit_Snake()
        tail = self.body[len(self.body) - 1]
        direction_of_movement = tail.get_direction_of_movement()
        new_unit.set_snake_pos_x(tail.get_snake_pos_x())
        new_unit.set_snake_pos_y(tail.get_snake_pos_y())
        new_unit.set_direction_of_movement(direction_of_movement)
        self.body.append(new_unit)

    def get_snake_pos_x(self):
        return self.head.get_snake_pos_x()

    def get_snake_pos_y(self):
        return self.head.get_snake_pos_y()

    def get_head(self):
        return self.head

    def get_body(self):
        return self.body


def play_game(snake, direction):
    draw_map()
    fruit.draw_fruit()
    snake.move_snake(direction)
    eat_fruit_action(snake, fruit)
    snake.draw_snake()


def draw_map():
    (x, y) = (40, 40)
    (x1, y1) = (560, 400)
    pygame.draw.rect(SCREEN, GREEN, Rect(x, y, x1, y1))


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Welcome to Twirly Snake')
    snake = Snake()
    fruit = Fruit()
    direction = -1
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
