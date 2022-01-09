import turtle as t
import time

class Letter:
    def __init__(self):
        pass

    #CREATE PEN
    def create():
        t.clear()
        t.hideturtle()
        t.shape('turtle')
        t.shapesize(4)
        t.color('pink')
        t.pensize(30)
        t.pencolor('red')

    #POSITION
    def jump(x,y,deg):
        time.sleep(1)
        t.penup()
        t.speed(0)
        t.setheading(deg) 
        t.setx(x)
        t.sety(y)
        t.showturtle()
        t.pendown()
        t.speed(1)
        time.sleep(1)

    #FINISH
    def finish():
        time.sleep(1)
        t.hideturtle()
        t.exitonclick()
        time.sleep(1)

def letter_a():
    Letter.create()
    Letter.jump(-100,0,55)
    t.goto(0,200)
    t.setheading(-55)
    t.goto(100,0)
    Letter.jump(-50,70,0)
    t.forward(100)
    Letter.finish()

def letter_b():
    Letter.create()
    Letter.jump(-100,0,90)
    t.forward(200)
    t.setheading(0)
    t.forward(80)
    t.circle(-50,180)
    t.forward(80)
    t.setheading(0)
    t.forward(80)
    t.circle(-50,180)
    t.forward(80)
    Letter.finish()

def letter_c():
    Letter.create()
    Letter.jump(80,160,90)
    t.circle(50,90)
    t.forward(20)
    t.circle(80,90)
    t.forward(80)
    t.circle(80,90)
    t.forward(20)
    t.circle(50,90)
    Letter.finish()

def letter_d():
    Letter.create()
    Letter.jump(-80,200,-90)
    t.forward(200)
    Letter.jump(-80,200,0)
    t.forward(40)
    t.circle(-100,180)
    t.forward(40)
    Letter.finish()

def letter_e():
    Letter.create()
    Letter.jump(-80,200,-90)
    t.forward(200)
    Letter.jump(-80,200,0)
    t.forward(140)
    Letter.jump(-80,100,0)
    t.forward(120)
    Letter.jump(-80,0,0)
    t.forward(140)
    Letter.finish()

def letter_f():
    Letter.create()
    Letter.jump(-80,200,-90)
    t.forward(200)
    Letter.jump(-80,200,0)
    t.forward(140)
    Letter.jump(-80,100,0)
    t.forward(120)
    Letter.finish()

def letter_g():
    Letter.create()
    Letter.jump(80,160,90)
    t.circle(50,90)
    t.forward(20)
    t.circle(80,90)
    t.forward(80)
    t.circle(80,90)
    t.forward(20)
    t.circle(50,90)
    Letter.jump(40,30,0)
    t.forward(60)
    Letter.finish()

def letter_h():
    Letter.create()
    Letter.jump(-80,200,-90)
    t.forward(200)
    Letter.jump(80,200,-90)
    t.forward(200)
    Letter.jump(-80,110,0)
    t.forward(160)
    Letter.finish()

def letter_i():
    Letter.create()
    Letter.jump(0,200,-90)
    t.forward(200)
    Letter.finish()

def letter_j():
    Letter.create()
    Letter.jump(50,200,-90)
    t.forward(140)
    t.circle(-50,180)
    Letter.finish()

def letter_k():
    Letter.create()
    Letter.jump(-100,200,-90)
    t.forward(200)
    Letter.jump(-100,100,45)
    t.goto(30,200)
    Letter.jump(-100,100,-45)
    t.goto(30,0)
    Letter.finish()

def letter_l():
    Letter.create()
    Letter.jump(-100,200,-90)
    t.forward(200)
    t.setheading(0)
    t.forward(120)
    Letter.finish()

def letter_m():
    Letter.create()
    Letter.jump(-100,200,-90)
    t.forward(200)
    Letter.jump(-100,200,-60)
    t.goto(0,0)
    t.setheading(60)
    t.goto(100,200)
    t.setheading(-90)
    t.forward(200)
    Letter.finish()

def letter_n():
    Letter.create()
    Letter.jump(-100,200,-90)
    t.forward(200)
    Letter.jump(-100,200,-48)
    t.goto(50,0)
    t.setheading(90)
    t.forward(200)
    Letter.finish()

def letter_o():
    Letter.create()
    Letter.jump(0,200,180)
    t.circle(80,90)
    t.forward(40)
    t.circle(80,90)
    t.circle(80,90)
    t.forward(40)
    t.circle(80,90)
    Letter.finish()


### TBC ###

def letter_t():
    Letter.create()
    Letter.jump(0,0,90)
    t.forward(200)
    Letter.jump(-80,200,0)
    t.forward(160)
    Letter.finish()

    
