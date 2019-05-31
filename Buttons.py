import numpy as np
import wx
import random

class ClearButton(wx.Button):
	def __init__(self, panel, pos):
		self.panel = panel
		super().__init__(panel, label='Clear', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)

	def onClick(self, event):
		for i in range(7):
			for j in range(7):
				self.panel.matrix[i][j].setVal(-1)

class RestartButton(wx.Button):
	def __init__(self, panel, pos):
		self.panel = panel
		super().__init__(panel, label='Restart', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)

	def onClick(self, event):
		for i in range(7):
			for j in range(7):
				self.panel.matrix[i][j].setVal(-1)
				self.panel.learn.matrix[i][j] = 0

def sign(value):
	if value >= 0:
		return 1
	else:
		return -1

class RunAsync10(wx.Button): #This needs a complete rework, it is messing with the learnt parameters, need to make its own versions of things and pass it between the other classes
	def __init__(self, panel, pos):
		super().__init__(panel, label='Run Async 10', pos=pos)
		self.panel = panel
		self.Bind(wx.EVT_BUTTON, self.onClick)

	def onClick(self, event):
		for i in range(10):
			r = random.randint(0,48)
			temp = 0
			for j in range(49):
				try:
					temp += self.panel.learn.unwinded_matrix[r][j]*self.panel.learn.unwinded_vector[j]
				except IndexError:
					print(r)
			self.panel.learn.unwinded_vector[j] = sign(temp)
			self.panel.learn.update()
		for i in range(7):
			for j in range(7):
				self.panel.secondMatrix[i][j].setVal(self.panel.learn.matrix[i][j])

class RunAsync100(wx.Button):
	def __init__(self, panel, pos):
		super().__init__(panel, label='Run Async 100', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)

	def onClick(self, event):
		pass

class RunAsync1000(wx.Button):
	def __init__(self, panel, pos):
		super().__init__(panel, label='Run Async 1000', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)

	def onClick(self, event):
		pass

class RunSync(wx.Button):
	def __init__(self, panel, pos):
		super().__init__(panel, label='Run Sync', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)

	def onClick(self, event):
		pass