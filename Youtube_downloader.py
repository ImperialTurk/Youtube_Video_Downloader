from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube


Folder_Name = ""

# File Location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()

    if (len(Folder_Name) > 1):
        locationError.config(text = Folder_Name, fg = "green")
    else:
        locationError.config(text = "Please Choose Folder", fg = "red")


# Download Video
def downloadVideo():
    choice = ytd_Choices.get()
    url = ytd_Entry.get()

    if (len(url) > 1):
        ytd_Error.config(text = "")
        yt = YouTube(url)

        if (choice == choices[0]):
            select = yt.streams.filter(progressive = True).first()

        elif (choice == choices[1]):
            select = yt.streams.filter(progressive = True).last()

        elif (choice == choices[2]):
            select = yt.streams.filter(only_audio = True).first()

        else:
            ytd_Error.config(text = "Paste Link Again", fg = "red")

    
    select.download(Folder_Name)
    ytd_Error.config(text = "Download Completed")


# USER INTERFACE
root = Tk()
root.title("Youtube Video Downloader")
root.geometry("350x400") # set window
root.columnconfigure(0,weight=1) # set all content in center

# Ytd Link Label
ytd_Label = Label(root, text = "Enter the URL of the Video", font=("jost",15))
ytd_Label.grid()


# Entry Box
ytd_EntryVar = StringVar()
ytd_Entry = Entry(root, width=50, textvariable = ytd_EntryVar)
ytd_Entry.grid()


# Error Message
ytd_Error = Label(root, text = "Please Enter A Valid URL !", fg = "red", font=("jost",10))
ytd_Error.grid()


# Asking Save File Label
saveLabel = Label(root, text = "Save the Video File", font=("jost",15,"bold"))
saveLabel.grid()


# Save Button
saveBtn = Button(root, text = "Choose Path", width = 10, bg = "blue", fg = "white", command = openLocation)
saveBtn.grid()


# Location Error
locationError = Label(root, text = "Please Select Valid File Path !", fg = "red", font=("jost",10))
locationError.grid()


# Download Quality
ytd_Quality = Label(root, text = "Select Quality", font=("jost",15))
ytd_Quality.grid()


# Quality Choice
choices = ["144p","360p","Audio Only"]
ytd_Choices = ttk.Combobox(root, values = choices)
ytd_Choices.grid()


# Download Button
downloadBtn = Button(root, text = "Download", width = 10, bg = "blue", fg = "white", command = downloadVideo)
downloadBtn.grid()


# Developer Label
dev = Label(root, text = "Developed by ImperialTurk", font=("jost",15))
dev.grid()


root.mainloop()
















