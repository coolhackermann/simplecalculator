from tkinter import *

root = Tk()
root.title('simple calc')

#entry
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

#e.insert(0, '')
#functions

def button_func():
    f_num = e.get()
    global fi_num
    global math
    math = 'addition'
    fi_num = int(f_num)
    e.delete(0, END)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_equal():
    secund_number = e.get()
    e.delete(0, END)

    if math == 'addition':
        e.insert(0, fi_num + int(secund_number))
        
    if math == 'subtraction':
        e.insert(0, fi_num - int(secund_number))

    if math == 'multiplycation':
        e.insert(0, fi_num * int(secund_number))
        
    if math == 'division':
        e.insert(0, fi_num / int(secund_number))





def button_sub():
    f_num = e.get()
    global fi_num
    global math
    math = 'subtraction'
    fi_num = int(f_num)
    e.delete(0, END)

def button_mul():
    f_num = e.get()
    global fi_num
    global math
    math = 'multiplycation'
    fi_num = int(f_num)
    e.delete(0, END)

def button_div():
    f_num = e.get()
    global fi_num
    global math
    math = 'division'
    fi_num = int(f_num)
    e.delete(0, END)

#buttons
button1 = Button(root, text='1', padx=40, pady=30, command=lambda: button_click(1))
button2 = Button(root, text='2', padx=40, pady=30, command=lambda: button_click(2))
button3 = Button(root, text='3', padx=40, pady=30, command=lambda: button_click(3))
button4 = Button(root, text='4', padx=40, pady=30, command=lambda: button_click(4))
button5 = Button(root, text='5', padx=40, pady=30, command=lambda: button_click(5))
button6 = Button(root, text='6', padx=40, pady=30, command=lambda: button_click(6))
button7 = Button(root, text='7', padx=40, pady=30, command=lambda: button_click(7))
button8 = Button(root, text='8', padx=40, pady=30, command=lambda: button_click(8))
button9 = Button(root, text='9', padx=40, pady=30, command=lambda: button_click(9))
button0 = Button(root, text='0', padx=40, pady=30, command=lambda: button_click(0))
buttonadd = Button(root, text='+', padx=38, pady=30, command=button_func)
buttonsub = Button(root, text='-', padx=40, pady=30, command=button_sub)
buttonmul = Button(root, text='x', padx=38, pady=30, command=button_mul)
buttondiv = Button(root, text='/', padx=41, pady=30, command=button_div)
sumofnum = Button(root, text='=', padx=39, pady=30, command=button_equal)
button_clear = Button(root, text='clear', padx=30, pady=40, command=button_clear)

#grids
button1.grid(row=1, column=1)
button2.grid(row=1, column=2)
button3.grid(row=1, column=3)
button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
button6.grid(row=2, column=3)
button7.grid(row=3, column=1)
button8.grid(row=3, column=2)
button9.grid(row=3, column=3)
button0.grid(row=4, column=2)
buttonadd.grid(row=4, column=1)
buttonsub.grid(row=4, column=3)
buttondiv.grid(row=5, column=1)
buttonmul.grid(row=5, column=3)
sumofnum.grid(row=5, column=2)
button_clear.grid(row=6, column=2)


root.mainloop()
