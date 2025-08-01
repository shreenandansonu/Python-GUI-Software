import tkinter as tk
import requests
import json
root=tk.Tk()

root.title("Wether APP")
root.iconbitmap('wether_Station\img.ico')
root.geometry('1080x720')
root.configure(bg="#343a40")

def findwether()-> None:
    city=city_enter.get()
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=1ed6219a920e748e463f58c5b81c79ed"
    #above one is a formated string for city 
    data=requests.get(url)
    if data.status_code==200: # checks if the data is fetched properly or not
        data=json.loads(data.text) #converts the string data into DICTIONARY format
        # print(f"🏙️ City Name: {data['name']}")
        temp.config(text=f"🌡️ City Temperature: {data['main']['temp']} °C")
        humidity.config(text=f"💦 City Humidity: {data['main']['humidity']}%")
        city_enter.delete(0,tk.END)
        # print(f"🌡️ City Temperature: {data['main']['temp']} °C")
        # print(f"🥶 City Feels like: {data['main']['feels_like']}°C")
        # print(f"💦 City Humidity: {data['main']['humidity']}%")
        # print(f"🌇 City Sky: {data['weather'][0]['description']}")
        # print(f"🍃 City Wind: {data['wind']['speed']}km/hr")
        

    else:
        print("Could Not find Place")


head_frame=tk.Frame(root,bg="#495057")
head_frame.grid(row=0,column=0)
heading = tk.Label(head_frame, text="SNS WEATHER APP", font=("Arial", 50), background="#ffffff")
heading.pack(fill='x')
input_frame=tk.Frame(root,bg="#000000")
input_frame.grid(row=1,column=0)
city_enter=tk.Entry(input_frame)
city_enter.grid(row=0,column=0)
enter_button=tk.Button(input_frame,text="Find",command=findwether)
enter_button.grid(row=0,column=1)

output_frame=tk.Frame(root,bg="#495555")
output_frame.grid(row=2,column=0,columnspan=5)
temp=tk.Label(output_frame,text="Temperature")
temp.grid(row=0,column=1,sticky="nsew")
humidity=tk.Label(output_frame,text="Humidity")
humidity.grid(row=1,column=1,sticky="nsew")


root.mainloop()