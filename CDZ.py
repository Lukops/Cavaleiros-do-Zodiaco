from tkinter import *
from tkinter import ttk

# Importando o pillow
from PIL import Image, ImageTk

from dados import *

################# cores #############
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

# Criando a janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=271)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frame
frame_anime = Frame(janela, width=550, height=290, relief='flat')
frame_anime.grid(row=1, column=0)

############################################################################

# Função para trocar o personagem
def trocar_personagem(i):
    global imagem_anime, character_image

    # trocando a cor do fundo
    frame_anime['bg'] = personagens[i]['Tipo'][2]

    # Tipo do personagem'
    anime_nome['text'] = i
    anime_nome['bg'] = personagens[i]['Tipo'][2]
    armadura_nome['text'] = personagens[i]['Status'][0]
    armadura_nome['bg'] = personagens[i]['Tipo'][2]

    # Imagem do character
    imagem_anime = personagens[i]['Tipo'][1]

    imagem_anime = Image.open(imagem_anime)
    imagem_anime = imagem_anime.resize((260, 260))
    imagem_anime = ImageTk.PhotoImage(imagem_anime)

    character_image = Label(frame_anime, image=imagem_anime, relief='flat', bg=personagens[i]['Tipo'][2], fg=co1)
    character_image.place(x=110, y=28)

    anime_nome.lift() #faz o nome permanecer acima da imagem
    armadura_nome.lift()

    # Status do personagem
    character_apelido['text'] = personagens[i]['Tipo'][0]
    
    # Podeer de Duelo
    poder_apelido['text'] = personagens[i]['Poder'][0]


############################################################################

# nome
anime_nome = Label(frame_anime, text="Cavaleiros do Zodíaco", relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=co0)
anime_nome.place(x=12, y=15)

# categoria
armadura_nome = Label(frame_anime, text="Nome da Armadura", relief='flat', anchor=CENTER, font=('Ivy 10 bold'), fg=co0)
armadura_nome.place(x=12, y=50)

# Status
character_status = Label(janela, text="Status", relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
character_status.place(x=15, y=310)

# Apelido
character_apelido = Label(janela, text="XXXXX", relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co0)
character_apelido.place(x=15, y=360)

# Poder
monster_status = Label(janela, text="Main Power", relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
monster_status.place(x=15, y=410)

# Mostro nome
poder_apelido = Label(janela, text="XXXXXX", relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
poder_apelido.place(x=15, y=460)

# Criando botões para personagens
# Imagem do BOTÃO
imagem_anime_face = Image.open(r'Projeto - Cavaleiros do Zodíaco/imagens/seiyacabeça.png')
imagem_anime_face = imagem_anime_face.resize((40, 40))
imagem_anime_face = ImageTk.PhotoImage(imagem_anime_face)

botao_image_face = Button(janela, command=lambda:trocar_personagem('Seiya'), image=imagem_anime_face, text="Seiya", width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Verdana 12"), bg=co1, fg=co0)
botao_image_face.place(x=375, y=10)

# Imagem do BOTÃO2
imagem_anime_face2 = Image.open(r'Projeto - Cavaleiros do Zodíaco/imagens/ikkicabeça.png')
imagem_anime_face2 = imagem_anime_face2.resize((40, 40))
imagem_anime_face2 = ImageTk.PhotoImage(imagem_anime_face2)

botao_image_face2 = Button(janela, command=lambda:trocar_personagem('Ikki'), image=imagem_anime_face2, text="Ikki", width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Verdana 12"), bg=co1, fg=co0)
botao_image_face2.place(x=375, y=60)

# Imagem do BOTÃO3
imagem_anime_face3 = Image.open(r'Projeto - Cavaleiros do Zodíaco/imagens/shuncabeça.png')
imagem_anime_face3 = imagem_anime_face3.resize((40, 40))
imagem_anime_face3 = ImageTk.PhotoImage(imagem_anime_face3)

botao_image_face3 = Button(janela, command=lambda:trocar_personagem('Shun'), image=imagem_anime_face3, text="Shun", width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Verdana 12"), bg=co1, fg=co0)
botao_image_face3.place(x=375, y=110)

# Imagem do BOTÃO4
imagem_anime_face4 = Image.open(r'Projeto - Cavaleiros do Zodíaco/imagens/shiryucabeça.png')
imagem_anime_face4 = imagem_anime_face4.resize((40, 40))
imagem_anime_face4 = ImageTk.PhotoImage(imagem_anime_face4)

botao_image_face4 = Button(janela, command=lambda:trocar_personagem('Shiryu'), image=imagem_anime_face4, text="Shiryu", width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Verdana 12"), bg=co1, fg=co0)
botao_image_face4.place(x=375, y=160)

# Imagem do BOTÃO5
imagem_anime_face5 = Image.open(r'Projeto - Cavaleiros do Zodíaco/imagens/Hyogacabeça.png')
imagem_anime_face5 = imagem_anime_face5.resize((40, 40))
imagem_anime_face5 = ImageTk.PhotoImage(imagem_anime_face5)

botao_image_face5 = Button(janela, command=lambda:trocar_personagem('Hyoga'), image=imagem_anime_face5, text="Hyoga", width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Verdana 12"), bg=co1, fg=co0)
botao_image_face5.place(x=375, y=210)

import random
Lista_personagens = ['Seiya', 'Ikki', 'Shun', 'Shiryu', 'Hyoga']

personagem_escolhido = random.sample(Lista_personagens, 1)
print(personagem_escolhido[0])

trocar_personagem(personagem_escolhido[0])

janela.mainloop()
