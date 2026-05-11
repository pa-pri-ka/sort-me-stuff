from wmain import MainWidget

__INITIAL_HEIGHT = 640
__INITIAL_WIDTH = 960

__wmain:MainWidget = MainWidget()
__wmain.display(__INITIAL_WIDTH, __INITIAL_HEIGHT)

__wmain.mainloop()
