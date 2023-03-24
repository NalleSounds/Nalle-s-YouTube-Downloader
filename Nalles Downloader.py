# Small YT downloader using tkinter and pytube

import tkinter
import customtkinter
from pytube import YouTube


def startdownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishlabel.configure(text="")
        video.download()
        finishlabel.configure(text="Download complete!", text_color="green")
    except:
        finishlabel.configure(text="Download Error", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent_completion = bytes_downloaded / total_size * 100
    per = str(int(percent_completion))
    pPercent.configure(text=per + '%')
    pPercent.update()

    # Update bar
    progBar.set(float(percent_completion) / 100)

# System settings
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

# app frame
app = customtkinter.CTk()
app.geometry("650x300")
app.title("Nalle's Downloader")

# GUI
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(padx=10, pady=10)

# finish DL
finishlabel = customtkinter.CTkLabel(app, text="")
finishlabel.pack(padx=5, pady=5)

# DL button
download = customtkinter.CTkButton(app, text="Download", command=startdownload)
download.pack(padx=10, pady=10)

# progress %
pPercent = customtkinter.CTkLabel(app, text="0%")
pPercent.pack()

progBar = customtkinter.CTkProgressBar(app, width=400, height=20)
progBar.set(0)
progBar.pack(padx=10, pady=10)

# run app
app.mainloop()
