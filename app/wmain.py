from tkinter import Tk, ttk
from pathstreeview import PathsTreeView
from fileselector import FileSelector


class MainWidget:

	_FILE_SELECTORS_ROW = 0
	_WINDOW_TITLE = "Sort Me Stuff"

	_FileSelectorLeft: FileSelector = None
	_FileSelectorRight: FileSelector = None
	_Frame = None
	_PathTreeviewLeft: PathsTreeView = None
	_PathTreeviewRight: PathsTreeView = None
	_ScanButton = None
	_Window = None

	def display(self, width, height):
		self._buildwindow()
		self._buildframe(width=width, height=height)
		# Define UI rows' behavior
		self._Frame.rowconfigure(1, weight=1)
		# File Selectors
		self._FileSelectorLeft = FileSelector().Add(self._Frame, self._FILE_SELECTORS_ROW, 0)
		self._FileSelectorRight = FileSelector().Add(self._Frame, self._FILE_SELECTORS_ROW, 3)
		# Scan Button
		self._ScanButton = ttk.Button(self._Frame, text="Compare").grid(column=2, row=0)
		# TreeViews
		self._PathTreeviewLeft = PathsTreeView().Add(self._Frame, 1, 0, 2)
		self._PathTreeviewRight = PathsTreeView().Add(self._Frame, 1, 3, 2)

	def mainloop(self):
		if self._Window == None:
			raise AttributeError(
				"MainWidget is not displayed, so mainloop() cannot be invoked"
			)
		self._Window.mainloop()
		
	def _buildframe(self, width, height):
		self._Frame = ttk.Frame(
			self._Window,
			height=height,
			padding=8,
			width=width,
		)
		self._Frame.grid(row=0, column=0, sticky="news")

	def _buildwindow(self):
		self._Window = Tk()
		self._Window.title(self._WINDOW_TITLE)
		self._Window.columnconfigure(0, weight=1)
		self._Window.grid_rowconfigure(0, weight=1)
	