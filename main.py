"""
COPYRIGHT JOEL MACHENS AND ETHAN DUPRE

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not,
see <https://www.gnu.org/licenses/>. FOR LICENSE SEE LICENSE.MD """

# Import & Initialize a Turtle object as /t/
import turtle
t = turtle.Turtle()
# Hides the turtle and sets its speed to 0, aka maximum, for the smoothest possible drawing experience
t.hideturtle()
t.speed(0)

# Give the Window a Title
turtle.title("Joel Machens & Ethan Dupre Present: Ourselves")

# Print the options for backgrounds and then print the prompt, storing the user input in the variable \bkgd_input\
print("Backgrounds: Colour, Forest, School, Space, Matrix")
bkgd_input = input("Choose a background: ").lower() # lowercase string so that capitalization doesn't matter

# Validate the variable \bkgd_input\
if bkgd_input == "colour":
    colour = input("")

t.circle(50)

# Main Loop for Window -- Boilerplate
window = turtle.Screen()
window.mainloop()
