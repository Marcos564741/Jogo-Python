import tkinter
from tkinter import *

janela = Tk()
janela.title("Label e botão!")
janela.geometry("200x200")

label = Label(janela, text="Primeiro Label", font = ("Arial Bold", 20), bg="green", fg="white")
label.grid(column=0, row=0)

bot = Button(janela, text="Cliqua aqui!")
bot.grid(column=0, row=1)
janela.mainloop()