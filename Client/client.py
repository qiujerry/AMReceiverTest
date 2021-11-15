import tkinter as tk




def main():
    window = tk.Tk()

    window.rowconfigure(0, minsize=50)
    window.columnconfigure([0, 1, 2, 3], minsize=50)

    greeting = tk.Label(text="FM Radio Client")

    #greeting.pack()
    greeting.grid(row=0,column=1)

    label1 = tk.Label(text="FM Radio Station: (FM)")
    fm_station = tk.Entry()
    fm_station.insert(0, "89.7")

    def tune_click():
        print(fm_station.get())
        return

    def pause_click():
        print("pause")
        return

    def play_click():
        print("play")
        return
    
    def gain_click():
        print("gain")
        return

    def sd_click():
        print("shut down")
        window.destroy()
        return

    tune = tk.Button(
        text="Tune",
        command = tune_click,
        width=25,
        height=2,
        bg="white",
        fg="black",
    )

    pause = tk.Button(
        text="Pause",
        command = pause_click,
        width=25,
        height=2,
        bg="white",
        fg="black",
    )

    play = tk.Button(
        text="Play",
        command = play_click,
        width=25,
        height=2,
        bg="white",
        fg="black",
    )

    gain = tk.Button(
        text="Adjust Gain",
        command = gain_click,
        width=25,
        height=2,
        bg="white",
        fg="black",
    )
    label2 = tk.Label(text="RX Gain")
    rx_gain = tk.Entry()
    rx_gain.insert(0, "10")

    shut_down = tk.Button(
        text="Shut Down",
        command = sd_click,
        width=25,
        height=2,
        bg="white",
        fg="black",
    )

    #play pause button
    pause.grid(row=1, column=0)
    play.grid(row=1, column=1)

    #tune radio
    label1.grid(row = 2, column = 0)
    fm_station.grid(row = 2, column=1)
    tune.grid(row = 2, column=2)
    #fm_station.pack()

    #adjust gain
    label2.grid(row=3,column=0)
    rx_gain.grid(row=3, column=1)
    gain.grid(row=3, column=2)

    #shut down server and client
    shut_down.grid(row=4, column=1)

    window.mainloop()



if __name__ == "__main__": main()