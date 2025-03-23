from tkinter import *
import random

window = Tk()
window.title("I'm geting bored")
window.geometry('512x512+750+250')

word = ["Don't Press me","I said DON'T","CAN'T YOU JUST STOP???","BRUH","PLEASE LEAVE ME ALONE"]
x = 5
y = 15
e=0
def click():
  random_int = random.randint(0, 450)
  x = (random_int)
  z = random.randrange(0,5)
  random_int = random.randint(0, 450)
  y = (random_int)
  button.config(text=(word[z]))
  button.place(x=x, y=y)
  for i in range():
    e = i+1
    print(e)
    return e
  if e >=1:
    buttone.place(x=15, y=20)

def exit():
    window.destroy()

buttone=Button(text="LAST TIME STOPPP!!!",command=exit)


button = Button(text=(word[0]), command=click)

button.pack(padx=20, pady=15)

window.mainloop()