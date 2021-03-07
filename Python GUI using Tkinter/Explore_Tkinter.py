import tkinter
from tkinter import *
from functools import partial

#Creating Window
'''
win  = Tk()
win.geometry("500x500")
win.mainloop()
'''
#======================================================================
'''
#Creating buttons
win  = Tk()
def pr():
    print('Hi')

win.geometry("500x500")
#declaring button
b = Button(win, text ='Button',command = pr, padx = 10, pady = 5, activeforeground='red', activebackground='green', bg = 'grey'  )
b1 = Button(win, text ='Button1')


#Showing button using pack method
#b.pack()
#b1.pack()

#Showing button using grid method
#b.grid(row=1,column=1)
#b1.grid(row=2,column=1)

#Showing button using place method
b.place(x=100,y=200)
b1.place(x=250,y=200)

win.mainloop()
'''
#======================================================================
'''
#Creating Canvas
win  = Tk()
#win.geometry("500x500")

c= Canvas(win,height=250,width=250, bg = 'blue')

cord = 10,50,240,210
arc = c.create_arc(cord, start = 0, extent = 150, fill = 'red')
arc = c.create_line(cord, fill = 'white')

oval = c.create_oval(10,10,40,40, fill = 'green')

polygon = c.create_polygon(10,10,40,40,60,60,190,190, fill = 'yellow')

c.pack()

win.mainloop()
'''
#======================================================================
'''
#Creating Check point and radio buttons

win  = Tk()
c1 = IntVar()
c2 = IntVar()
cb = Checkbutton(win, text = 'Music', offvalue = 0, onvalue = 1, height = 5, width = 10, variable = c1)
cb1 = Checkbutton(win, text = 'Video', offvalue = 0, onvalue = 1, height = 5, width = 10,variable = c2)
cb.pack()
cb1.pack()

var = IntVar()
r1 = Radiobutton(win, text='Option1', variable=var, value=1)
r2 = Radiobutton(win, text='Option2', variable=var, value=2)
r3 = Radiobutton(win, text='Option3', variable=var, value=3)
r1.pack()
r2.pack()
r3.pack()

win.mainloop()
'''
#======================================================================
#Creating text and lable
'''
win  = Tk()

l= Label(win,text = 'Username')
l.pack()
e = Entry(win)
e.pack()
t = Text(win)
t.insert(INSERT,'hello')
t.pack()

win.mainloop()
'''
#============================================================================
#Calculate sum

win  = Tk()

def sum(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum = int(n1) + int(n2)
    label.config(text='sum is : %d' %sum)
    return

l1= Label(win,text = 'First No. : ')
l1.grid(row=1, column=0)
l2= Label(win,text = 'Second No. :')
l2.grid(row=2, column=0)
label =Label(win)
label.grid(row=6, column=2)

x1 = StringVar()
x2 = StringVar()

e1 = Entry(win, textvariable = x1)
e1.grid(row=1, column=2)
e2 = Entry(win, textvariable = x2)
e2.grid(row = 2, column = 2)

sum = partial(sum, label, x1, x2)

button = Button(win, text ='Calculate', command = sum, bg = 'grey'  )
button.grid(row=3,column=0)
win.mainloop()
