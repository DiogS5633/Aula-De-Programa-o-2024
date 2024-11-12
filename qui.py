#tem que fazer visul studio code
from tkinter import Tk, Label, Entry, Button, messagebox

def show_nome( ):
    messagebox.showinfo(
        title='Seja Bem Vindo!',
        message=f'Ola {txt_nome.get( )}'
    )
janela = Tk()
janela.title('Mnha Janela')
janela.config(padx=10, pady=10)

lbl_nome = Label(text='Nome: ')
lbl_nome.grid(row=0, column=0)

txt_nome = Entry(width=40)
txt_nome.grid(row=0, column=1,columnspan=2, sticky='W')

btn_ok = Button(text='OK' , width=20, command=show_nome)
btn_ok.grid(row=1, column=0, columnspan=3)

janela.mainloop()