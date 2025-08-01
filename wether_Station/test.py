import tkinter as tk

def start_countdown():
    time_str = time_value.get()
    minutes, seconds = map(int, time_str.split(":"))
    total_seconds = minutes * 60 + seconds
    update_timer(total_seconds)

def update_timer(seconds_left):
    if seconds_left >= 0:
        mins, secs = divmod(seconds_left, 60)
        countdown.config(text=f"{mins:02d}:{secs:02d}")
        root.after(1000, update_timer, seconds_left - 1)

root = tk.Tk()
root.title("Countdown Timer")
root.config(bg="white")

# Label to show countdown
countdown = tk.Label(root, text="00:00", font=("Oswald", 40), bg="white", fg="black")
countdown.pack(pady=20)

# Time selection
timevalue = ["00:30", "01:00", "05:00", "10:00", "15:00", "20:00", "25:00"]
time_value = tk.StringVar(value=timevalue[0])

select_time = tk.OptionMenu(root, time_value, *timevalue)
select_time.config(font=("Oswald", 12))
select_time.pack(pady=10)

# Start button
start_button = tk.Button(root, text="Start Countdown", font=("Oswald", 12), command=start_countdown)
start_button.pack(pady=10)

root.mainloop()
