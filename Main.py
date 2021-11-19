from tkinter import *
from random import randint

frameWidth = 1366
frameHeight = 720

class Ball:
    def __init__(self, canvas, x, y, width, height, deltax, deltay, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.canvas = canvas
        self.deltax = deltax
        self.deltay = deltay
        self.ball = canvas.create_oval(self.x, self.y, x + width, y + height, fill=color, outline="black")

    def move_ball(self):
        if self.x >= frameWidth or self.x <= 0:
            self.deltax = -self.deltax
            if self.deltax < 0 : self.deltax -= 1
            if self.deltax > 0 : self.deltax += 1

            # Замедление по абциссе после удара о стенку
            #if(self.deltax > 0): self.deltax -= 1
            #if(self.deltax < 0): self.deltax += 1

        if self.y >= frameHeight or self.y <= 0:
            self.deltay = -self.deltay
            if self.deltay < 0 : self.deltay -= 1
            if self.deltay > 0 : self.deltay += 1

            # Замедление по ординате после удара о стенку
            #if (self.deltay > 0): self.deltay -= 1
            #if (self.deltay < 0): self.deltay += 1

        self.canvas.move(self.ball, self.deltax, self.deltay)
        self.x += self.deltax
        self.y += self.deltay

        """
        # Замедление на всем пути
        if (self.deltax > 0): self.deltax -= 0.01
        if (self.deltax < 0): self.deltax += 0.01
        if (self.deltay > 0): self.deltay -= 0.01
        if (self.deltay < 0): self.deltay += 0.01
        """
        self.canvas.after(50, self.move_ball)

root = Tk()
root.title("Moleculs")
root.wm_state('zoomed')
root.overrideredirect(1)
root.resizable(False,False)
root.update()
canvas = Canvas(root, width=root.winfo_width(), height=root.winfo_height())
canvas.configure(background="black")
canvas.pack()

for i in range(250):
    deltax1 = randint(-100, 100)
    deltay1 = randint(-100, 100)
    size1 = 5  # randint(5,20)
    x1 = randint(200, 400)
    y1 = randint(200, 400)
    a = Ball(canvas, x1, y1, size1, size1, deltax1, deltay1, "white")
    a.move_ball()

root.mainloop()
