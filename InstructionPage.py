from tkinter import *
from PIL import ImageTk,Image
from tkinter.ttk import *
import os

root=Tk()

#os.environ["SDL_VIDEO_CENTERED"] = "1"
root.title("Instruction Page")
root.resizable(0,0)
canvas=Canvas(root,width=900, height=600)
image=ImageTk.PhotoImage(Image.open("E:\\AAllAboutStudy\\MY3.2\\MyPingPongBall\\inspagebg.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
root.mainloop()
