import turtle

bg_color = "black"
pen_color = "white"
pen_width = 1
speed = 0

def main():

    print("--- Build Your Own Spirograph ---")
    radius = int(input("Enter the radius size you want: "))
    density = int(input("Enter the number of circles you want: "))
    angle = 360 / density

    screen = turtle.Screen()
    screen.bgcolor(bg_color)
    screen.title("Your Custom Spirograph!")

    artist = turtle.Turtle()
    artist.speed(speed)
    artist.width(pen_width)
    artist.color(pen_color)

    print(f"Drawing with Radius: {radius} and Density: {density} ... ")

    for i in range(density):
        artist.circle(radius)
        artist.left(angle)
    artist.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()