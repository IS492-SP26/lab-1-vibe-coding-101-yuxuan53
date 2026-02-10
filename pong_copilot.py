import turtle
import time

# Set up the game window
screen = turtle.Screen()
screen.title("Ping-Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

# Game constants
PADDLE_HEIGHT = 100
PADDLE_WIDTH = 15
BALL_SIZE = 15
BALL_SPEED = 2
PADDLE_SPEED = 20

# Create paddles
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=1, stretch_len=PADDLE_HEIGHT // 20)
left_paddle.penup()
left_paddle.goto(-380, 0)

right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=1, stretch_len=PADDLE_HEIGHT // 20)
right_paddle.penup()
right_paddle.goto(380, 0)

# Create ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)

# Ball velocity
ball.velocity_x = BALL_SPEED
ball.velocity_y = BALL_SPEED

# Create scoreboard
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)
score_display.hideturtle()

left_score = 0
right_score = 0

def update_scoreboard():
    """Update and display the scoreboard"""
    score_display.clear()
    score_display.write(
        f"Left: {left_score}    Right: {right_score}",
        align="center",
        font=("Courier", 24, "normal")
    )

def left_paddle_up():
    """Move left paddle up"""
    if left_paddle.ycor() < 250:
        left_paddle.sety(left_paddle.ycor() + PADDLE_SPEED)

def left_paddle_down():
    """Move left paddle down"""
    if left_paddle.ycor() > -250:
        left_paddle.sety(left_paddle.ycor() - PADDLE_SPEED)

def right_paddle_up():
    """Move right paddle up"""
    if right_paddle.ycor() < 250:
        right_paddle.sety(right_paddle.ycor() + PADDLE_SPEED)

def right_paddle_down():
    """Move right paddle down"""
    if right_paddle.ycor() > -250:
        right_paddle.sety(right_paddle.ycor() - PADDLE_SPEED)

# Set up keyboard controls
screen.listen()
screen.onkey(left_paddle_up, "w")
screen.onkey(left_paddle_down, "s")
screen.onkey(right_paddle_up, "Up")
screen.onkey(right_paddle_down, "Down")

def check_paddle_collision():
    """Check collision with paddles"""
    global ball
    
    # Left paddle collision
    if (
        ball.xcor() < -360
        and left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50
    ):
        if ball.velocity_x < 0:
            ball.velocity_x *= -1.05
            ball.setx(-360)
    
    # Right paddle collision
    if (
        ball.xcor() > 360
        and right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50
    ):
        if ball.velocity_x > 0:
            ball.velocity_x *= -1.05
            ball.setx(360)

def check_wall_collision():
    """Check collision with top/bottom walls"""
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.velocity_y *= -1

def check_out_of_bounds():
    """Check if ball is out of bounds and update score"""
    global left_score, right_score
    
    if ball.xcor() < -400:
        right_score += 1
        ball.goto(0, 0)
        ball.velocity_x = BALL_SPEED
        ball.velocity_y = BALL_SPEED
        update_scoreboard()
    
    if ball.xcor() > 400:
        left_score += 1
        ball.goto(0, 0)
        ball.velocity_x = -BALL_SPEED
        ball.velocity_y = BALL_SPEED
        update_scoreboard()

def move_ball():
    """Move the ball"""
    ball.setx(ball.xcor() + ball.velocity_x)
    ball.sety(ball.ycor() + ball.velocity_y)

# Main game loop
update_scoreboard()

running = True
while running:
    screen.update()
    time.sleep(0.01)
    
    move_ball()
    check_paddle_collision()
    check_wall_collision()
    check_out_of_bounds()