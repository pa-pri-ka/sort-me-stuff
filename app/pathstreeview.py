from tkinter import Tk, ttk


class PathsTreeView:

	def Add(self, parent_frame: ttk.Frame, at_grid_row, at_grid_column, colspan):
		treeview = ttk.Treeview(parent_frame)
		treeview.grid(row=at_grid_row, column=at_grid_column, columnspan=colspan, sticky="news")
		# treeview.insert('', '0', 'item2', text ='Computer Science')
		# treeview.insert('', '1', 'item3', 
		# 				text ='GATE papers')
		# treeview.insert('', 'end', 'item4',
		# 				text ='Programming Languages')
		# treeview.move('item3', 'item2', 'end')
		# treeview.move('item4', 'item2', 'end')
		return self
