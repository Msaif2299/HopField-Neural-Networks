import numpy as np
import wx
import random
from Processor import *

m = Matrix()

class ClearButton(wx.Button):
	def __init__(self, panel, pos):
		self.panel = panel
		super().__init__(panel, label='Clear', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)

	def onClick(self, event):
		for i in range(7):
			for j in range(7):
				self.panel.matrix[i][j].setVal(0)
				self.panel.secondMatrix[i][j].setVal(0)
		m.reset()

class RestartButton(wx.Button):
	def __init__(self, panel, pos):
		self.panel = panel
		super().__init__(panel, label='Restart', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)

	def onClick(self, event):
		for i in range(7):
			for j in range(7):
				self.panel.matrix[i][j].setVal(0)
				self.panel.learn.matrix[i][j] = 0
				self.panel.secondMatrix[i][j].setVal(0)
		for i in range(49):
			for j in range(49):
				self.panel.learn.unwinded_matrix[i][j] = 0
		for i in range(49):
			self.panel.learn.unwinded_vector[i] = 0
		m.reset()


class RunAsync10(wx.Button): #This needs a complete rework, it is messing with the learnt parameters, need to make its own versions of things and pass it between the other classes
	def __init__(self, panel, pos):
		super().__init__(panel, label='Run Async 10', pos=pos)
		self.panel = panel
		self.Bind(wx.EVT_BUTTON, self.onClick)

	def onClick(self, event):
		m.input(self.panel)
		m.runAsync(self.panel, 10)

class RunAsync100(wx.Button):
	def __init__(self, panel, pos):
		super().__init__(panel, label='Run Async 100', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)
		self.panel = panel

	def onClick(self, event):
		m.input(self.panel)
		m.runAsync(self.panel, 100)

class RunAsync1000(wx.Button):
	def __init__(self, panel, pos):
		super().__init__(panel, label='Run Async 1000', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)
		self.panel = panel

	def onClick(self, event):
		m.input(self.panel)
		m.runAsync(self.panel, 1000)


class RunSync(wx.Button):
	def __init__(self, panel, pos):
		super().__init__(panel, label='Run Sync', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)
		self.panel = panel

	def onClick(self, event):
		m.input(self.panel)
		m.runSync(self.panel)