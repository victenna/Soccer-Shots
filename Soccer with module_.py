#Soccer with module
import turtle,time,random
from module_soccer_sprites import *
from mod_scr import *
wn=turtle.Screen()
wn.setup(1200,750)
wn.bgpic('grass1.gif')
golkip=turtle.Turtle()
golkip.up()
player=turtle.Turtle()
player.up()
wn.addshape('00.gif')
wn.addshape('03.gif')
player.shape('00.gif')
player.showturtle()
player.goto(-100,-250)
ball=turtle.Turtle()
ball.up()
ball. hideturtle()
ball.goto(170,-400)
wn.addshape('ball.gif')
ball.shape('ball.gif')
sprite(golkip,0)
golkip.goto(-120,80)
pos=100,100
n=-1
def right():
    global n
    n=n+1
    n1=n%27
    global pos
    sprite(golkip,n1)
    golkip.fd(15)
    pos=golkip.position()
    
def left():
    global n
    n=n+1
    n1=n%27
    global pos
    sprite(golkip,n1)
    golkip.fd(-15)
    pos=golkip.position()
    
wn.onkey(left,'a')
wn.onkey(right,'s')
wn.listen()
turtle.tracer(1) 
#delta=100
while True:
    ball.hideturtle()    
    ball.setheading(random.randint(40,110))
    player.shape('00.gif')
    player.showturtle()
    X,Y=player.position()
    ball.setposition(X,Y+100)
    ball.hideturtle()
    time.sleep(0.1)
    player.shape('03.gif')
    q=0 
    while q<110:
        if q==0:
            tot_number()
        q=q+1
        ball.showturtle()
        ball.fd(4)
        delta=abs(ball.position()-golkip.position())
        if delta<40:
            ball.hideturtle()
            ball.goto(-100,-150)
            q=111
        if q==109:
            scr()
            ball.hideturtle()    
            ball.goto(-100,-150)
            player.shape('00.gif')
            q=111
          
                