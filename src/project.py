from PIL import ImageGrab
from tkinter import messagebox
import turtle
import random
import math

bg_color = "black"
pen_width = 2
speed = 0


def get_user_choice(screen):

    mode = screen.textinput("Mode Selection", "Mode (manual/random)? (m/r):")
    
    if not mode: 
        mode = "r" 
    
    mode = mode.lower()

    if mode == "r" or mode == "random":
        radius = random.randint(80, 150)
        density = random.randint(60, 120)
        color_choice = random.choice(["red", "green", "blue", "yellow", 
                                      "cyan", "magenta", "white", "orange"])
        shape_type = random.choice(["circle", "square", "triangle"])
        void = random.randint(20, 100)
        return radius, density, color_choice, shape_type, void
        
    else:
        radius = int(screen.numinput("Radius", "Enter Radius (50-200):", default=100, minval=50, maxval=200))
        density = int(screen.numinput("Density", "Enter Density (20-100):", default=60, minval=20, maxval=100))
        
        color_choice = screen.textinput("Color", "Enter Color (red, blue, cyan, etc.):")
        if not color_choice: color_choice = "cyan"
        
        shape_type = screen.textinput("Shape", "Enter Shape (circle, square, triangle):").lower()
        if not shape_type: shape_type = "circle"

        void = int(screen.numinput("Gap", "Center Gap distance:", default=40, minval=0, maxval=150))
        
        return radius, density, color_choice, shape_type, void 

def setup_artist():
    artist = turtle.Turtle()
    artist.speed(speed)
    artist.width(pen_width)
    return artist

def draw_one_shape(artist, shape_type, size):
    if shape_type == "circle":
        artist.circle(size)
    elif shape_type == "square":
        for _ in range(4):
            artist.forward(size)
            artist.left(90)
    elif shape_type == "triangle":
        for _ in range(3):
            artist.forward(size)
            artist.left(120)

def draw_spirograph(artist, base_radius, density, color_choice, shape_type, void):
    artist.color(color_choice)
    angle = 360 / density
    
    for i in range(density):
        artist.penup()
        artist.forward(void)
        artist.pendown()
        draw_one_shape(artist, shape_type, base_radius)
        
        artist.penup()
        artist.backward(void)
        artist.pendown()
        artist.left(angle)

def save_as_png():
    filename = turtle.textinput("Save Art", "Enter file name:")
    if filename:
        canvas = turtle.getcanvas()
        canvas = turtle.getcanvas()
        x = canvas.winfo_rootx()
        y = canvas.winfo_rooty()
        w = canvas.winfo_width()
        h = canvas.winfo_height()

        box = (x, y, x + w, y+ h)
        image = ImageGrab.grab(bbox=box)
        save_path = filename + ".png"
        image.save(save_path)
        
        messagebox.showinfo("Success", f"Saved {save_path} successfully!")

def main():
    screen = turtle.Screen()
    screen.bgcolor(bg_color)
    screen.title("Spirograph Maker")
    radius, density, color_choice, shape_type, void = get_user_choice(screen)
    artist = setup_artist()
    draw_spirograph(artist, radius, density, color_choice, shape_type, void)
    artist.hideturtle()
    screen.listen()
    screen.onkey(save_as_png, "s")
    screen.onkey(save_as_png, "S")

    screen.exitonclick()

if __name__ == "__main__":
    main()