from tkinter import *
import math
import tkinter.messagebox as messagebox

ws = Tk()
ws.title('EGSA')
ws.geometry('225x350')
ws["bg"] = "gray80"

Label(ws, bg='gray81', text="Введите P: ").place(x=50, y=30)
decimal_p_ = Entry(ws)
decimal_p_.place(x=50, y=50)

Label(ws, bg='gray81', text="Введите G: ").place(x=50, y=80)
decimal_g_ = Entry(ws)
decimal_g_.place(x=50, y=100)

Label(ws, bg='gray81', text="Введите X: ").place(x=50, y=130)
decimal_x_ = Entry(ws)
decimal_x_.place(x=50, y=150)

def get_p():
    decimal_number = decimal_p_.get()
    return decimal_number

def get_g():
    decimal_number = decimal_g_.get()
    return decimal_number

def get_x():
    decimal_number = decimal_x_.get()
    return decimal_number

def Answer():

    P = int(get_p())
    G = int(get_g())
    X = int(get_x())

    Y = (G ** X) % P

    M = 5
    K = 2

    flag = True

    for i in range(0, 100):
        while flag:
            if math.gcd(K, P - 1) == 1:
                flag = False
            else:
                K += 1


        
        a = (G ** K) % P
        B = 1

        for i in range(1, 50):
            if (K * B) % (P - 1) == (M - (X * a)) % (P - 1):
                break
            else:
                B += 1

        n = ((Y ** a) * (a ** B)) % P
        l = (G ** M) % P

        if n != l:
            flag = True

    messagebox.showinfo("Результаты",
                            f"A: {a}\n"
                            f"K: {K}\n"
                            f"B: {B}\n"
                            f"M: {M}\n"
                            f"Ya: {n}\n"
                            f"Gm: {l}\n")
btn = Button(ws, text="Зашифровать", command=Answer)
btn.place(x=65, y=185)
ws.mainloop()
