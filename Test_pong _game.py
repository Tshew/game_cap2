import unittest
import pygame
import sys
# from Pong_Game import *

# Copy your game code here (excluding the pygame.quit() and sys.exit() lines)

WIDTH, HEIGHT = 600, 800
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('pong')

WHITE = (255, 255, 255)
BLACK = (0,0,0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20,120
PADDLE_SPEED = 15

BALL_SIZE = 20
BALL_SPEED_X, BALL_SPEED_Y = 6,6

L_PADDLE = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
R_PADDLE = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
class TestPongGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('pong')

    def tearDown(self):
        pygame.quit()
        # sys.exit()

    def test_move_paddles(self):
        # Test moving paddles up and down
        keys = {
            pygame.K_w: True,
            pygame.K_s: False,
            pygame.K_UP: True,
            pygame.K_DOWN: False
        }
        pygame.key.get_pressed = lambda: keys
        initial_position = L_PADDLE.y
        # move_paddles()
        # self.assertEqual(L_PADDLE.y, initial_position - PADDLE_SPEED)

        keys[pygame.K_w] = False
        keys[pygame.K_s] = True
        keys[pygame.K_UP] = False
        keys[pygame.K_DOWN] = True
        initial_position = R_PADDLE.y
        # move_paddles()
        #self.assertEqual(R_PADDLE.y, initial_position + PADDLE_SPEED)

    def test_move_ball(self):
        # Test moving the ball
        global BALL_SPEED_X, BALL_SPEED_Y
        initial_position = ball.x, ball.y
        # move_ball()
        #self.assertEqual((ball.x, ball.y), (initial_position[0] + BALL_SPEED_X, initial_position[1] + BALL_SPEED_Y))

    def test_collision_with_walls(self):
        # Test ball collision with walls
        global BALL_SPEED_X, BALL_SPEED_Y
        ball.top = 0
        BALL_SPEED_Y = abs(BALL_SPEED_Y)
        # move_ball()
        #self.assertEqual(BALL_SPEED_Y, -abs(BALL_SPEED_Y))  # Ball should bounce off the top wall

        ball.bottom = HEIGHT
        BALL_SPEED_Y = -abs(BALL_SPEED_Y)
        #move_ball()
        #self.assertEqual(BALL_SPEED_Y, abs(BALL_SPEED_Y))  # Ball should bounce off the bottom wall

        ball.left = 0
        BALL_SPEED_X = abs(BALL_SPEED_X)
        # move_ball()
        # self.assertEqual((ball.x, ball.y), (WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2))  # Ball should reset to center

        ball.right = WIDTH
        BALL_SPEED_X = -abs(BALL_SPEED_X)
        # move_ball()
        # self.assertEqual((ball.x, ball.y), (WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2))  # Ball should reset to center

    def test_collision_with_paddles(self):
        # Test ball collision with paddles
        global BALL_SPEED_X, BALL_SPEED_Y
        # ball.colliderect = lambda rect: True  # Mocking the collision
        initial_speed_x = BALL_SPEED_X
        #move_ball()
        #self.assertEqual(BALL_SPEED_X, -initial_speed_x)  # Ball should bounce off the paddles

if __name__ == '__main__':
    unittest.main()
