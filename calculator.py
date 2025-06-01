from tkinter import *

# Create the main window
root = Tk()
root.title("Simple Calculator")

# Global variable to store the expression
expression = ""

# Function to update the expression
def update_expression(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the expression
def evaluate():
    global expression
    try:
        result = eval(expression)
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")
        expression = ""

# Function to clear the expression
def clear():
    global expression
    expression = ""
    equation.set("")

# Create a entry field for displaying the expression
equation = StringVar()
expression_field = Entry(root, textvariable=equation, width=20)
expression_field.grid(row=0, column=0, columnspan=4)

# Create number buttons
button_1 = Button(root, text="1", command=lambda: update_expression(1))
button_1.grid(row=1, column=0)
button_2 = Button(root, text="2", command=lambda: update_expression(2))
button_2.grid(row=1, column=1)
button_3 = Button(root, text="3", command=lambda: update_expression(3))
button_3.grid(row=1, column=2)

button_4 = Button(root, text="4", command=lambda: update_expression(4))
button_4.grid(row=2, column=0)
button_5 = Button(root, text="5", command=lambda: update_expression(5))
button_5.grid(row=2, column=1)
button_6 = Button(root, text="6", command=lambda: update_expression(6))
button_6.grid(row=2, column=2)

button_7 = Button(root, text="7", command=lambda: update_expression(7))
button_7.grid(row=3, column=0)
button_8 = Button(root, text="8", command=lambda: update_expression(8))
button_8.grid(row=3, column=1)
button_9 = Button(root, text="9", command=lambda: update_expression(9))
button_9.grid(row=3, column=2)

button_0 = Button(root, text="0", command=lambda: update_expression(0))
button_0.grid(row=4, column=0)

# Create operator buttons
button_add = Button(root, text="+", command=lambda: update_expression("+"))
button_add.grid(row=1, column=3)
button_subtract = Button(root, text="-", command=lambda: update_expression("-"))
button_subtract.grid(row=2, column=3)
button_multiply = Button(root, text="", command=lambda: update_expression(""))
button_multiply.grid(row=3, column=3)
button_divide = Button(root, text="/", command=lambda: update_expression("/"))
button_divide.grid(row=4, column=3)

button_equal = Button(root, text="=", command=evaluate)
button_equal.grid(row=4, column=2)

button_clear = Button(root, text="C", command=clear)
button_clear.grid(row=4, column=1)

root.mainloop()
