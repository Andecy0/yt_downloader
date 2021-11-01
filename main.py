from pypresence import Presence
import time
from tkinter import *


window = Tk()
def setpre():
    label.config(text="Durum Ayarlandi")
    entry.destroy()
    button.destroy()
    client_id = '777136079870230528'
    RPC = Presence(client_id)
    RPC.connect()

    pstate = "Butona bassana <3"
    pdetails = "Python"
    b_label = "Ee bascak mısın?"
    b_url = "https://discord.gg/DgqgGaUVyq"
    while True:
        RPC.update(state=pstate, details=pdetails, large_image="est.png", buttons=[{"label":b_label,"url":b_url}])

        time.sleep(1)


label=Label(window)
label.config(text="Durum girin",font=("Arial",20))
label.place(x="20",y="20")

entry = Entry(window)
entry.place(x="20",y="70")

button=Button(window)
button.config(text="Set discord presence",bg="black",fg="white",command=setpre)
button.place(x="20",y="100")
window.title("Discord Presence")
window.configure(width=500, height=400)

mainloop()