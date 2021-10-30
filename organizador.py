from tkinter import *
import shutil
import os
from tkinter.filedialog import askopenfilename

#----------------------------------------------------------#

root = Tk()
root.title("Organizador de Ficheiros")
root.geometry('700x300')

def selecionador(): #Dá o nome do ficheiro original
    filename = askopenfilename(initialdir="/", filetypes = (("All files", "*.*"), ("jpeg files", "*.JPEG")))
    Ficheiro = Label(root, text=filename, bg="white")
    Ficheiro.grid(row=2, column=2)
    return filename


Lbl_ficheiro = Label(root, text="Ficheiro a mover:", font = "Helvetica 12 bold")
Lbl_ficheiro.grid(row=2, column=1)


def destino():  #Dá o caminho da pasta
    destino = os.path.dirname(askopenfilename(initialdir="/", filetypes=(("All files", "*.*"),("jpeg files", "*.JPEG"))))
    Destino_do_ficheiro=Label(root, text=destino, bg="white")
    Destino_do_ficheiro.grid(row=4, column=2)
    return destino


Lbl_destino=Label(root, text="Destino:", font="Helvetica 12 bold")
Lbl_destino.grid(row=4, column=1)


def mover():
    Origem = selecionador()
    Destino = destino() + "/" +  os.path.basename(Origem)
    shutil.move(Origem, Destino)
    Done = Label(root, text="DONE!", font= "Helvetica 20 bold")
    Done.grid(row=8, column=2)
    return Done


FIM = Button(root, text="Mover Ficheiro", height=2, width=15, command=mover)
FIM.grid(row=8, column=1)
    

root.mainloop()

#Acabado a 24/9/21