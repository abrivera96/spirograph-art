import turtle

bg_color = "black"
pen_color = "white"
pen_width = 1
speed = 0

def main():
    screen = turtle.Screen()
    screen.bgcolor(bg_color)
    screen.title("Your Custom Spirograph!")

    artist = turtle.Turtle()
    artist.speed(speed)
    artist.width(pen_width)
    artist.color(pen_color)

    for i in range(36):
        artist.circle(100)
        artist.left(10)
    artist.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()