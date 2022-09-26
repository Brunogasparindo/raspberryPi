import sqlite3
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

# --- API (Library) ---
import json
from urllib.request import urlopen

# --- API (URL) ---
url = "http://192.168.137.64:5000/items"
response = urlopen(url)

data_json = json.loads(response.read())


# --- API (Abfrage) ---
def lightQuery():
    response = urlopen(url)
    data_json = json.loads(response.read())
    
    return data_json

def fillTableIn(table):
    values = lightQuery()
    counter = 0
    for value in values:
        table.insert(parent='', index='end', iid=counter, values=(value[1], value[2]))
        counter += 1


def fillArray(isBrightness):
    values = lightQuery()
    returnArray = []

    for value in values:
        if isBrightness:
            returnArray.append(value[1])
        else:
            returnArray.append(value[2])
    
    return returnArray



def showGraph():
        x_val = fillArray(False)
        print("+++++++++++++++++++++=======XXXXX =============================================")
        print(len(x_val))
        print(x_val)
        y_val = fillArray(True)
        print("+++++++++++++++++++++===========YYYYYY =========================================")
        print(len(y_val))
        print(y_val)

        plt.plot(x_val, y_val)
        plt.tight_layout()
        plt.xticks([]) # in order to keep the x-axe cleand
        plt.show()


class brightnessHistoryFrame(ttk.Frame):

    # initialize
    def __init__(self, container):
        super().__init__(container)
        self.parentWindow = container

        # setup grid
        # columns
        self.columnconfigure(0)
        self.columnconfigure(1)

        # rows
        self.rowconfigure(0, minsize=30)
        self.rowconfigure(3, minsize=5)
        self.rowconfigure(6, minsize=5)
        self.rowconfigure(9, minsize=5)
        self.rowconfigure(12, minsize=5)

        # Show histoy table
        lightQuery()
        self.table = ttk.Treeview(self)
        self.table.grid(column=0, row=2, sticky=tk.W, padx=20)
        self.table['columns'] = ('brightness', 'date')

        self.table.column("#0", width=0)
        self.table.column("brightness" , width=60)
        self.table.column("date"       , width=120)

        self.table.heading("brightness", text='Brightness')
        self.table.heading("date"      , text='Date')

        fillTableIn(self.table)

        # Graphic
        showGraph()

