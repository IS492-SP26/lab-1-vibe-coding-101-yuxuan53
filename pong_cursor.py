import pygame
import sys


# ---------- Game Constants ----------
WIDTH, HEIGHT = 800, 600
FPS = 60

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15

PADDLE_SPEED = 7
BALL_SPEED_X = 5
BALL_SPEED_Y = 4

BG_COLOR = (0, 0, 0)
PADDLE_COLOR = (255, 255, 255)
BALL_COLOR = (255, 255, 255)
TEXT_COLOR = (255, 255, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ping-Pong (Cursor)")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Arial", 36)

    # Paddles (left and right)
    left_paddle = pygame.Rect(
        30, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT
    )
    right_paddle = pygame.Rect(
        WIDTH - 30 - PADDLE_WIDTH,
        HEIGHT // 2 - PADDLE_HEIGHT // 2,
        PADDLE_WIDTH,
        PADDLE_HEIGHT,
    )

    # Ball
    ball = pygame.Rect(
        WIDTH // 2 - BALL_SIZE // 2,
        HEIGHT // 2 - BALL_SIZE // 2,
        BALL_SIZE,
        BALL_SIZE,
    )
    ball_vel_x = BALL_SPEED_X
    ball_vel_y = BALL_SPEED_Y

    # Scores
    left_score = 0
    right_score = 0

    running = True
    while running:
        # ----- Event Handling -----
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Left paddle controls: W / S
        if keys[pygame.K_w]:
            left_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_s]:
            left_paddle.y += PADDLE_SPEED

        # Right paddle controls: Up / Down arrows
        if keys[pygame.K_UP]:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN]:
            right_paddle.y += PADDLE_SPEED

        # Constrain paddles to screen
        left_paddle.y = max(0, min(HEIGHT - PADDLE_HEIGHT, left_paddle.y))
        right_paddle.y = max(0, min(HEIGHT - PADDLE_HEIGHT, right_paddle.y))

        # ----- Ball Movement -----
        ball.x += ball_vel_x
        ball.y += ball_vel_y

        # Bounce off top and bottom walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_vel_y *= -1

        # Bounce off paddles
        if ball.colliderect(left_paddle) and ball_vel_x < 0:
            ball_vel_x *= -1
        if ball.colliderect(right_paddle) and ball_vel_x > 0:
            ball_vel_x *= -1

        # Scoring: ball passed left or right edge
        if ball.right < 0:
            right_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_vel_x = BALL_SPEED_X
            ball_vel_y = BALL_SPEED_Y * (-1 if ball_vel_y < 0 else 1)
        elif ball.left > WIDTH:
            left_score += 1
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_vel_x = -BALL_SPEED_X
            ball_vel_y = BALL_SPEED_Y * (-1 if ball_vel_y < 0 else 1)

        # ----- Drawing -----
        screen.fill(BG_COLOR)

        # Draw paddles and ball
        pygame.draw.rect(screen, PADDLE_COLOR, left_paddle)
        pygame.draw.rect(screen, PADDLE_COLOR, right_paddle)
        pygame.draw.ellipse(screen, BALL_COLOR, ball)

        # Center line
        pygame.draw.aaline(
            screen, PADDLE_COLOR, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT)
        )

        # Draw scores
        score_text = font.render(f"{left_score}   {right_score}", True, TEXT_COLOR)
        text_rect = score_text.get_rect(center=(WIDTH // 2, 40))
        screen.blit(score_text, text_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

