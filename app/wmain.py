from tkinter import Tk, ttk
from app.pathstreeview import PathsTreeView
from file_selector import FileSelector


class MainWidget:

	__FILE_SELECTORS_ROW = 0
	__WINDOW_TITLE = "Sort Me Stuff"

	__file_selector_left: FileSelector = None
	__file_selector_right: FileSelector = None
	__frame = None
	__path_treeview_left: PathsTreeView = None
	__path_treeview_Right: PathsTreeView = None
	__scan_button = None
	__window = None

	def display(self, width, height):
		self.__buildwindow()
		self.__buildframe(width=width, height=height)
		# Define UI rows' behavior
		self.__frame.rowconfigure(1, weight=1)
		# File Selectors
		self.__file_selector_left = FileSelector().add(self.__frame, self.__FILE_SELECTORS_ROW, 0)
		self.__file_selector_right = FileSelector().add(self.__frame, self.__FILE_SELECTORS_ROW, 3)
		# Scan Button
		self.__scan_button = ttk.Button(self.__frame, text="Compare").grid(column=2, row=0)
		# TreeViews
		self.__path_treeview_left = PathsTreeView().add(self.__frame, 1, 0, 2)
		self.__path_treeview_right = PathsTreeView().add(self.__frame, 1, 3, 2)

	def mainloop(self):
		if self.__window == None:
			raise AttributeError(
				"MainWidget is not displayed, so mainloop() cannot be invoked"
			)
		self.__window.mainloop()
		
	def __buildframe(self, width, height):
		self.__frame = ttk.Frame(
			self.__window,
			height=height,
			padding=8,
			width=width,
		)
		self.__frame.grid(row=0, column=0, sticky="news")

	def __buildwindow(self):
		self.__window = Tk()
		self.__window.title(self.__WINDOW_TITLE)
		self.__window.columnconfigure(0, weight=1)
		self.__window.grid_rowconfigure(0, weight=1)
	