from tkinter import ttk


class PathsTreeView:

	def Add(self, parentgrid: ttk.Frame, row, col, colspan):
		treeview = ttk.Treeview(parentgrid)
		treeview.grid(row=row, column=col, columnspan=colspan, sticky="news")
		# treeview.insert('', '0', 'item2', text ='Computer Science')
		# treeview.insert('', '1', 'item3', 
		# 				text ='GATE papers')
		# treeview.insert('', 'end', 'item4',
		# 				text ='Programming Languages')
		# treeview.move('item3', 'item2', 'end')
		# treeview.move('item4', 'item2', 'end')
		return self
