from tkinter import BooleanVar, ttk


class PathsTreeView:

	_DISPLAYED_COLUMNS = ("line", "checked", "path")

	def Add(self, parentgrid: ttk.Frame, row, col, colspan):
		treeview = ttk.Treeview(
			parentgrid,
			columns=self._DISPLAYED_COLUMNS,
			displaycolumns=self._DISPLAYED_COLUMNS,
			show="tree",
			selectmode="none"
			)

		treeview.column("#0", width=24, stretch=False)		
		treeview.heading("line", text="")
		treeview.column("line", minwidth=48, width=48, stretch=False, anchor="w")
		treeview.heading("checked", text="☐")
		treeview.column("checked", minwidth=24, width=24, stretch=False, anchor="center")
		treeview.heading("path", text="Path")
		treeview.column("path", minwidth=128, width=128, anchor="w")

		treeview.grid(row=row, column=col, columnspan=colspan, sticky="news")

		# Temp test rows
		treeview.insert('', index=0, iid=1, values=(1, "☐", "path 1"))
		treeview.insert('', index=1, iid=2, values=(2, "☑", "path 2"), open=True)
		treeview.insert('', index=2, iid=3, values=(3, "☑", "  path 3"))
		
		return self
