import random
import pygame
import sys
from pygame.locals import *

WIDTH = 640
HEIGHT = 480

SNAKE_LENGTH = 10
FRUIT_SIZE = 1

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

GREEN = [50, 125, 25]
BROWN = [90, 10, 0]

SNAKE_LENGTH = 20
SNAKE_WIDTH = 5


def initialize_game(snake):
    # TODO: Three diff thread for each ?
    draw_map()
    snake.draw_snake()
    draw_fruit()


def draw_map():
    (x, y) = (40, 40)
    (x1, y1) = (560, 400)
    pygame.draw.rect(SCREEN, GREEN, Rect(x, y, x1, y1))


class Snake:
    snake_pos_x = random.randint(100, 200)
    snake_pos_y = random.randint(100, 200)

    # def __init__():

    def get_snake_pos_x(self):
        return snake_pos_x

    def get_snake_pos_y(self):
        return snake_pos_y

    def draw_snake(self):
        pygame.draw.rect(SCREEN, BROWN,
                         Rect(self.snake_pos_x, self.snake_pos_y,
                              SNAKE_LENGTH, SNAKE_WIDTH))

    def move_snake(self):
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                if(event.key == K_DOWN):
                    self.snake_pos_y += 10
                if(event.key == K_UP):
                    self.snake_pos_y -= 10
                if(event.key == K_LEFT):
                    self.snake_pos_x -= 10
                if(event.key == K_RIGHT):
                    self.snake_pos_x += 10
                pygame.draw.rect(SCREEN, BROWN,
                                 Rect(self.snake_pos_x, self.snake_pos_y,
                                      SNAKE_LENGTH, SNAKE_WIDTH))


def draw_fruit():
    pass


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Welcome to Twirly Snake')
    snake = Snake()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        # SCREEN.fill((40, 50, 180))
        initialize_game(snake)
        snake.move_snake()
        pygame.display.update()
