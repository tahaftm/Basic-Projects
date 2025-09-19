from tkinter import *

def press_button(num):
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():
    try:
        global equation_text
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Mathematical error.")
    except SyntaxError:
        equation_label.set("Sorry!")
def clear():
    global equation_text
    equation_text = ""
    equation_label.set("")
window = Tk()

window.title("Calculator")
# window.geometry("500x500")

icon = PhotoImage(file="C:\\Users\\USER\\Desktop\\microsoft\\module 1\\basic projects\\calculator project\\calculator-icon-1-removebg-preview.png")
window.iconphoto(True, icon)

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font = ('consolas', 20), bg = 'white', width=19, height=2)
label.pack()

frame = Frame(window)

frame.pack()

button1 = Button(frame, text = 1,
                 command= lambda: press_button(1),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
button1.grid(row = 0,column = 0, sticky='nsew')
button2 = Button(frame, text = 2, 
                 height=4,
                 width=9,
                 command=lambda: press_button(2),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = "#ffc800",
                 activeforeground = '#ffc800',
                 activebackground = 'black')
button2.grid(row = 0,column = 1)
button3 = Button(frame, text = 3, 
                 height=4,
                 width=9,
                 command=lambda: press_button(3),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
button3.grid(row = 0,column = 3)
plus = Button(frame, text = '+', 
                 height=4,
                 width=9,
                 command=lambda: press_button('+'),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
plus.grid(row = 0,column = 4)

button4 = Button(frame, text = 4, 
                 height=4,
                 width=9,
                 command=lambda: press_button(4),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
button4.grid(row = 1,column = 0)
button5 = Button(frame, text = 5, 
                 height=4,
                 width=9,
                 command=lambda: press_button(5),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
button5.grid(row = 1,column = 1)
button6 = Button(frame, text = 6, 
                 height=4,
                 width=9,
                 command=lambda: press_button(6),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
button6.grid(row = 1,column = 3)
minus = Button(frame, text = '-', 
                 height=4,
                 width=9,
                 command=lambda: press_button('-'),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
minus.grid(row = 1,column = 4)



button7 = Button(frame, text = 7, 
                 height=4,
                 width=9,
                 command=lambda: press_button(7),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
button7.grid(row = 2,column = 0)
button8 = Button(frame, text = 8, 
                 height=4,
                 width=9,
                 command=lambda: press_button(8),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
button8.grid(row = 2,column = 1)
button9 = Button(frame, text = 9, 
                 height=4,
                 width=9,
                 command=lambda: press_button(9),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
button9.grid(row = 2,column = 3)
divide = Button(frame, text = '/', 
                 height=4,
                 width=9,
                 command=lambda: press_button('/'),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = "#ffc800",
                 activeforeground = '#ffc800',
                 activebackground = 'black')
divide.grid(row = 2,column = 4)


zero = Button(frame, text = 0, 
                 height=4,
                 width=9,
                 command=lambda: press_button(0),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
zero.grid(row = 3,column = 0)
point = Button(frame, text = ".", 
                 height=4,
                 width=9,
                 command=lambda: press_button('.'),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
point.grid(row = 3,column = 1)
equal = Button(frame, text = "=", 
                 height=4,
                 width=9,
                 command=equals,
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
equal.grid(row = 3,column = 3)
multiply = Button(frame, text = 'x', 
                 height=4,
                 width=9,
                 command=lambda: press_button('*'),
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
multiply.grid(row = 3,column = 4)


clr = Button(frame, text = 'clear', 
                 height=4,
                 width=40,
                 command= clear,
                 font = ('consolas', 10, "bold"),
                 bg = 'black',
                 fg = '#ffc800',
                 activeforeground = '#ffc800',
                 activebackground = 'black')
clr.grid(row = 4,column = 0, columnspan=5)


window.mainloop()









                                                































