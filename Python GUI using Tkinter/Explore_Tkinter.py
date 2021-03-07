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
'''
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
'''
#============================================================================
#Creating frames
'''
win = Tk()
frame = Frame(win)
frame.pack()

frame2 = Frame(win)
frame2.pack(side = BOTTOM)

rb = Button(frame, text = 'Red', fg = 'red' )
rb.pack(side = LEFT)
bb = Button(frame, text = 'Blue', fg = 'blue' )
bb.pack(side = LEFT)
gb = Button(frame, text = 'Green', fg = 'green' )
gb.pack(side = LEFT)

gb = Button(frame2, text = 'Green', fg = 'green' )
gb.pack(side = BOTTOM)

win.mainloop()
'''
#============================================================================
'''
#Creating list

win = Tk()

lb = Listbox(win)
lb.insert(1, 'Python')
lb.insert(2, 'Js')
lb.insert(3, 'Flutter')
lb.insert(4, 'React')
lb.insert(5, 'Ruby')
lb.pack()
win.mainloop()
'''
#============================================================================
#Top Level Window
'''
win = Tk()

win.title("First")
top = Toplevel()
win.title("Second")

win.mainloop()
'''
#============================================================================
#Message Box
'''
from tkinter import messagebox
win = Tk()

def hello():
    messagebox.showinfo('From computer','Welcome!!')

b = Button(win, text = 'Click Me', fg = 'green', command = hello )
b.pack()

win.mainloop()
'''
#============================================================================
# Menu button/Bar
'''
win = Tk()
mb =Menubutton(win, text = 'File')
mb.grid()
mb.menu = Menu(mb)
mb['menu'] = mb.menu

x1 = IntVar()
x2 = IntVar()

mb.menu.add_checkbutton(label = 'open', variable = x1)
mb.menu.add_checkbutton(label = 'close', variable = x2)
mb.pack()
win.mainloop()
'''
'''
win = Tk()

def nothing():
    file = Toplevel(win)
    button = Button(file, text = 'do nothing')
    button.pack()

menubar = Menu(win)

filemenu = Menu(menubar)
filemenu.add_command(label= 'New Window', command = nothing)
filemenu.add_command(label= 'New File', command = nothing)
filemenu.add_command(label= 'New Folder', command = nothing)
filemenu.add_command(label= 'Open File', command = nothing)
filemenu.add_separator()
filemenu.add_command(label= 'Save', command = nothing)
filemenu.add_command(label= 'Save As', command = nothing)
filemenu.add_command(label= 'Save All', command = nothing)
filemenu.add_separator()
filemenu.add_command(label= 'Close Tab', command = nothing)
filemenu.add_command(label= 'Close Window', command = nothing)
filemenu.add_separator()
filemenu.add_command(label= 'Exit', command = win.quit)
menubar.add_cascade(label = 'File', menu = filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label= 'Undo', command = nothing)
editmenu.add_command(label= 'Redo', command = nothing)
editmenu.add_separator()
editmenu.add_command(label= 'Cut', command = nothing)
editmenu.add_command(label= 'Copy', command = nothing)
editmenu.add_command(label= 'Paste', command = nothing)
editmenu.add_separator()
editmenu.add_command(label= 'Line', command = nothing)
editmenu.add_command(label= 'Column', command = nothing)
editmenu.add_command(label= 'Text', command = nothing)
editmenu.add_separator()
editmenu.add_command(label= 'Exit', command = win.quit)
menubar.add_cascade(label = 'Edit', menu = editmenu)

win.config(menu=menubar)
win.mainloop()
'''
#============================================================================
# Menu Scale, Spinbox, Scroll bar
'''
win = Tk()

#s= Scale(win)
#s.pack()

#sb= Spinbox(win, from_ = 1, to = 10)
#sb.pack()


scrollbar = Scrollbar(win)

scrollbar.pack(side = RIGHT, fill = Y)

list = Listbox(win,yscrollcommand = scrollbar.set)

for line in range(100):
    list.insert(END, 'This is line no is '+ str(line))

list.pack(side= LEFT, fill = BOTH)
win.mainloop()
'''
#============================================================================
# Paned Window
'''
pw = PanedWindow()
pw.pack(fill=BOTH,expand = 1)

left = Entry(pw, bd =5)
pw.add(left)

pw2 = PanedWindow(pw, orient = VERTICAL)
pw.add(pw2)

top= Scale(pw2, orient = HORIZONTAL )
pw2.add(top)

button = Button(pw2, text = 'OK')
pw2.add(button)

mainloop()
'''

#============================================================================
# Paned Window
