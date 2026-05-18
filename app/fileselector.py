from tkinter import StringVar, ttk


class FileSelector:

    _BUTTON_LABEL = "Browse..."

    _Path = None

    def Add(self, parentframe, at_row, at_col):
        parentframe.grid_columnconfigure(at_col, weight=1)
        self._Path = StringVar()
        ttk.Entry(parentframe, textvariable=self._Path, width=50).grid(
            column=at_col, row=at_row, sticky="news"
        )
        ttk.Button(parentframe, text=self._BUTTON_LABEL).grid(
            column=at_col + 1, row=at_row
        )
        return self
