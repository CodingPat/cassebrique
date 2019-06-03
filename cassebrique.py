import pgzrun
import random
from math import copysign

WIDTH = 480
HEIGHT = 640
BALL_SIZE = 20
MARGIN = 0

BRICKS_X = 8
BRICKS_Y = 5
BRICK_W = 60
BRICK_H = 25


def reset():
    """Reset bricks and ball."""
    # First, let's do bricks
    bricks.clear()
    for x in range(BRICKS_X):
        for y in range(BRICKS_Y):
            brick=Actor(brickimages[y],anchor=('left','top'))
            brick.pos=(x*BRICK_W,y*BRICK_H)
            bricks.append(brick)

    # Now reset the ball
    ball.center = (WIDTH / 2, HEIGHT / 3)
    #ball.vel = (random.uniform(-200, 200), 400)
    ball.vel = (random.uniform(-3, 3), 6)
    
    # positioning the bat
    bat.center=(WIDTH / 2, HEIGHT-20)
    bat.dir=0#left=-1 / right=1 / still=0
    bat.dx=5#number pixels for movement

    #register speed to give some offspin to ball
    bat.vx = 0
    bat.prev_centerx = bat.centerx


def draw():
    screen.clear()
    for brick in bricks:
        brick.draw()
    ball.draw()
    bat.draw()

def update():
    x, y = ball.center
    vx, vy = ball.vel

    if ball.top > HEIGHT:
        reset()
        return

    #update bat
    bat.x+=bat.dir*bat.dx
    if bat.left<0:
        bat.left=0
    elif bat.right>WIDTH:
        bat.right=WIDTH
        

    # Update ball 

    x += vx
    y += vy
    ball.center = (x, y)

    # Check for and resolve collisions
    if ball.left < 0:
        vx = abs(vx)
        ball.left=0
    elif ball.right > WIDTH:
        vx = -abs(vx)
        ball.right=WIDTH
    if ball.top < 0:
        vy = abs(vy)
        ball.top=0        
    if ball.colliderect(bat):
        vy = -abs(vy)
        # Add some spin off the paddle
        vx += -30 * bat.vx
    else:
        # Find first collision
        idx = ball.collidelist(bricks)
        if idx != -1:
            brick = bricks[idx]
            # Work out what side we collided on
            dx = (ball.centerx - brick.centerx) / BRICK_W
            dy = (ball.centery - brick.centery) / BRICK_H
            if abs(dx) > abs(dy):
                vx = copysign(vx, dx)
            else:
                vy = copysign(vy, dy)
            del bricks[idx]

    ball.vel = (vx, vy)




def update_bat_vx():
    """calculate bat vx."""
    x = bat.centerx
    dx = x - bat.prev_centerx
    bat.prev_centerx = x

    bat.vx = min(10, max(-10, dx))


def on_key_down(key):
    #print(key)
    if key==keys.LEFT:
        bat.dir=-1
    elif key==keys.RIGHT:
        bat.dir=1

def on_key_up(key):
    bat.dir=0
    
    

#create balls,bat,bricks list
        
ball = Actor('ball')
bat = Actor('bat')

bricks = []

brickimages=['redbrick','orangebrick','yellowbrick','greenbrick','bluebrick']


# Reset bricks and ball at start
reset()


pgzrun.go()
