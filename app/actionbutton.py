from tkinter import ttk
from tktooltip import ToolTip

class ActionButton:
    def __init__(self, text, tooltip=""):
        self._text=text
        self._tooltip=tooltip

    def Add(self, parentframe, row=0):
        button = ttk.Button(parentframe, text=self._text, )
        button.grid(row=row, sticky="ew")
        ToolTip(button, msg=self._tooltip, delay=1.0)
        return self
