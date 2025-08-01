import requests
import json
import tkinter as tk


c1="#f5dfbb"
c2="#f2542d"
c3="#562c2c"
x=5
y=5

w=400
h=51


def wethersearch(event=None):
    city=city_name.get()
    city_name.delete(0,tk.END)
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=1ed6219a920e748e463f58c5b81c79ed"
    #above one is a formated string for city 
    data=requests.get(url)
    if data.status_code==200: # checks if the data is fetched properly or not
        data=json.loads(data.text) #converts the string data into DICTIONARY format
        cityname(data['name'].upper())
        temperature(data['main']['temp'])
        # print(f"🥶 City Feels like: {data['main']['feels_like']}°C")
        humidity(data['main']['humidity'])
        # print(f"🌇 City Sky: {data['weather'][0]['description']}")
        # print(f"🍃 City Wind: {data['wind']['speed']}km/hr")
        h=385
        root.geometry(f'{w}x{h}')
        root.maxsize(width=w,height=h)
        root.minsize(width=w,height=h)
        

    else:
        city="NO SUCH PLACE"
        cityname(city)
        h=165
        root.geometry(f'{w}x{h}')
        root.maxsize(width=w,height=h)
        root.minsize(width=w,height=h)



def cityname(city):
    city_frame=tk.LabelFrame(root,bg=c1,text="CITY",font=("Oswald Medium",10),fg=c3)
    city_frame.grid(column=0,row=1,padx=x,pady=y,sticky="NEWS")
    city_frame.columnconfigure(0,weight=1)
    city_lable=tk.Label(city_frame,text=city,bg=c1,fg=c2,font=("Oswald Medium",30),justify="center")
    city_lable.grid(column=0,row=0)

def temperature(temp):
    temp_frame=tk.LabelFrame(root,bg=c1,text="TEMPERATURE",font=("Oswald Medium",10),fg=c3)
    temp_frame.grid(column=0,row=2,padx=x,pady=y,sticky="NEWS")
    temp_frame.columnconfigure(0,weight=1)
    temp_lable=tk.Label(temp_frame,text=f"{temp} °C",bg=c1,fg=c2,font=("Oswald Medium",30),justify="center")
    temp_lable.grid(column=0,row=0)

def humidity(humid):
    humid_frame=tk.LabelFrame(root,bg=c1,text="HUMIDITY",font=("Oswald Medium",10),fg=c3)
    humid_frame.grid(column=0,row=3,padx=x,pady=y,sticky="NEWS")
    humid_frame.columnconfigure(0,weight=1)
    humid_lable=tk.Label(humid_frame,text=f"{humid} %",bg=c1,fg=c2,font=("Oswald Medium",30),justify="center")
    humid_lable.grid(column=0,row=0)



root=tk.Tk()
root.title("Wether Station")
root.iconbitmap("img.ico")
root.geometry(f'{w}x{h}')
root.maxsize(width=w,height=h)
root.minsize(width=w,height=h)
root.columnconfigure(0,weight=1)
root.config(bg=c1)

name_frame=tk.Frame(root,bg=c2)
name_frame.grid(column=0,row=0,columnspan=1,rowspan=1,sticky="news")
name_frame.columnconfigure(0,weight=1)
name=tk.Label(name_frame,text="WETHER STATION",font=("Oswald Medium",20),bg=c2,fg=c1)
name.grid(row=0,column=0,columnspan=1,rowspan=1,sticky='w',padx=x+x)
city_name=tk.Entry(name_frame,font=("Oswald Medium",10),bg=c1,fg=c2,justify="center")
city_name.grid(row=0,column=1,columnspan=1,sticky='w',padx=x+x,pady=y)
city_name.bind("<Return>", wethersearch)

root.mainloop()


# pyinstaller --onefile --noconsole --icon=img.ico wetherstation.py
