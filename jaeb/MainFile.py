import sys
sys.path.append('./jaeb/Frames')
import tkinter as tk
import Frames.BrightnessHistory as bhf



#setup the base window

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Artificial-Light-Sensor-App')
        window_width = 480
        window_height = 600

        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)
        self.iconbitmap('.\jaeb\style\ScooTeq_Icon.ico')

        self.brightnessVisualizationFrame = bhf.brightnessHistoryFrame(self)
        self.brightnessVisualizationFrame.pack()

root = App()
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    
    root.tk.call("source", "azure.tcl")
    root.tk.call("set_theme", "dark")
    
    root.mainloop()