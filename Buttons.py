import numpy as np
import wx
import random
from Processor import *

trigger = True

class ClearButton(wx.Button):
	def __init__(self, panel, pos):
		self.panel = panel
		super().__init__(panel, label='Clear', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)

	def onClick(self, event):
		self.panel.clear_button_grid(self.panel.secondMatrix)
		self.panel.clear_button_grid(self.panel.matrix)
		self.panel.network.start = True

class RestartButton(wx.Button):
	def __init__(self, panel, pos):
		self.panel = panel
		super().__init__(panel, label='Restart', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)

	def onClick(self, event):
		self.panel.clear_button_grid(self.panel.secondMatrix)
		self.panel.clear_button_grid(self.panel.matrix)
		self.panel.network.reset()

def print_matrix(matrix):
	for i in range(len(matrix)):
		string = ''
		for j in range(len(matrix)):
			string += str(1 if matrix[i][j] == 1 else 0) + ' '
		print(string)

def print_vector(vector):
	temp = [[0 for i in range(7)] for j in range(7)]
	for i in range(7):
		for j in range(7):
			temp[i][j] = vector[i*7+j]
	print_matrix(temp)

class RunAsync10(wx.Button): #This needs a complete rework, it is messing with the learnt parameters, need to make its own versions of things and pass it between the other classes
	def __init__(self, panel, pos):
		super().__init__(panel, label='Run Async 10', pos=pos)
		self.panel = panel
		self.Bind(wx.EVT_BUTTON, self.onClick)

	def onClick(self, event):
		global trigger
		if trigger:
			self.panel.set_matrix(self.panel.secondMatrix, self.panel.get_matrix(self.panel.matrix))
			trigger = False
		self.panel.network.read_matrix(self.panel.get_matrix(self.panel.secondMatrix))
		self.panel.network.set_input()
		self.panel.network.run_async(10)
		self.panel.set_matrix(self.panel.secondMatrix, self.panel.network.get_matrix())'''
		self.panel.network.read_matrix(self.panel.get_matrix(self.panel.matrix))
		print_matrix(self.panel.get_matrix(self.panel.matrix))
		self.panel.network.set_input()
		print_vector(self.panel.network.inputs)
		print_vector(self.panel.network.outputs)
		self.panel.network.run_async(1000)
		self.panel.set_matrix(self.panel.secondMatrix, self.panel.network.get_matrix())'''

class RunAsync100(wx.Button):
	def __init__(self, panel, pos):
		super().__init__(panel, label='Run Async 100', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)
		self.panel = panel

	def onClick(self, event):
		global trigger
		if trigger:
			self.panel.set_matrix(self.panel.secondMatrix, self.panel.get_matrix(self.panel.matrix))
			trigger = False
		self.panel.network.read_matrix(self.panel.get_matrix(self.panel.secondMatrix))
		self.panel.network.set_input()
		self.panel.network.run_async(100)
		self.panel.set_matrix(self.panel.secondMatrix, self.panel.network.get_matrix())

class RunAsync1000(wx.Button):
	def __init__(self, panel, pos):
		super().__init__(panel, label='Run Async 1000', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)
		self.panel = panel

	def onClick(self, event):
		global trigger
		if trigger:
			self.panel.set_matrix(self.panel.secondMatrix, self.panel.get_matrix(self.panel.matrix))
			trigger = False
		self.panel.network.read_matrix(self.panel.get_matrix(self.panel.secondMatrix))
		self.panel.network.set_input()
		self.panel.network.run_async(1000)
		self.panel.set_matrix(self.panel.secondMatrix, self.panel.network.get_matrix())


class RunSync(wx.Button):
	def __init__(self, panel, pos):
		super().__init__(panel, label='Run Sync', pos=pos)
		self.Bind(wx.EVT_BUTTON, self.onClick)
		self.panel = panel

	def onClick(self, event):
		global trigger
		if trigger:
			self.panel.set_matrix(self.panel.secondMatrix, self.panel.get_matrix(self.panel.matrix))
			trigger = False
		self.panel.network.read_matrix(self.panel.get_matrix(self.panel.secondMatrix))
		self.panel.network.set_input()
		self.panel.network.run_sync()
		self.panel.set_matrix(self.panel.secondMatrix, self.panel.network.get_matrix())