import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Checkbutton, Radiobutton, Notebook, Label
import urllib.request
import xml.dom.minidom
import datetime
from datetime import datetime, date, time
from Period import weeks, months, cvarts, years
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
########################
import datetime

date = datetime.datetime.today()
date = date.strftime('%d.%m.%Y')
try:
    URL = urllib.request.urlopen("http://cbr.ru/scripts/XML_daily.asp?date_req=" + date)
except:
    message = Tk()
    message.withdraw()
    messagebox.showinfo("Error", "No Internet Connection")
    sys.exit()
    message.mainloop()

dom = xml.dom.minidom.parse(URL)
dom.normalize()
Valute = dom.getElementsByTagName("Name")
ValuteName = []
for node in Valute:
    Data = node.childNodes
    for node in Data:
        ValuteName.append(str(node.nodeValue))
ValuteName.append("Российский Рубль")
ValuteName = sorted(ValuteName)

########################

window = Tk()
window.title("Конвертер валют")
window.geometry("600x300")

########################
########################
vkladki = Notebook(window)
vkladka1 = Frame(vkladki)
labelv1 = Label(vkladka1, background="midnight blue")
labelM1 = Label(vkladka1, background="midnight blue", text="ВАЛЮТА 1", font="Courier",
                foreground="SteelBlue3")
labelM2 = Label(vkladka1, background="midnight blue", text="ВАЛЮТА 2", font="Courier",
                foreground="SteelBlue3")
vkladki.add(vkladka1, text="Калькулятор валют")
combobox1 = Combobox(vkladka1)
combobox1["values"] = ValuteName
combobox2 = Combobox(vkladka1)
combobox2["values"] = ValuteName
fieldm1 = Entry(vkladka1)
vkladka1.configure(background="midnight blue")


def Value1():
    Valute = dom.getElementsByTagName("Valute")
    cb1 = combobox1.get()
    if cb1 != "Российский Рубль":
        for node in Valute:
            if (node.childNodes[3].childNodes[0].nodeValue) == cb1:
                A = (node.childNodes[4].childNodes[0].nodeValue)
                B = (node.childNodes[2].childNodes[0].nodeValue)
                A = float(A.replace(',', '.'))
                B = float(B.replace(',', '.'))
                C = (A / B)
    else:
        C = 1
    return (C)


def Value2():
    Valute = dom.getElementsByTagName("Valute")
    cb2 = combobox2.get()
    if cb2 != "Российский Рубль":
        for node in Valute:
            if (node.childNodes[3].childNodes[0].nodeValue) == cb2:
                A = (node.childNodes[4].childNodes[0].nodeValue)
                B = (node.childNodes[2].childNodes[0].nodeValue)
                A = float(A.replace(',', '.'))
                B = float(B.replace(',', '.'))
                T = (A / B)
    else:
        T = 1
    return (T)


def Convert():
    cb2 = combobox2.get()
    K = fieldm1.get()
    K = float(K.replace(',', '.'))
    Val = (Value1() / Value2()) * K
    Val = str(Val)
    labelv1.config(text=cb2 + ":" + Val, font="Times")


convertbut = Button(vkladka1, text="Конвертировать", bg="SteelBlue3", activebackground="SteelBlue3", command=Convert)

labelv1.place(x=250, y=180, relheight=0.1)
convertbut.place(x=400, y=50, relheight=0.1)
fieldm1.place(x=250, y=50, relheight=0.1)
labelM1.place(x=90, y=30, relheight=0.1)
combobox1.place(x=50, y=50, relheight=0.1)
labelM2.place(x=90, y=160, relheight=0.1)
combobox2.place(x=50, y=180, relheight=0.1)
########################
vkladka2 = Frame(vkladki)
vkladki.add(vkladka2, text="Динамика курса")
radio_state = IntVar()
labelv2 = Label(vkladka2, background="midnight blue", text="Период:", foreground="DeepSkyBlue3")
labelv22 = Label(vkladka2, background="midnight blue", text="Валюта:", foreground="DeepSkyBlue3")
labelv23 = Label(vkladka2, background="midnight blue", text="Выбор периода:", foreground="DeepSkyBlue3")

combobox3 = Combobox(vkladka2)


def ValCb3():
    for i in range(len(ValuteName)):
        if ValuteName[i] == "Российский Рубль":
            del (ValuteName[i])
            break
    return (ValuteName)


combobox3["values"] = ValCb3()
combobox4 = Combobox(vkladka2)


def wk():
    combobox4["values"] = weeks()


radiobutton1 = tk.Radiobutton(vkladka2, text="Неделя", value=1, variable=radio_state, bg="midnight blue",
                              activebackground="midnight blue", fg="DeepSkyBlue3", selectcolor="black",
                              command=wk)


def mh():
    combobox4["values"] = months()


radiobutton2 = tk.Radiobutton(vkladka2, text="Месяц", value=2, variable=radio_state, bg="midnight blue",
                              activebackground="midnight blue", fg="DeepSkyBlue3", selectcolor="black",
                              command=mh)


def cv():
    combobox4["values"] = cvarts()


radiobutton3 = tk.Radiobutton(vkladka2, text="Квартал", value=3, variable=radio_state, bg="midnight blue",
                              activebackground="midnight blue", fg="DeepSkyBlue3", selectcolor="black",
                              command=cv)


def yr():
    combobox4["values"] = years()


radiobutton4 = tk.Radiobutton(vkladka2, text="Год", value=4, variable=radio_state, bg="midnight blue",
                              activebackground="midnight blue", fg="DeepSkyBlue3", selectcolor="black",
                              command=yr)


def buildgraph():
    x = []
    y = []
    Valute = dom.getElementsByTagName("Valute")
    cb3 = combobox3.get()
    for node in Valute:
        attrs = dict(node.attributes.items())
        if cb3 == node.childNodes[3].childNodes[0].nodeValue:
            ValuteID = str(attrs["ID"])
            l = combobox4.get().find('-')
            Dat1 = str(combobox4.get()[:l])
            Dat2 = str(combobox4.get()[l + 1:])
    URL = urllib.request.urlopen("http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=" + Dat1 + "&date_req2=" + Dat2
                                 + "&VAL_NM_RQ=" + ValuteID)
    bom = xml.dom.minidom.parse(URL)
    bom.normalize()
    Valute = bom.getElementsByTagName("Record")
    for node in Valute:
        attrs = dict(node.attributes.items())
        x.append(attrs["Date"])
        Val = node.childNodes[1].childNodes[0].nodeValue
        Val = float(Val.replace(',', '.'))
        y.append(Val)

    wingrap = Tk()
    wingrap.geometry("635x480")
    wingrap.title("График")
    matplotlib.use('TkAgg')
    fig = plt.figure()
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, wingrap)
    plot_widget = canvas.get_tk_widget()
    fig.clear()
    plt.plot(x, y)
    rb = radio_state.get()
    if rb == 2:
        plt.xticks(np.arange(0, len(x) + 1, 10))
    if rb == 3:
        plt.xticks(np.arange(0, len(x) + 1, 15))
    if rb == 4:
        plt.xticks(np.arange(0, len(x) + 1, 60))
    plt.grid()
    plot_widget.grid(row=0, column=0)
    wingrap.iconbitmap("Dollar.ico")
    wingrap.resizable(0, 0)
    wingrap.mainloop


button2 = Button(vkladka2, text="Построить график", command=buildgraph)

labelv2.place(x=215, y=10)
labelv22.place(x=75, y=10)
labelv23.place(x=375, y=10)
combobox3.place(x=25, y=30)
button2.place(x=25.2, y=215)
combobox4.place(x=350, y=30)
radiobutton1.place(x=200, y=30)
radiobutton2.place(x=200, y=70)
radiobutton3.place(x=200, y=110)
radiobutton4.place(x=200, y=150)
vkladka2.configure(background='midnight blue')
########################
vkladki.pack(expand=True, fill=BOTH)
# window.iconbitmap("Dollar.ico")
window.resizable(0, 0)
window.mainloop()

# 3301
