from tkinter import Tk, ttk
from app.actionbutton import ActionButton
from app.midsectionactions import MidSectionActions
from pathstreeview import PathsTreeView
from fileselector import FileSelector


class MainWidget:

    _LEFT_SECTION_COL = 0
    _MID_SECTION_COL = 2
    _RIGHT_SECTION_COL = 4

    _FILE_SELECTORS_ROW = 0
    _PATH_TREE_VIEW_ROW = 1

    _WINDOW_TITLE = "Sort Me Stuff"

    _FileSelectorLeft: FileSelector = None
    _FileSelectorRight: FileSelector = None
    _Frame = None
    _PathTreeViewLeft: PathsTreeView = None
    _PathTreeViewRight: PathsTreeView = None
    _Window = None

    def display(self, width, height):
        self._buildwindow()
        self._buildframe(width=width, height=height)
        # File Selectors
        self._buildfileselectors()
        # Path Tree Views
        self._PathTreeViewLeft = PathsTreeView().Add(
            self._Frame, row=1, col=self._LEFT_SECTION_COL, colspan=2
        )
        self._PathTreeViewRight = PathsTreeView().Add(
            self._Frame, row=1, col=self._RIGHT_SECTION_COL, colspan=2
        )
        # Compare Button
        ttk.Button(self._Frame, text="Compare").grid(
            column=self._MID_SECTION_COL,
            row=self._FILE_SELECTORS_ROW,
            columnspan=2,
            sticky="we",
        )

        # Action buttons
        MidSectionActions().Add(self._Frame, row=self._PATH_TREE_VIEW_ROW, col=self._MID_SECTION_COL)
        

    def mainloop(self):
        if self._Window == None:
            raise AttributeError(
                "MainWidget is not displayed, so mainloop() cannot be invoked"
            )
        self._Window.mainloop()

    def _buildfileselectors(self):
        self._Frame.grid_columnconfigure(self._LEFT_SECTION_COL, weight=1)
        self._FileSelectorLeft = FileSelector().Add(
            self._Frame, self._FILE_SELECTORS_ROW, self._LEFT_SECTION_COL
        )
        self._Frame.grid_columnconfigure(self._RIGHT_SECTION_COL, weight=1)
        self._FileSelectorRight = FileSelector().Add(
            self._Frame, self._FILE_SELECTORS_ROW, self._RIGHT_SECTION_COL
        )

    def _buildframe(self, width, height):
        self._Frame = ttk.Frame(
            self._Window,
            height=height,
            padding=8,
            width=width,
        )
        self._Frame.grid(row=0, column=0, sticky="news")
        self._Frame.grid_propagate(False)
        self._Frame.rowconfigure(1, weight=1)

    def _buildwindow(self):
        self._Window = Tk()
        self._Window.title(self._WINDOW_TITLE)
        self._Window.columnconfigure(0, weight=1)
        self._Window.grid_rowconfigure(0, weight=1)