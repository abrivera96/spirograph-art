import turtle
import random


BG_COLOR = "black"
PEN_WIDTH = 2
SPEED = 0

def get_user_choice():
    """
    Asks the user for mode (manual/random).
    Returns a tuple: (radius, density, color_choice)
    """
    print("--- Welcome to the Spirograph Maker ---")
    mode = input("Do you want 'manual' or 'random' mode? (m/r): ").lower()

    if mode == "r" or mode == "random":
        print("Randomizing your art...")
        radius = random.randint(50, 150)
        density = random.randint(30, 100)
        color_choice = random.choice(["red", "green", "blue", "purple", "orange", "cyan", "white", "yellow"])
        print(f"I picked: Radius={radius}, Density={density}, Color={color_choice}")
        return radius, density, color_choice
    else:
        print("Please enter your settings:")
        radius = int(input("Enter radius (e.g., 100): "))
        density = int(input("Enter density (e.g., 60): "))
        color_choice = input("Choose color (red, green, blue, purple, orange, cyan): ").lower()
        return radius, density, color_choice

def setup_artist():
    """
    Creates the screen and turtle. 
    Returns the turtle object (artist).
    """
    print("Initializing Turtle...")
    screen = turtle.Screen()
    screen.bgcolor(BG_COLOR)
    screen.title("Python Spirograph")
    turtle.colormode(255) 
    
    artist = turtle.Turtle()
    artist.speed(SPEED)
    artist.width(PEN_WIDTH)
    return artist

def set_pen_color(artist, color_choice, shade):
    """
    Sets the turtle's color based on the choice and the current shade intensity.
    """
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
    elif color_choice == "yellow":
        artist.color(shade, shade, 0)
    elif color_choice == "white":
        artist.color(shade, shade, shade)
    else:
        artist.color(shade, shade, shade)

def draw_spirograph(artist, radius, density, color_choice):
    """
    Takes the artist and the data, and performs the drawing.
    """
    angle = 360 / density
    
    for i in range(density):
        shade = int((i / density) * 255)
        set_pen_color(artist, color_choice, shade)
        artist.circle(radius)
        artist.left(angle)

def main():
    radius, density, color_choice = get_user_choice()
    artist = setup_artist()
    draw_spirograph(artist, radius, density, color_choice)
    artist.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()