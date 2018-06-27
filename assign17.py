from tkinter import *
root =Tk()
frame=Frame(root,bg='red')
frame.pack()
rb=Button(frame,text='hello world',fg='red')
rb.pack(side=LEFT)
bb=Button(frame,text='exit',fg='brown',command=quit)
bb.pack(side=LEFT)
root.mainloop()