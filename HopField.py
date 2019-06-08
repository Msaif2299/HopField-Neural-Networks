from Buttons import *
from Processor import *
import numpy as np
import wx

class MyFrame(wx.Frame):
	def __init__(self, parent, title):
		super().__init__(parent, title=title, size=(1450,650))
		panel = MyPanel(self)
		self.Bind(wx.EVT_CLOSE, self.onClose)

	def onClose(self, event):
		self.Destroy()

class MyButton(wx.Button):
	def __init__(self, panel):
		super().__init__(panel, label='', size=(80, 80))
		self.value = 0
		self.SetBackgroundColour('white')
		self.Bind(wx.EVT_LEFT_DOWN, self.onClick)

	def onClick(self, event):
		if self.value == 1:
			self.value = -1
			self.SetBackgroundColour('white')
		else:
			self.value = 1
			self.SetBackgroundColour('blue')

	def getVal(self):
		return self.value

	def setVal(self, value):
		self.value = value
		if value == 1:
			self.SetBackgroundColour('blue')
		else:
			self.SetBackgroundColour('white')

class MyPanel(wx.Panel):
	def __init__(self, parent):
		super().__init__(parent)
		self.matrix = []
		gridSizer = wx.GridSizer(7, 7, 0, 0)
		for i in range(7):
			temp = []
			for j in range(7):
				temp.append(MyButton(self))
				gridSizer.Add(temp[j], 0, wx.ALL)
			self.matrix.append(temp)
		new_sizer = wx.BoxSizer(wx.VERTICAL)
		new_sizer.Add(gridSizer, 0, wx.ALL, 5)
		self.secondMatrix = []
		gridSizer = wx.GridSizer(7,7,0,0)
		for i in range(7):
			temp = []
			for j in range(7):
				temp.append(MyButton(self))
				gridSizer.Add(temp[j], 0, wx.ALL)
			self.secondMatrix.append(temp)
		second_new_sizer = wx.BoxSizer(wx.VERTICAL)
		second_new_sizer.Add(gridSizer, 0, wx.ALL, 5)
		self.learn = LearnButton(self, (250, 570))
		main_sizer = wx.BoxSizer(wx.HORIZONTAL)
		main_sizer.Add(new_sizer, 0, wx.RIGHT, 300)
		main_sizer.Add(second_new_sizer, 0, wx.ALIGN_RIGHT, 5)
		self.SetSizerAndFit(main_sizer)
		self.clear = ClearButton(self, (675, 150))
		self.restart = RestartButton(self, (675, 175))
		self.runasync10 = RunAsync10(self, (675, 225))
		self.runasync100 = RunAsync100(self, (672, 250))
		self.runasync1000 = RunAsync1000(self, (669, 275))
		self.runsync = RunSync(self, (675, 325))
		self.energy1 = wx.StaticText(self, pos=(400, 575))
		self.energy1.SetLabel('Energy: 0.0')
		self.energy2 = wx.StaticText(self, pos=(1050, 575))
		self.energy2.SetLabel('Energy: 0.0')
		self.network = Network()

	def get_matrix(self, buttonGrid):
		matrix = [[0 for i in range(7)] for j in range(7)]
		for i in range(7):
			for j in range(7):
				matrix[i][j] = buttonGrid[i][j].getVal()
		return matrix

	def set_matrix(self, buttonGrid, matrix):
		for i in range(7):
			for j in range(7):
				buttonGrid[i][j].setVal(matrix[i][j])

	def clear_button_grid(self, buttonGrid):
		for i in range(7):
			for j in range(7):
				buttonGrid[i][j].setVal(-1)

def print_matrix(matrix):
	for i in range(len(matrix)):
		string = ''
		for j in range(len(matrix)):
			string += str(1 if matrix[i][j] == 1 else 0) + ' '
		print(string)

class LearnButton(wx.Button):
	def __init__(self, panel, pos):
		super().__init__(panel, label="Learn", pos=pos)
		self.panel = panel
		self.Bind(wx.EVT_BUTTON, self.onClick)

	def calcEnergy(self):
		energy1, energy2 = self.panel.network.calcEnergy()
		self.panel.energy1.SetLabel('Energy: '+str(energy1+0))
		self.panel.energy2.SetLabel('Energy: '+str(energy2+0))

	def onClick(self, event):
		self.panel.network.read_matrix(self.panel.get_matrix(self.panel.matrix))
		self.panel.network.set_weights()
		self.calcEnergy()
		

class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(parent=None, title='HopField Network')
		self.frame.Show()
		return True

if __name__ == '__main__':
	app = MyApp()
	app.MainLoop()