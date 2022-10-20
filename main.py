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
# lowercase string so that capitalization doesn't matter, as well as removing whitespace
bkgd_input = input("Choose a background: ").lower().strip(" ")

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

t.fillcolor("white")
t.begin_fill()
t.circle(50)
t.end_fill()

# Main Loop for Window -- Boilerplate
window = turtle.Screen()
window.mainloop()
