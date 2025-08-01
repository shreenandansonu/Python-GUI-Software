import tkinter as tk
from tkinter import messagebox

c1="#e63946"
c2="#f1faee"
c3="#a8dadc"
c4="#1d3557"
h=400
w=300
root=tk.Tk()
root.geometry('300x400')
root.maxsize(height=h,width=w)
root.minsize(height=h,width=w)
root.title("POMODORO")
root.iconbitmap("clock.ico")
root.config(bg=c2)
root.columnconfigure(0,weight=1)


wait=None
totaltime=0
is_paused=False
is_interupt=False

def start_countdown():
    # messagebox.showinfo("Countdown Started",f"Your {time_value.get()} minutes session starts now.")
    select_time["state"]="disabled"
    start["state"]="disabled"
    restart["state"]="normal"
    playpause["state"]="normal"
    time=time_value.get()
    # print(time)
    min,sec=map(int,time.split(":"))
    global totaltime
    totaltime=min*60+sec
    # print(totaltime)
    update_counter(totaltime)
    
def update_counter(tim):
    global totaltime, is_interupt
    totaltime=tim
    if totaltime>=0 and not is_interupt :
        global wait
        min,sec=divmod(totaltime,60)
        time_min_sec=f"{min:02d}:{sec:02d}"
        countdown.config(text=time_min_sec)
        wait=root.after(1000, update_counter, totaltime - 1)
    else:
        totaltime=0
        countdown["text"]="00:00"
        select_time["state"]="normal"
        start["state"]="normal"
        restart["state"]="disabled"
        playpause["state"]="disabled"
        if is_interupt:
            messagebox.showwarning("Countdown Endded","You Restarted The Countdown")
            is_interupt=False
        else:
            messagebox.showinfo("Countdown Endded",f"GREAT JOB! 🎉 \n Your {time_value.get()} minutes session ended.")

def reset_counter():
    global is_interupt
    is_interupt=True

def playpause_counter():
    global is_paused,wait
    if is_paused:
        is_paused=False
        playpause["text"]="PAUSE"
        restart["state"]="normal"
        start["state"]="disabled"
        update_counter(totaltime)
    else:
        is_paused=True
        playpause["text"]="PLAY"
        root.after_cancel(wait)
        restart["state"]="disabled"
        start["state"]="disabled"


#widgets
headframe=tk.Frame(root,bg=c4)
headframe.grid(column=0,row=0,columnspan=1,rowspan=1,sticky="news")
headframe.rowconfigure(0,weight=1)
headframe.columnconfigure(0,weight=1)
name=tk.Label(headframe,text="POMODORO",font=("Oswald Medium",30),foreground=c2,bg=c4)
name.grid(column=0,row=0)
timevalue=["00:00","01:00","05:00","10:00","15:00","20:00","25:00","30:00","40:00","45:00","50:00","60:00"]
time_show_frame=tk.LabelFrame(root,text="COUNTDOWN",bg=c2,font=("Oswald",10))
time_show_frame.grid(column=0,row=1,rowspan=1,sticky="news",padx=5)
time_show_frame.columnconfigure(0,weight=1)
time_show_frame.columnconfigure(0,weight=1)
countdown=tk.Label(time_show_frame,text="00:00",font=("Oswald Medium",40),bg=c2,fg=c4)
countdown.grid(column=0,row=0,padx=5,pady=5)

time_frame=tk.LabelFrame(root,text="OWN YOUR TIME",bg=c2,font=("Oswald",10))
time_frame.grid(column=0,row=2,rowspan=1,sticky="news",padx=5)
time_frame.columnconfigure(0,weight=1)

time_value=tk.StringVar()
time_value.set(timevalue[0])

time_label=tk.Label(time_frame,text="Time Duration",font=("Oswald Medium",15),bg=c2,fg=c4)
time_label.grid(row=0,column=0,columnspan=1,rowspan=1,sticky='w',padx=5,pady=5)

def time_selected(time_value):
    countdown.config(text=time_value)


select_time=tk.OptionMenu(time_frame,time_value,*timevalue,command=time_selected)
select_time.config(font=("Oswald",10),bg=c2,activebackground=c2)
select_time.grid(column=1,row=0,columnspan=1,rowspan=1,padx=5,pady=5,sticky='E')
# start=tk.Button(time_frame,text="Start",bg=c3)
# start.grid(column=0,row=0)

control_frame=tk.LabelFrame(root,text="CONTROLS",bg=c2,font=("Oswald",10))
control_frame.grid(column=0,row=3,columnspan=1,rowspan=1,sticky="news",padx=5)
padx=5
pady=5
wid=int((w-(6*padx))/3)
start=tk.Button(control_frame,text="START",width=wid,font=("Oswald",10),bg=c4,fg=c2,activebackground=c4,command=start_countdown)
start.grid(column=2,row=1,padx=padx,pady=pady)
restart=tk.Button(control_frame,text="RESTART",width=wid,font=("Oswald",10),bg=c4,fg=c2,activebackground=c4,state="disabled",command=reset_counter)
restart.grid(column=0,row=1,padx=padx,pady=pady)
playpause=tk.Button(control_frame,text="PAUSE",width=wid,font=("Oswald",10),bg=c4,fg=c2,activebackground=c4,state="disabled",command=playpause_counter)
playpause.grid(column=1,row=1,padx=padx)


for col in range(3):
    control_frame.columnconfigure(col,weight=1)

brand=tk.Label(root,text="Designed & developed by Shreenandan Sahu with 💓",bg=c2,font=("Oswald",10))
brand.grid(row=4,padx=padx,pady=pady+2)

root.mainloop()

#pyinstaller --onefile --noconsole --icon=clock.ico pomodoro.py