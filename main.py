from tkinter import *
import bank as bk

janela = Tk()
lb = Label(janela, text="Bem-Vindo ao RafaBank!!")
lb.place(x=500, y=0)
janela.title("RafaBank")
janela.geometry("1080x720+50+50")
janela["bg"] = "light green"
janela.mainloop()