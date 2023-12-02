import tkinter as tk
from tkinter import ttk

#x axis = 
#y axis = 

xaxis = True
yaxis = False
negativex = False
negativey = False

def find_axis():
    """ This function is used to find the x,y,-x,-y axis of screen. """
    while True:
        if xaxis == True:
            for i in range(0, 10000, 200):
                popup = tk.Tk() #Tkinter initialization

                popup.wm_title("MUTED") #Title of Message
            
                popup.geometry(f"300x300+{i}+0")
                print(i)

                popup.focus() #Focuses the window

                label = ttk.Label(popup, text="YOU'RE MUTED") #Message string - Can change to alphabetical character

                label.pack(side="left", fill="x", pady=10) #Where the message is located in the application
                B1 = ttk.Button(popup, text="Okay", command=exit) #Message + Command of Okay button.
                B1.pack() #Same as label1 Pack, just has nothing in it
                popup.mainloop() #This part finishes the tkinter GUI (Which is a message inside of the GUI
        elif yaxis == True:
            for i in range(0, 10000, 200):
                popup = tk.Tk() #Tkinter initialization

                popup.wm_title("MUTED") #Title of Message
            
                popup.geometry(f"300x300+0+{i}")
                print(i)

                popup.focus() #Focuses the window

                label = ttk.Label(popup, text="YOU'RE MUTED") #Message string - Can change to alphabetical character

                label.pack(side="left", fill="x", pady=10) #Where the message is located in the application
                B1 = ttk.Button(popup, text="Okay", command=exit) #Message + Command of Okay button.
                B1.pack() #Same as label1 Pack, just has nothing in it
                popup.mainloop() #This part finishes the tkinter GUI (Which is a message inside of the GUI
        elif negativex == True:
            for i in range(0, -10000, -200):
                popup = tk.Tk() #Tkinter initialization

                popup.wm_title("MUTED") #Title of Message
            
                popup.geometry(f"300x300+{i}+0")
                print(i)

                popup.focus() #Focuses the window

                label = ttk.Label(popup, text="YOU'RE MUTED") #Message string - Can change to alphabetical character

                label.pack(side="left", fill="x", pady=10) #Where the message is located in the application
                B1 = ttk.Button(popup, text="Okay", command=exit) #Message + Command of Okay button.
                B1.pack() #Same as label1 Pack, just has nothing in it
                popup.mainloop() #This part finishes the tkinter GUI (Which is a message inside of the GUI
        elif negativey == True:
            for i in range(0, -10000, -200):
                popup = tk.Tk() #Tkinter initialization

                popup.wm_title("MUTED") #Title of Message
            
                popup.geometry(f"300x300+0+{i}")
                print(i)

                popup.focus() #Focuses the window

                label = ttk.Label(popup, text="YOU'RE MUTED") #Message string - Can change to alphabetical character

                label.pack(side="left", fill="x", pady=10) #Where the message is located in the application
                B1 = ttk.Button(popup, text="Okay", command=exit) #Message + Command of Okay button.
                B1.pack() #Same as label1 Pack, just has nothing in it
                popup.mainloop() #This part finishes the tkinter GUI (Which is a message inside of the GUI
        else:
            print("Error, nothing is True")
            break


find_axis()