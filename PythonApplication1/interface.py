from tkinter import filedialog
import tkinter
from tkinter import *
from PIL import ImageTk, Image
import os


# Criando janela principal
wd = tkinter.Tk()
wd.title("Sistema de Processamento Veicular")
wd.geometry("650x400")
#wd.maxsize(650, 400)
wd.minsize(650, 400)



# funções
def btnImg_onclick():
	img_path = (filedialog.askopenfilename())
	img = Image.open(img_path)
	img = img.resize((300, 350), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	lb_img = tkinter.Label(wd, image=img, height=300, width=350)
	lb_img.image = img
	lb_img.place(x=5,y=20)


# Defindo Componentes

# row 0
nome_img = tkinter.Label(wd, text="IMG")
nome_placa = tkinter.Label(wd, text="Nº Placa: ")
lb_placa = tkinter.Label(wd, text="placa aqui!")

# row 1

nome_status = tkinter.Label(wd, text="Status do Veiculo: ")
lb_status = tkinter.Label(wd, text="status aqui!")

# row 3
bt_img = tkinter.Button(wd, text="Imagem", command=btnImg_onclick)
bt_proc = tkinter.Button(wd, text="Processar")
bt_busca = tkinter.Button(wd, text="Buscar")

# Aplicando Layout
nome_img.place(x=5,y=0)
nome_placa.place(x=400, y=20)
lb_placa.place(x=450,y=20)
#lb_img.place(x=5,y=20)
nome_status.place(x=400, y=50)
lb_status.place(x=495, y=50)
bt_img.place(x=95, y=340)
bt_proc.place(x=195,y=340)
bt_busca.place(x=400, y=80)

# loop principal
wd.mainloop()

