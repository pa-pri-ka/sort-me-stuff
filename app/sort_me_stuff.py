from tkinter import Tk
from wmain import MainWidget

__INITIAL_HEIGHT = 400
__INITIAL_WIDTH = 640

__wmain:Tk = MainWidget().create(__INITIAL_WIDTH, __INITIAL_HEIGHT)
__wmain.mainloop()
