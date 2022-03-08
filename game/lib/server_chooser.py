from logging import root
from tkinter import *

root = Tk()
root.title("Vitrix")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 375
window_height = 150

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


is_ready = False

def submit():
    with open("data.txt", "w") as file:
        file.writelines([E1.get(), "\n",  E2.get(), "\n",  E3.get()])
    root.destroy()

L1 = Label(root, text="Username:")
L1.place(anchor = CENTER, relx = .10, rely = .1)
E1 = Entry(root, bd = 5)
E1.place(anchor = CENTER, relx = .5, rely = .1)

L2 = Label(root, text="Server:")
L2.place(anchor = CENTER, relx = .10, rely = .3)
E2 = Entry(root, bd = 5)
E2.place(anchor = CENTER, relx = .5, rely = .3)

L3 = Label(root, text="Port:")
L3.place(anchor = CENTER, relx = .10, rely = .5)
E3 = Entry(root, bd = 5)
E3.place(anchor = CENTER, relx = .5, rely = .5)

submit = Button(root, text="Join", width=10, command=submit)
submit.place(anchor = CENTER, relx = .5, rely = .8)

root.mainloop()
