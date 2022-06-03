# import everything from tkinter module
from tkinter import *
 
# declare the expression global variable
expression = ""
 
 
# Function to update expression in the input
def press(input):
    global expression
    # adding the value from the button to the expression
    expression = expression + str(input)
    # updating the expression
    equation.set(expression)
 
 

def equal():
    try:
 
        global expression
 
        # eval function turns the string input into an expression and calculates the result
        result = str(eval(expression))
        equation.set(result)
 
        # resetting the expression variable
        expression = ""
 
    # if the previous lines fail(empty input) the output will just be changed to "error"
    except:
 
        equation.set(" ERROR ")
        expression = ""
 
 
# Function to clear the contents of the input
def clear():
    global expression
    expression = ""
    equation.set("")
 
 
# Driver code
if __name__ == "__main__":
    # creating a window and configuring it
    gui = Tk()
    gui.configure(background="light gray")
    gui.title("Calcutron 9000")
    gui.geometry("300x200")
    equation = StringVar()
 
    #showing the expression
    expression_field = Text(gui, textvariable=equation)
 
    # using a grid to organize the buttons
    expression_field.grid(columnspan=4, ipadx=70,ipady=10)
 
    # creating buttons and assigning functions to them
    button1 = Button(gui, text=' 1 ', fg='black', bg='gray',
                    command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='gray',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='gray',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='gray',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='gray',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='gray',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='gray',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='gray',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='gray',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='gray',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='black', bg='gray',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='gray',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' x ', fg='black', bg='gray',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='gray',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='black', bg='gray',
                command=equal, height=1, width=7)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='black', bg='gray',
                command=clear, height=1, width=7)
    clear.grid(row=6, column=0)
 
    Decimal= Button(gui, text='.', fg='black', bg='gray',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=5, column=1)


    # starting the GUI
    gui.mainloop()
