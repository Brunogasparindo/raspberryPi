import tkinter as tk
from tkinter import HORIZONTAL, ON, VERTICAL, ttk


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
        self.var_5 = tk.DoubleVar(value=75.0)

        # Create widgets :)
        self.setup_widgets()
    
    
    def setup_widgets(self):
        # Create a Frame for the Checkbuttons


        # Create a Frame for the Radiobuttons
        self.radio_frame = ttk.LabelFrame(self, text="RGB", padding=(20, 10))
        self.radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

        # Radiobuttons
        self.radio_1 = ttk.Radiobutton(
            self.radio_frame, text="RED", variable=self.var_3, value=1
        )
        self.radio_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
        self.radio_2 = ttk.Radiobutton(
            self.radio_frame, text="GREEN", variable=self.var_3, value=2
        )
        self.radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
        self.radio_4 = ttk.Radiobutton(
            self.radio_frame, text="BLUE", variable=self.var_3, value=3
        )
        self.radio_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

        # Separator
        self.separator = ttk.Separator(self, orient='vertical')
        self.separator.grid(row=1, column=1, padx=(50, 50), pady=10, sticky="ew")

        # Create a Frame for input widgets
        self.widgets_frame = ttk.Frame(self, padding=(0, 0, 0, 10))
        self.widgets_frame.grid(
            row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3
        )
        self.widgets_frame.columnconfigure(index=0, weight=1)

        # Spinbox
        self.spinbox = ttk.Spinbox(self.widgets_frame, from_=0, to=24, increment=0.1)
        self.spinbox.insert(0, "UHRZEIT")
        self.spinbox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

        """"
        # Read-only combobox
        self.readonly_combo = ttk.Combobox(
            self.widgets_frame, state="readonly", values=self.readonly_combo_list
        )
        self.readonly_combo.current(0)
        self.readonly_combo.grid(row=3, column=0, padx=5, pady=10, sticky="ew")
        """
        # Switch
        self.switch = ttk.Checkbutton(
            self.widgets_frame, style="Switch.TCheckbutton"
        )
        self.switch.grid(row=10, column=0, padx=0, pady=0, sticky="nsew")

         # Panedwindow
        self.paned = ttk.PanedWindow(self)
        self.paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)    
        # Notebook, pane #2
        self.pane_2 = ttk.Frame(self.paned, padding=5)
        self.paned.add(self.pane_2, weight=3)
        """
        self.notebook = ttk.Notebook(self.pane_2)
        self.notebook.pack(fill="both", expand=True)

        # Tab #1
        self.tab_1 = ttk.Frame(self.notebook)
        for index in [0, 1]:
            self.tab_1.columnconfigure(index=index, weight=1)
            self.tab_1.rowconfigure(index=index, weight=1)
        self.notebook.add(self.tab_1, text="WÄRME")
        """
        self.scale_frame = ttk.LabelFrame(
            self,
            text="WÄRME",
            padding=(20, 10))
        self.scale_frame.grid(row=2, column=5, padx=(20, 10), pady=10, sticky="nsew")
        # Scale
        self.scale = ttk.Scale(
            self.scale_frame,
            from_=255,
            to=-255,
            variable=self.var_5,
            command=lambda event: self.var_5.set(self.scale.get()),
        )
        self.scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

        # Label
        self.label = ttk.Label(
            self.scale_frame,
            text="Kälter ---------- Wärmer",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        self.label.grid(row=1, column=0, pady=10, columnspan=2)

        

        # Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("")

#     # Simply set the theme
#     root.tk.call("source", "azure.tcl")
#     root.tk.call("set_theme", "dark")

#     app = App(root)
#     app.pack(fill="both", expand=True)

#     # Set a minsize for the window, and place it in the middle
#     root.update()
#     root.minsize(root.winfo_width(), root.winfo_height())
#     x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
#     y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
#     root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

#     root.mainloop()
