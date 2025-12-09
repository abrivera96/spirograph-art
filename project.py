import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Your Custome Spirograph")

artist = turtle.Turtle()
artist.speed(0)
artist.width(2)
artist.color("white")

for i in range(36):
    artist.circle(100)
    artist.left(10)
artist.hideturtle()
turtle.done()

