import turtle
import random

bg_color = "black"
pen_width = 1
speed = 0

def main():
    print("---Welcome to the Spirograph Maker!---")

    mode = input("Do you want 'manual' or 'random' mode? (m/r): ").lower()
    radius = 0
    density = 0
    color_choice = ""

    if mode == "r" or mode == "random":
        print("Randomizing your art...")
        radius = random.randint(50, 150)
        density = random.randint(30, 100)
        color_choice = random.choice(["red", "green", "blue", "purple", "orange", "cyan"])
        print(f"I picked: Radius={radius}, Density={density}, Color={color_choice}")
        
    else:
        # Manual Mode (Default)
        print("Please enter your settings:")
        radius = int(input("Enter radius (e.g., 100): "))
        density = int(input("Enter density (e.g., 60): "))
        color_choice = input("Choose color (red, green, blue, purple, orange, cyan): ").lower()

    print("Initailizing Turtle...")

    screen = turtle.Screen()
    screen.bgcolor(bg_color)
    screen.title("Your Custom Spirograph!")
    turtle.colormode(255)
    artist = turtle.Turtle()
    artist.speed(speed)
    artist.width(pen_width)
    
    angle = 360 / density
    
    print(f"Drawing with Radius: {radius} and Density: {density} ... ")

    for i in range(density):
        shade = int((i / density) * 255)
        if color_choice == "red":
            artist.color(shade, 0, 0)
        elif color_choice == "green":
            artist.color(0, shade, 0)
        elif color_choice == "blue":
            artist.color(0, 0, shade)
        elif color_choice == "purple":
            artist.color(shade, 0, shade)
        elif color_choice == "orange":
            artist.color(shade, shade // 2, 0) 
        elif color_choice == "cyan":
            artist.color(0, shade, shade)
        else:
            # White/Grey if unknown
            artist.color(shade, shade, shade)
        artist.circle(radius)
        artist.left(angle)
    artist.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()