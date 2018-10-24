#! python3

from tkinter import *

root = Tk()

top_frame = Frame(root)
top_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text="Click Me!", fg="red")
button2 = Button(bottom_frame, text="Click Me 2!", fg="blue")
button3 = Button(bottom_frame, text="Click Me 3!", fg="green")
button4 = Button(bottom_frame, text="Click Me 4!", fg="yellow")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)


root.mainloop()