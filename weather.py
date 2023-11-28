from tkinter import *
import tkinter as tk
import requests
import time

def getweather():
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=780747910ea0f0518a76e8e4dd933fb2"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']
    humidity = json_data['main']['humidity']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']-21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']-21600))

    n.config(text="Current Weather")
    temperature.config(text=(temp,"°C"))
    cloud.config(text =(condition, "|", "FEELS", "LIKE", temp,"°" ))

    Pressure.config(text=pressure)
    Wind_Speed.config(text=wind)
    Humidity.config(text=humidity)
    Sunrise.config(text=sunrise)
    Sunset.config(text=sunset)


root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")

f = ("poppins", 25, "bold")
t = ("poppins", 15, "bold")
m = ("arial", 50, "bold")
n = ("arial", 20, "bold")

#Search box
Search_image = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20,y=20)

textfield = tk.Entry(root, justify="center", font=f, bg="#404040", border=0, fg="white")
textfield.place(x=50,y=40)
textfield.focus()


#Search Icon
Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, border=0, cursor="hand2", bg="#404040", command=getweather)
myimage_icon.place(x=400,y=34)


#Logo
Logo_image = PhotoImage(file="logo.png")
logo = Label(image=Logo_image)
logo.place(x=160,y=100)

#box
box_image = PhotoImage(file="box.png")
box = Label(image=box_image)
box.pack(padx=5, pady=5, side=BOTTOM)

#Label
label1 = Label(root, text="PRESSURE", font=t, bg="#1ab5ef", fg="white")
label1.place(x=120, y=400)
label2 = Label(root, text="WIND SPEED", font=t, bg="#1ab5ef", fg="white")
label2.place(x=250, y=400)
label3 = Label(root, text="HUMIDITY", font=t, bg="#1ab5ef", fg="white")
label3.place(x=410, y=400)
label4 = Label(root, text="SUNRISE", font=t, bg="#1ab5ef", fg="white")
label4.place(x=560, y=400)
label5 = Label(root, text="SUNSET", font=t, bg="#1ab5ef", fg="white")
label5.place(x=700, y=400)

n = Label(root, font=t)
n.place(x=420, y=150)

temperature = Label(root,font=m, fg="#ee666d")
temperature.place(x=440, y=200)

cloud = Label(root,font=t)
cloud.place(x=440, y=300)


Pressure=Label(text="...", font=n, bg="#1ab5ef")
Pressure.place(x=150, y=430)
Wind_Speed=Label(text="...", font=n, bg="#1ab5ef")
Wind_Speed.place(x=300, y=430)
Humidity=Label(text="...", font=n, bg="#1ab5ef")
Humidity.place(x=440, y=430)
Sunrise=Label(text="...", font=n, bg="#1ab5ef")
Sunrise.place(x=550, y=430)
Sunset=Label(text="...", font=n, bg="#1ab5ef")
Sunset.place(x=690, y=430)


root.mainloop()

