from doctest import master
from tkinter import StringVar, ttk


class FileSelector:

	_BUTTON_LABEL = "Browse..."

	_Path = None

	def Add(self, parentframe: ttk.Frame, atgridrow, atgridcolumn):
		parentframe.grid_columnconfigure(atgridcolumn, weight=1)
		self._Path = StringVar()
		ttk.Entry(parentframe, textvariable=self._Path, width=50).grid(column=atgridcolumn, row=atgridrow, sticky="news")
		ttk.Button(parentframe, text=self._BUTTON_LABEL).grid(column=atgridcolumn + 1, row=atgridrow)
		return self
