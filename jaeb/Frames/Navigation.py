import tkinter as tk
from tkinter import ttk


class NavBar(ttk.Frame):
    #initialize frame
    def __init__(self, container):
        super().__init__(container)
        #set container as self.parentWindow to access the mainWindow
        self.parentWindow = container
        #highlights the button with value set to 2
        self.var = tk.IntVar(value=2)
        #sets up grid and columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)    
        self.columnconfigure(2, weight=1)    
        self.columnconfigure(3, weight=1)    
        self.columnconfigure(4, weight=1)  

        # BTN 1 - buttons for navigation
        self.nav_0 = ttk.Radiobutton(
                    self,
                    text='Brightness History',
                    style="Toggle.TButton",
                    command=self.menuNav_History,
                    variable=self.var,
                    value=0
                    )
        self.nav_0.grid(column=0, row=0,sticky=tk.EW, padx=5)

        # BTN 2 - buttons for navigation
        self.nav_1 = ttk.Radiobutton(
                    self,
                    text='Configuration',
                    style="Toggle.TButton",
                    command=self.menuNav_Config,
                    variable=self.var,
                    value=0
                    )
        self.nav_1.grid(column=2, row=0,sticky=tk.EW, padx=5)
        
    # BTN 1
    def menuNav_History(self):
        #clears the frame
        self.clear_frame()
        #selects the new frame
        self.parentWindow.navigateHistory()
        self.parentWindow.brightnessHistoryFrame.pack()

    # BTN 2
    def menuNav_Config(self):
        #clears the frame
        self.clear_frame()
        #selects the new frame
        self.parentWindow.navigateConfig()
        self.parentWindow.configFrame.pack()
    
    
    #does exactly as the name implies
    def clear_frame(self):
        #goes through all frames on screen
        for frame in self.parentWindow.winfo_children():
            #checks if the frame is not the navbar
            if frame != self:
                #forgets the frame while keeping the navbar
                frame.destroy()
    
    #does exactly as the name implies
    def destroy_frame(self):
        #goes through all frames on screen
        for frame in self.parentWindow.winfo_children():
                #destroys everything it comes across
                frame.destroy()
    
