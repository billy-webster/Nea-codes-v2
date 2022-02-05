from tkinter import *
import requests
from ip import *
import matplotlib.pyplot as plt 
import numpy as np
import time
kelvin = 273.15


def apiweather(canvas):
    cityname = textField.get()
    
    key = ("c06a4a716e304b47fb03963722bf177f")
    link =  "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(cityname,key)
    try:
        jsoninfo = requests.get(link)
        jsonformat = jsoninfo.json()
    
        condition = jsonformat['weather'][0]['main']
        temperature = int(jsonformat['main']['temp']- kelvin)
        pressure = int(jsonformat['main']['pressure'])
        humidity= int(jsonformat['main']['humidity'])
        wind = (jsonformat['wind']['speed'])

        maininfo = ("Condition: "+condition2 + 2*"\n" + "Temperature: "+str(temperature2) + "°C")
        otherinfo = ("\n" + "Pressure: " + str({}) + "\n" +"Humidity: " + str({}) + "\n" +"Wind Speed: " + str({})).format(pressure,humidity,wind)
        label1.config(text = maininfo)
        label2.config(text = otherinfo)
    
    except:
        label1.config(text="Enter A Valid City Name")
        label2.config(text="")



canvas = Tk() #creates the display
canvas.geometry("600x500") #sets dimensions
canvas.title("Weather App") #sets title
canvas["bg"]="#b0bea9" #sets background color
#img=PhotoImage(file='weather.png') #creates an image to be implemented
#icon = Label(canvas,image=img,bg="#b0bea9",) #defines the icon as a label which contains the image
#icon.place(x=140,y=80) #places the icon
canvas.resizable(0,0) #doesnt allow the program to be resizable



Label(canvas,width="300", text="Weather Program", bg="#92aa83",fg="white",font=("OpenSans",12,"normal")).pack()
Label(canvas, text="Enter a city: ",bg="#b0bea9",fg="white",font=("OpenSans",12,"bold")).place(x=0,y=50)


textField = Entry(canvas,width = 10, font =("OpenSans", 12, "normal"))
textField.place(x=10,y=80)
textField.bind('<Return>', apiweather)





label1 = Label(canvas, font=("OpenSans", 12, "normal"),bg="#b0bea9",fg="white",borderwidth=1,relief="groove")
label1.place(x=10,y=110)

label2 = Label(canvas, font=("OpenSans", 12, "normal"),bg="#b0bea9",fg="white",borderwidth=1,relief="groove")
label2.place(x=10,y=170)








#current location
label3 = Label(canvas, font=("OpenSans", 12, "bold"),bg="#b0bea9",fg="white",text=("User Location: "+loc))
label3.place(x=380,y=50)

label4 = Label(canvas, font=("OpenSans", 12, "normal"),bg="#b0bea9",fg="white",borderwidth=1,relief="groove")
label4.place(x=400,y=110)

label5 = Label(canvas, font=("OpenSans", 12, "normal"),bg="#b0bea9",fg="white",borderwidth=1,relief="groove")
label5.place(x=400,y=170)

key = ("c06a4a716e304b47fb03963722bf177f")
link =  "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(loc,key)
jsoninfo = requests.get(link)
jsonformat = jsoninfo.json()
    
condition2 = jsonformat['weather'][0]['main']
temperature2 = int(jsonformat['main']['temp']- kelvin)
pressure2 = int(jsonformat['main']['pressure'])
humidity2= int(jsonformat['main']['humidity'])
wind2 = (jsonformat['wind']['speed'])

maininfo2 = ("Condition: "+condition2 + 2*"\n" + "Temperature: "+str(temperature2) + "°C")
otherinfo2 = ("\n" + "Pressure: " + str({}) + "\n" +"Humidity: " + str({}) + "\n" +"Wind Speed: " + str({})).format(pressure2,humidity2,wind2)
label4.config(text = maininfo2)
label5.config(text = otherinfo2)



#forecast
def forecast():
    ytemp=[]
    
    xcord=[]
    forecastlink="https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=minutely,hourly&appid={}&units=metric".format(lat,lon,key)
    request = requests.get(forecastlink)
    r=request.json()
    for i in range(0,7):
        ytemp.append(r['daily'][i]['temp']['day'])
        xcord.append(i)
    
    plt.plot(xcord,ytemp)
    plt.ylabel("Temperature:°C")
    plt.xlabel("Days:")
    plt.show()


def close():
    time.sleep(.5)
    canvas.destroy()

button1 =Button(canvas,text="Forecast:",command=forecast,font=("OpenSans", 12, "normal"),width=50,bg="#92aa83",fg="white")
button1.place(y=350,x=50)   
button2 =Button(canvas,text="Exit",command=close,font=("OpenSans", 12, "normal"),width=50,bg="#92aa83",fg="white")
button2.place(y=400,x=50)  
































canvas.mainloop()