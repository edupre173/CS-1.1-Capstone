"""
COPYRIGHT JOEL MACHENS AND ETHAN DUPRE

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>. FOR LICENSE SEE LICENSE.MD """

# Import & Initialize a Turtle object as /t/, as well as importing pathlib for use in backgrounds.
import pathlib
import turtle

t = turtle.Turtle()
# Hides the turtle and sets its speed to 0, aka maximum, for the smoothest possible drawing experience
t.hideturtle()
t.speed(0)

# Give the Window a Title
turtle.title("Joel Machens & Ethan Dupre Present: Ourselves")

# Print the options for backgrounds
print("Backgrounds: Colour, Forest, School, Space, Matrix")
# Prompt the user, storing the user input in the variable \bkgd_input\ &
# lowercase string and remove whitespace
bkgd_input = input("Choose a background: ").lower().strip()

# Validate the variable \bkgd_input\ & apply background
if bkgd_input == "colour":
    colour = input("Choose a colour for the background: ")
    turtle.Screen().bgcolor(colour)
elif bkgd_input == "forest":
    turtle.Screen().bgpic(pathlib.Path("res/forest.png").resolve().__str__())
elif bkgd_input == "school":
    turtle.Screen().bgpic(pathlib.Path("res/school.png").resolve().__str__())
elif bkgd_input == "space":
    turtle.Screen().bgpic(pathlib.Path("res/space.png").resolve().__str__())
elif bkgd_input == "matrix":
    turtle.Screen().bgpic(pathlib.Path("res/matrix.png").resolve().__str__())
else:
    print("We're not sure what you meant, drawing default.")

# Print the options for styles
print("Body Styles: Cool, Tuxedo, Buff")
# Prompt the user for input on what to draw for the bodies, storing it in \body_style\ &
# lowercase string and remove whitespace
body_style = input("Choose a body style: ").lower().strip()
# Validate the variable \body_style\ : if it's valid we don't care, we'll deal with that when we're drawing
if body_style != "tuxedo" and body_style != "tux" and body_style != "cool" and body_style != "buff":
    print("We're not sure what you meant, going with cool.")
    body_style = "cool"
# Prompt the user for a colour and validate it
colour = input("Choose a colour for our clothes (hex code or named colour): ").lower().strip() or "cyan"
strcolours = ["red", "yellow", "blue", "black", "grey", "gray", "silver", "white", "maroon", "olive", "lime", "teal",
              "cyan", "navy", "purple"]
if not strcolours.__contains__(colour) or not colour.startswith("#"):
    colour = "cyan"

# Set starting position for drawing bodies
t.penup()
t.goto(-60, 0)
t.pendown()
t.setheading(0)

for person in range(2):
    # Draw a head
    t.fillcolor("#f1cea5")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.fillcolor(colour)

    # Get ready to draw a body
    t.penup()
    t.fd(50)
    t.rt(90)
    t.fd(40)
    t.pendown()

    # Draw a body
    t.seth(90)
    t.begin_fill()
    t.circle(50, 180)
    t.fd(80)
    t.circle(50, 180)
    t.fd(80)
    t.end_fill()

    t.seth(0)
    t.penup()
    t.left(90)
    t.forward(95)
    t.left(90)
    t.forward(70)
    t.pendown()

    if body_style == "buff":
        old_position = t.pos()
        old_colour = t.fillcolor()
        if colour == "black":
            t.pencolor("white")
        else:
            t.pencolor("black")

        # get the turtle in pos to draw the abs
        t.penup()
        t.right(180)
        t.forward(22)
        t.left(180)
        t.left(90)
        t.forward(120)
        t.right(90)
        t.pendown()
        t.left(90)
        t.forward(60)
        t.right(90)
        t.penup()



        t.penup()
        t.setpos(old_position)
        t.pendown()

    # Check if drawing a Tuxedo, if so, draw it
    if body_style == "tuxedo" or body_style == "tux":
        # Save current turtle position
        old_position = t.pos()
        old_colour = t.fillcolor()
        if colour == "black":
            t.fillcolor("white")
            t.pencolor("white")
        else:
            t.fillcolor("black")
            t.pencolor("black")

        t.penup()
        t.left(90)
        t.forward(50)
        t.pendown()
        t.right(180)

        # Left tie
        t.begin_fill()
        t.right(120)
        t.forward(20)
        t.right(120)
        t.forward(20)
        t.right(120)
        t.forward(20)
        t.end_fill()

        t.right(90)
        t.penup()
        t.forward(40)
        t.left(90)
        t.backward(20)
        t.pendown()

        # Right tie
        t.begin_fill()
        t.right(120)
        t.backward(20)
        t.right(120)
        t.backward(20)
        t.right(120)
        t.backward(20)
        t.end_fill()

        # Draw line down body
        t.right(90)
        t.penup()
        t.backward(20)
        t.right(90)
        t.backward(10)
        t.pendown()
        t.pensize(4)
        t.forward(150)
        t.pensize(1)

        # Restore turtle position
        t.left(270)
        t.penup()
        t.setpos(old_position)
        t.fillcolor(old_colour)
        t.pencolor(old_colour)
        t.pendown()

    # Draw the eyes
    t.pencolor("blue")
    t.circle(8)
    t.penup()
    t.right(180)
    t.forward(30)
    t.right(90)
    t.forward(10)
    t.pendown()
    t.circle(8)
    t.penup()
    t.forward(15)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.pendown()

    # Draw smile
    t.pencolor("white")
    t.fillcolor("white")
    t.begin_fill()
    t.circle(20, 180)
    t.left(90)
    t.forward(40)
    t.end_fill()
    t.penup()
    t.left(90)
    t.forward(200)
    t.pendown()
    t.pencolor("black")
    t.fillcolor(colour)

    # Get ready to draw again.
    t.seth(0)
    t.penup()
    t.goto(60, 0)
    t.pendown()

# Main Loop for Window -- Boilerplate
window = turtle.Screen()
window.mainloop()
