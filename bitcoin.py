import requests
import tkinter as tk
from datetime import datetime

def track_bitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price1 = response["USD"]
    price2 = response["JPY"]
    price3 = response["EUR"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text=str(price1)+"$\n"+str(price2)+"¥\n"+str(price3)+"€", bg="#24fc03")
    labelTime.config(text="Updated at "+time, bg="#24fc03")

    canvas.after(5000, track_bitcoin)

canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("Bitcoin Tracker")
canvas.config(bg="#24fc03")

f1 = ("poppins", 24, "bold")
f2 = ("poppins", 22, "bold")
f3 = ("poppins", 18, "normal")

label = tk.Label(canvas, text="Bitcoin Price", font=f1, bg="#24fc03")
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2)
labelPrice.pack(pady=20)

labelTime = tk.Label(canvas, font=f3)
labelTime.pack(pady=20)

track_bitcoin()

canvas.mainloop()