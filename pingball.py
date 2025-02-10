import turtle

# Create the screen
s1 = turtle.Screen()
s1.bgcolor('black')
s1.title('PING BALL')

# Create ball and bat objects globally
ball = None
bat1 = None
bat2 = None

# Function to create the ball
def create_ball():
    global ball
    ball = turtle.Turtle()  # CREATING A BALL OBJECT IN TURTLE
    ball.shape('circle')
    ball.color('blue')
    ball.penup()
    ball.dx = 6
    ball.dy = 6

# Function to create bat1
def create_bat1():
    global bat1
    bat1 = turtle.Turtle()
    bat1.shape('square')
    bat1.color('yellow')
    bat1.penup()
    bat1.shapesize(stretch_len=2, stretch_wid=6)
    bat1.goto(-600, 0)

# Function to create bat2
def create_bat2():
    global bat2
    bat2 = turtle.Turtle()
    bat2.shape('square')
    bat2.color('yellow')
    bat2.penup()
    bat2.shapesize(stretch_len=2, stretch_wid=6)
    bat2.goto(600, 0)

# Initialize scores
playerA = 0
playerB = 0

# Creating and initializing the score display
score = turtle.Turtle()
score.speed(0)
score.penup()
score.goto(0, 280)
score.color('red')
score.hideturtle()
score.write(f"playerA: {playerA}  playerB: {playerB}", align='center', font=('arial', 24, 'normal'))

# Function to move bat1 up
def move_up1():
    y = bat1.ycor()
    if y < 250:  # Prevent bat1 from moving off screen
        bat1.sety(y + 20)

# Function to move bat1 down
def move_down1():
    y = bat1.ycor()
    if y > -240:  # Prevent bat1 from moving off screen
        bat1.sety(y - 20)

# Function to move bat2 up
def move_up2():
    y = bat2.ycor()
    if y < 250:  # Prevent bat2 from moving off screen
        bat2.sety(y + 20)

# Function to move bat2 down
def move_down2():
    y = bat2.ycor()
    if y > -240:  # Prevent bat2 from moving off screen
        bat2.sety(y - 20)

# Update the score on the screen
def update_score():
    score.clear()
    score.write(f"playerA: {playerA}  playerB: {playerB}", align='center', font=('arial', 24, 'normal'))

# Set up key bindings
s1.listen()
s1.onkey(move_up1, 'w')
s1.onkey(move_down1, 's')
s1.onkey(move_up2, 'Up')
s1.onkey(move_down2, 'Down')

# Create ball and bats before entering the main event loop
create_ball()
create_bat1()
create_bat2()

# Main game loop
def game_loop():
    global playerA, playerB

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball boundary detection
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 600:
        ball.goto(0, 0)
        playerA += 1
        ball.dy *= -1
        update_score()

    if ball.xcor() < -600:
        ball.goto(0, 0)
        playerB += 1
        ball.dy *= -1
        update_score()

    # Check collision with bats
    if (ball.xcor() > bat2.xcor() - 20 and ball.xcor() < bat2.xcor() + 20) and (ball.ycor() < bat2.ycor() + 50 and ball.ycor() > bat2.ycor() - 50):
        ball.dx *= -1
    if (ball.xcor() < bat1.xcor() + 20 and ball.xcor() > bat1.xcor() - 20) and (ball.ycor() < bat1.ycor() + 50 and ball.ycor() > bat1.ycor() - 50):
        ball.dx *= -1

    # Schedule the next game loop
    s1.ontimer(game_loop, 20)  # Continue the loop every 20 ms

# Start the game loop
game_loop()

# Main event loop
s1.mainloop()
      

       



            



















