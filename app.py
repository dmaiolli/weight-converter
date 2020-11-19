from tkinter import *
window = Tk()

def kg_convert():
    # Converter kg para grama
    grama = float(e2_value.get()) * 1000

    # Converter kg para libras
    lbs = float(e2_value.get()) * 2.20462

    # Converter kg para tonelada
    ton = float(e2_value.get()) * 0.001

    t1.delete("1.0", END)
    t1.insert(END, grama)

    t2.delete("1.0", END)
    t2.insert(END, lbs)

    t3.delete("1.0", END)
    t3.insert(END, ton)


e1 = Label(window, text= "Coloque o valor a ser convertido em KG")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Grama")
e4 = Label(window, text="Libras")
e5 = Label(window, text="Tonelada")

t1 = Text(window, height=1, width=20)
t2 = Text(window, height=1, width=20)
t3 = Text(window, height=1, width=20)

button = Button(window, text="Converter", command=kg_convert)


def grid():
    e1.grid(row=0, column=0)
    e2.grid(row=0, column=1)
    e3.grid(row=1, column=0)
    e4.grid(row=1, column=1)
    e5.grid(row=1, column=2)

    t1.grid(row=2, column=0)
    t2.grid(row=2, column=1)
    t3.grid(row=2, column=2)

    button.grid(row=0, column=2)

grid()
window.mainloop()