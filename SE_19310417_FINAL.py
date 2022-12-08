# -*- coding: utf-8 -*-
"""
SE_19310417
Sistema experto - Rivales en pokemon

@author: Cristian
"""

from tkinter import ttk, messagebox
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import mysql.connector

cnn = mysql.connector.connect(host="localhost", user="root",
                                  passwd="cris2000", database="se_pkm")

pkAtaques = []
pkDefensas = []
pkTotal = []
tipo1 = ""
tipo2 = ""

cur = cnn.cursor()
cur.execute("SELECT * FROM tabla_tipos")
tablaTipos = cur.fetchall()
cur.execute("SELECT * FROM pkm_programados")
listapkm = cur.fetchall()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Cristian\Documents\CETI\ING\7F1\Sistemas Expertos\SE PKM\build\assets\frame3")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def buscaTipo(tipo):
    itipo=10
    if(tipo=='Acero'): itipo=0
    if(tipo=='Agua'): itipo=1
    if(tipo=='Bicho'): itipo=2
    if(tipo=='Dragon'): itipo=3
    if(tipo=='Electrico'): itipo=4
    if(tipo=='Fantasma'): itipo=5
    if(tipo=='Fuego'): itipo=6
    if(tipo=='Hada'): itipo=7
    if(tipo=='Hielo'): itipo=8
    if(tipo=='Lucha'): itipo=9
    if(tipo=='Normal'): itipo=10
    if(tipo=='Planta'): itipo=11
    if(tipo=='Psiquico'): itipo=12
    if(tipo=='Roca'): itipo=13
    if(tipo=='Siniestro'): itipo=14
    if(tipo=='Tierra'): itipo=15
    if(tipo=='Veneno'): itipo=16
    if(tipo=='Volador'): itipo=17
    if(tipo==''): itipo=-1
    return itipo

def buscaAtaque(tabla, lista, t1, t2):
    for i in range(len(lista)):
        it1 = buscaTipo(t1)
        it2 = buscaTipo(t2)
        lt1 = buscaTipo(lista[i][2])
        lt2 = buscaTipo(lista[i][3])
        atk1 = tabla[lt1][it1+1]
        if(it2!=it1): atk1 = atk1 *tabla[lt1][it2+1]
        if(lt2!=-1): 
            atk2=tabla[lt2][it1+1]
            if(it2!=it1): atk2=atk2*tabla[lt2][it2+1]     
        else: 
            atk2 =0
        atkt=atk1+atk2
        #print(lista[i][1],"Pega con ",atk1," Y ",atk2)
        pkAtaques.insert(i,atkt)
   # print(pkAtaques)

def buscaDefensa(tabla, lista, t1, t2):
    for i in range(len(lista)):
        it1 = buscaTipo(t1)
        it2 = buscaTipo(t2)
        lt1 = buscaTipo(lista[i][2])
        lt2 = buscaTipo(lista[i][3])
        
        def1 = tabla[it1][lt1+1]
        if(lt2!=-1): 
            def1 = def1 *tabla[it1][lt2+1] 
        if(it2!=it1): 
            def2=tabla[it2][lt1+1]
            if(lt2!=-1):def2=def2*tabla[it2][lt2+1] 
        else: 
            def2 = 0
        deft=def1+def2
        #print(lista[i][1],"Se defiende con ",def1," Y ",def2)
        pkDefensas.insert(i,deft)
    #print(pkDefensas)

def calculoFinal(lista):
    for i in range(len(pkAtaques)):
        pkTotal.insert(i,[lista[i][1] ,lista[i][4]*int(pkAtaques[i]-pkDefensas[i])])
    
    def takeSecond(elem):
        return elem[1]
    pkTotal.sort(key=takeSecond,reverse=True)
    #print(pkTotal)

def show_selection():
    selec1 = combo1.get()
    selec2 = combo2.get()
    tipo1=selec1
    tipo2=selec2
    print("Tipo 1: ", selec1,"\nTipo 2: ", selec2)
    
    buscaAtaque(tablaTipos, listapkm, tipo1, tipo2)
    buscaDefensa(tablaTipos, listapkm, tipo1, tipo2)
    calculoFinal(listapkm)
    """
    for i in range(len(pkAtaques)):
        pkTotal.insert(i,[listapkm[i][1] ,listapkm[i][4]*int(pkAtaques[i]-pkDefensas[i])])
    
    def takeSecond(elem):
        return elem[1]
    pkTotal.sort(key=takeSecond,reverse=True)
    print(pkTotal) """
    pantallaResultados()
    
def pantallaResultados():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Cristian\Documents\CETI\ING\7F1\Sistemas Expertos\SE PKM\build\assets\frame1")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    window.destroy()
    window2 = Tk()
    window2.geometry("1280x720")
    window2.configure(bg = "#000000")


    canvas = Canvas(
        window2,
        bg = "#000000",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        378.0,
        480.0,
        image=image_image_1
        )
    
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        821.0,
        95.0,
        image=image_image_2
        )
    
    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        251.0,
        135.0,
        image=image_image_3
        )
    
    canvas.create_text(
        500.0,
        585.0,
        anchor="nw",
        text="4°",
        fill="#FFF400",
        font=("Inter Bold", 48 * -1)
        )
    
    canvas.create_text(
        500.0,
        493.0,
        anchor="nw",
        text="3°",
        fill="#FFF400",
        font=("Inter Bold", 48 * -1)
        )
    
    canvas.create_text(
        500.0,
        397.0,
        anchor="nw",
        text="2°",
        fill="#FFF400",
        font=("Inter Bold", 48 * -1)
        )
    
    canvas.create_text(
        500.0,
        301.0,
        anchor="nw",
        text="1°",
        fill="#FFF400",
        font=("Inter Bold", 48 * -1)
        )
    
    canvas.create_rectangle(
        641.0,
        295.0,
        1189.0,
        354.0,
        fill="#0000FF",
        outline="")
    
    canvas.create_rectangle(
        641.0,
        391.0,
        1189.0,
        450.0,
        fill="#0000FF",
        outline="")
    
    canvas.create_rectangle(
        641.0,
        486.0,
        1189.0,
        546.0,
        fill="#0000FF",
        outline="")
    
    canvas.create_rectangle(
        641.0,
        582.0,
        1196.0,
        642.0,
        fill="#0000FF",
        outline="")
    
    canvas.create_text(
        645.0,
        589.0,
        anchor="nw",
        text=pkTotal[3][0],
        fill="#FFF400",
        font=("Inter Bold", 48 * -1)
        )
    
    canvas.create_text(
        648.0,
        493.0,
        anchor="nw",
        text=pkTotal[2][0],
        fill="#FFF400",
        font=("Inter Bold", 48 * -1)
        )
    
    canvas.create_text(
        648.0,
        397.0,
        anchor="nw",
        text=pkTotal[1][0],
        fill="#FFF400",
        font=("Inter Bold", 48 * -1)
        )

    canvas.create_text(
        648.0,
        301.0,
        anchor="nw",
        text=pkTotal[0][0],
        fill="#FFF400",
        font=("Inter Bold", 48 * -1)
        )
    window2.resizable(False, False)
    window2.mainloop()


window = Tk()
window.geometry("1280x720")
window.configure(bg = "#000000")


canvas = Canvas(
    window,
    bg = "#000000",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    188.0,
    108.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    695.0,
    102.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    165.0,
    421.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    window,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=show_selection
)

button_1.place(
    x=1019.0,
    y=505.0,
    width=208.0,
    height=168.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    608.0,
    321.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    961.0,
    321.0,
    image=image_image_5
)

combo1 = ttk.Combobox(
    state="readonly",
    values=["Acero", "Agua", "Bicho", "Dragon", "Electrico", "Fantasma",
            "Fuego", "Hada", "Hielo", "Lucha", "Normal", "Planta", 
            "Psiquico", "Roca", "Siniestro", "Tierra", "Veneno", "Volador"]
)

combo2 = ttk.Combobox(
    state="readonly",
    values=["Acero", "Agua", "Bicho", "Dragon", "Electrico", "Fantasma",
            "Fuego", "Hada", "Hielo", "Lucha", "Normal", "Planta", 
            "Psiquico", "Roca", "Siniestro", "Tierra", "Veneno", "Volador"]
)

combo1.set("Acero")
combo1.place(x=540, y=400)
combo2.set("Acero")
combo2.place(x=890, y=400)


window.resizable(False, False)
window.mainloop()
