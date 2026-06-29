from tkinter import StringVar, ttk


class FileSelector:

    _BUTTON_LABEL = "Browse..."

    _Path = None

    def Add(self, parentgrid, row, col):
        self._Path = StringVar()
        ttk.Entry(parentgrid, textvariable=self._Path, width=50).grid(
            column=col, row=row, sticky="news"
        )
        ttk.Button(parentgrid, text=self._BUTTON_LABEL).grid(
            column=col + 1, row=row
        )
        return self
