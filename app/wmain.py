from tkinter import Tk, ttk
from file_selector import FileSelector


class MainWidget:

	__FILE_SELECTORS_ROW = 0
	__WINDOW_TITLE = "Sort Me Stuff"

	__file_selector_left: FileSelector = None
	__file_selector_right: FileSelector = None
	__frame = None
	__scan_button = None
	__window = None

	def display(self, width, height):
		# Main window
		window = Tk()
		window.title(self.__WINDOW_TITLE)
		self.__frame = ttk.Frame(
			window,
			height=height,
			name="main_widget",
			padding=8,
			width=width,
		)
		self.__frame.grid()
		# File Selectors
		self.__file_selector_left = FileSelector().add(self.__frame, self.__FILE_SELECTORS_ROW, 0)
		self.__file_selector_right = FileSelector().add(self.__frame, self.__FILE_SELECTORS_ROW, 3)
		# Scan Button
		self.__scan_button = ttk.Button(self.__frame, text="Compare").grid(column=2, row=0)
		# Done
		self.__window = window

	def mainloop(self):
		if self.__window == None:
			raise AttributeError(
				"MainWidget is not displayed, so mainloop() cannot be invoked"
			)
		self.__window.mainloop()
