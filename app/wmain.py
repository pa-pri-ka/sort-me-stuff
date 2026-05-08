from tkinter import *
from tkinter import ttk

class MainWidget:

    __WINDOW_TITLE = "Sort Me Stuff"

    def create(self, initial_width, initial_height):

        widget = Tk()
        widget.title(self.__WINDOW_TITLE)
        
        frame = ttk.Frame(widget, height=initial_height, name="main_widget", padding=8, width=initial_width)
        frame.grid(column=3, ipadx=8, ipady=8, row=3)
        
        return widget
