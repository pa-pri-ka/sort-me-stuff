from enum import Enum
from tkinter import ttk

from app.actionbutton import ActionButton


class MidSectionActions:

    class Action(Enum):
        COPY_LEFT = "copyleft"
        COPY_RIGHT = "copyright"
        MOVE_LEFT = "moveleft"
        MOVE_RIGHT = "moveright"
        DELETE_LEFT = "deleteleft"
        DELETE_RIGHT = "deleteright"

    def __init__(self, parentframe, row, col):
        self._col = col
        self._parentframe = parentframe
        self._row = row
        self._build()

    _ActionButtons = {}

    def _build(self):
        leftcol = ttk.Frame(self._parentframe)
        leftcol.grid(row=self._row, column=self._col, sticky="news")
        self._ActionButtons[self.Action.MOVE_LEFT] = ActionButton(
            "Move Left Items To Right Path",
            "Moves the items selected in the left root folder to the same path than the matching items shown on the right. If the path is missing in the left root folder, it will be created.",
        ).Add(leftcol)
        self._ActionButtons[self.Action.COPY_LEFT] = ActionButton(
            "Copy Left Items To Right Path",
            "Copies the items selected in the left root folder to the same path than the matching items shown in the right folder. If the path is missing in the left root folder, it will be created.",
        ).Add(leftcol, 1)
        self._ActionButtons[self.Action.DELETE_LEFT] = ActionButton(
            "Delete From Left", "Deletes the items selected in the left root folder."
        ).Add(leftcol, 2)

        rightcol = ttk.Frame(self._parentframe)
        rightcol.grid(row=self._row, column=self._col + 1, sticky="news")
        rightcol.rowconfigure(0, weight=1)
        spacer = ttk.Frame(rightcol)
        spacer.grid(sticky="news")
        self._ActionButtons[self.Action.MOVE_RIGHT] = ActionButton(
            "Move Right Items To Left Path",
            "Moves the items selected in the right root folder to the same path than the matching items shown on the left. If the path is missing in the right root folder, it will be created.",
        ).Add(rightcol, 1)
        self._ActionButtons[self.Action.COPY_RIGHT] = ActionButton(
            "Copy Left Items To Right Path",
            "Copies the items selected in the right root folder to the same path than the matching items shown in the left folder. If the path is missing in the right root folder, it will be created.",
        ).Add(rightcol, 2)
        self._ActionButtons[self.Action.DELETE_RIGHT] = ActionButton(
            "Delete From Right", "Deletes the items selected in the right root folder."
        ).Add(rightcol, 3)
        print()