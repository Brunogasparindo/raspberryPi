import tkinter as tk
from tkinter import  ttk
from urllib import request
from tktimepicker import AnalogPicker, AnalogThemes
import requests




class ConfigFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        # Make the app responsive
        for index in [0, 1, 2]:
            self.columnconfigure(index=index, weight=1)
            self.rowconfigure(index=index, weight=1)

        # Create value lists
        self.option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
        self.combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
        self.readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

        # Create control variables
        self.var_0 = tk.BooleanVar()
        self.var_1 = tk.BooleanVar(value=True)
        self.var_2 = tk.BooleanVar()
        self.var_3 = tk.IntVar(value=4)
        self.var_4 = tk.StringVar(value=self.option_menu_list[1])
        self.var_5 = tk.DoubleVar(value=100.0)
        self.var_6 = tk.DoubleVar(value=100.0)
        self.var_7 = tk.DoubleVar(value=100.0)
        self.var_8 = tk.DoubleVar(value=80.0)

        # Create widgets :)
        self.setup_widgets()


    def save(self):
        print(self.fromInput.get(), self.untilInput.get())
        print(self.var_8.get())

        requests.post('http://192.168.137.64:5000/setConfig', data={'test': '123'})
        return
    
    
    def setup_widgets(self):
        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # Panedwindow
        self.paned = ttk.PanedWindow(self)
        self.paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)    
        # Notebook, pane #2
        self.pane_2 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_2, weight=3)

        # Scale red
        self.scale_frame_red = ttk.LabelFrame(
            self,
            text="RED",
            padding=(20, 10))
        self.scale_frame_red.grid(row=2, column=1, padx=(20, 10), pady=10, sticky="nsew")
        
        self.scaleRed = ttk.Scale(
            self.scale_frame_red,
            from_=0,
            to=100,
            variable=self.var_5,
            command=lambda event: self.var_5.set(self.scaleRed.get()),
        )
        self.scaleRed.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

        # Scale blue
        self.scale_frame_blue = ttk.LabelFrame(
            self,
            text="BLUE",
            padding=(20, 10))
        self.scale_frame_blue.grid(row=3, column=1, padx=(20, 10), pady=10, sticky="nsew")
        
        self.scaleBlue = ttk.Scale(
            self.scale_frame_blue,
            from_=0,
            to=100,
            variable=self.var_6,
            command=lambda event: self.var_6.set(self.scaleBlue.get()),
        )
        self.scaleBlue.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

        # Scale green
        self.scale_frame_green = ttk.LabelFrame(
            self,
            text="GREEN",
            padding=(20, 10))
        self.scale_frame_green.grid(row=4, column=1, padx=(20, 10), pady=10, sticky="nsew")
        
        self.scaleGreen = ttk.Scale(
            self.scale_frame_green,
            from_=0,
            to=100,
            variable=self.var_7,
            command=lambda event: self.var_7.set(self.scaleGreen.get()),
        )
        self.scaleGreen.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")


        # Scale Brightness
        self.scale_frame_bright = ttk.LabelFrame(
            self,
            text="BRIGHTNESS",
            padding=(20, 10))
        self.scale_frame_bright.grid(row=5, column=1, padx=(20, 10), pady=10, sticky="nsew")
        
        self.scaleBright = ttk.Scale(
            self.scale_frame_bright,
            from_=0,
            to=100,
            variable=self.var_8,
            command=lambda event: self.var_8.set(self.scaleBright.get()),
        )
        self.scaleBright.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

        # Time
        self.fromLabel = ttk.Label(self, text='From')
        self.fromLabel.grid(row=6, column=0, sticky=tk.W, padx=40)
        self.fromInput = ttk.Entry(self, width=30)
        # self.fromInput = AnalogPicker(self)
        self.fromInput.grid(row=6, column=1, sticky=tk.W, padx=40)

        self.untilLabel = ttk.Label(self, text='Until')
        self.untilLabel.grid(row=7, column=0, sticky=tk.W, padx=40)
        self.untilInput = ttk.Entry(self, width=30)
        # self.untilInput = AnalogPicker(self)
        self.untilInput.grid(row=7, column=1, sticky=tk.W, padx=40)

        self.saveConfig = tk.Button(text="Save", command=self.save)
        self.saveConfig.pack(side=tk.BOTTOM)
