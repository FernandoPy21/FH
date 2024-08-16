import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Ball variables
ball = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
ball_speed_x = 7
ball_speed_y = 7

# Paddle variables
paddle1 = pygame.Rect(WIDTH - 20, HEIGHT//2 - 60, 10, 120)
paddle2 = pygame.Rect(10, HEIGHT//2 - 60, 10, 120)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Moving the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle1.y > 0:
        paddle1.y -= 5
    if keys[pygame.K_DOWN] and paddle1.y < HEIGHT - paddle1.height:
        paddle1.y += 5

    if keys[pygame.K_w] and paddle2.y > 0:
        paddle2.y -= 5
    if keys[pygame.K_s] and paddle2.y < HEIGHT - paddle2.height:
        paddle2.y += 5

    # Moving the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x = -ball_speed_x

    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x = WIDTH // 2 - 15
        ball.y = HEIGHT // 2 - 15
        ball_speed_x = 7
        ball_speed_y = 7

    # Fill the screen with black color
    screen.fill(BLACK)

    # Draw the paddles and the ball
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Set the FPS
    pygame.time.Clock().tick(FPS)