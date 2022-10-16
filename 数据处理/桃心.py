import turtle
import time


def LittleHeart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)


isLove = input('你会一直爱她吗？（Y or N）\n')

run = 1
while (run):
    if isLove == "Y":
        me = ""
        love = ""
        if love == '':
            love = ' 小欧同学 I love you'
        turtle.setup(width=900, height=500)
        turtle.color('red', 'red')
        turtle.pensize(3)
        turtle.speed(50)
        turtle.up()
        turtle.hideturtle()
        turtle.goto(0, -180)
        turtle.showturtle()
        turtle.down()
        turtle.speed(5)
        turtle.begin_fill()
        turtle.left(140)
        turtle.forward(224)
        LittleHeart()
        turtle.left(120)
        LittleHeart()
        turtle.forward(224)
        turtle.end_fill()
        turtle.pensize(5)
        turtle.up()
        turtle.hideturtle()
        turtle.goto(0, 0)
        turtle.showturtle()
        turtle.color('#CD5C5C', 'blue')
        turtle.write(love, font=('gungsuh', 30,), align="center")
        turtle.up()
        turtle.hideturtle()
        if me != '':
            turtle.color('yellow', 'red')
            time.sleep(2)
        turtle.goto(180, -180)
        turtle.showturtle()
        turtle.write(me, font=(20,), align="center", move=True)
        window = turtle.Screen()
        window.exitonclick()
        run = 0


    else:
        print("活该单身一辈子")
        print("！！！！！！！！！再给你一次机会！！！！！！！！")
        isLove = input('你会一直爱她吗？（Y or N）\n')
        continue
