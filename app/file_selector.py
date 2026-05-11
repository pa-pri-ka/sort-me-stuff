from doctest import master
from tkinter import StringVar, ttk


class FileSelector:

	__BUTTON_LABEL = "Browse..."

	__path = None

	def add(self, parent_frame: ttk.Frame, at_grid_row, at_grid_column):
		parent_frame.grid_columnconfigure(at_grid_column, weight=1)
		self.__path = StringVar()
		ttk.Entry(parent_frame, textvariable=self.__path, width=50).grid(column=at_grid_column, row=at_grid_row)
		ttk.Button(parent_frame, text=self.__BUTTON_LABEL).grid(column=at_grid_column + 1, row=at_grid_row)
		return self
