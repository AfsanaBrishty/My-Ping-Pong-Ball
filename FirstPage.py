from tkinter import *
from PIL import ImageTk,Image
from tkinter.ttk import *
import os

root=Tk()

#os.environ["SDL_VIDEO_CENTERED"] = "1"


root.title("My PingPong Ball")
root.resizable(0,0)
canvas=Canvas(root,width=900, height=600)
image=ImageTk.PhotoImage(Image.open("E:\\AAllAboutStudy\\MY3.2\\MyPingPongBall\\bg5.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()

Title = Label(root, text = "My PingPong Ball",font=("Comic Sans MS",50,"normal")).place(x = 195,y = 200)
root.wm_attributes("-transparentcolor",'grey')

pgbar=Progressbar(
    root,
    length=900,
    orient=HORIZONTAL,
    mode='determinate',

)
pgbar.start(100)
pgbar.pack()


root.mainloop()
