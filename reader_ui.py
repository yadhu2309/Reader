import tkinter as tk
from tkinter import filedialog
import os
import threading

import pyttsx3

# engine = pyttsx3.init()
# engine.say('yadhu')
# engine.runAndWait()

import queue

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def reader(file_path):
    book = open(file_path, 'r')
    book_text = book.readlines()

   

    # Create a queue to store the lines of text
    text_queue = queue.Queue()

    # Add the lines of text to the queue
    for line in book_text:
        text_queue.put(line)

    # Define a function to speak the lines of text
    def speak():
        while not text_queue.empty():
            line = text_queue.get()
            engine.say(line)
            engine.runAndWait()

    # Start a new thread to speak the lines of text
    threading.Thread(target=speak).start()


def choose_file():
    # Open a file dialog and return the path of the selected file
    file_path = filedialog.askopenfilename(
        title="Choose a file",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if file_path:
    # Update the label with the selected file path
        file_label.config(text=file_path)
        root.update()
        reader(file_path)
    # print(file_path)
# def play():
#     print('playing')
#     engine.runAndWait()
    

# def pause():
#     print('pausing')
#     engine.stop()   

# def stop():
#     print('stoping')
#     engine.stop()
# Create the root window
root = tk.Tk()
root.geometry("500x400")  # Set the size of the window

# Create a button to open the file dialog
file_button = tk.Button(
    root,
    text="Choose a file",
    command=choose_file
)

# Create buttons for play, pause and stop
# play_button = tk.Button(
#     root,
#     text='Play',
#     command=play

# )

# pause_button = tk.Button(
#     root,
#     text='Pause',
#     command=pause

# )

# stop_button = tk.Button(
#     root,
#     text='Stop',
#     command=stop

# )

# Create a label to display the selected file path
file_label = tk.Label(root)

# Pack the widgets
file_button.pack()
# play_button.pack()
# pause_button.pack()
# stop_button.pack() 
file_label.pack()

# Start the event loop
root.mainloop()



