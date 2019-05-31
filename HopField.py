from Buttons import *
import numpy as np
import wx

class MyFrame(wx.Frame):
	def __init__(self, parent, title):
		super().__init__(parent, title=title, size=(1450,650))
		panel = MyPanel(self)

class MyButton(wx.Button):
	def __init__(self, panel):
		super().__init__(panel, label='', size=(80, 80))
		self.value = -1
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


class LearnButton(wx.Button):
	def __init__(self, panel, pos):
		super().__init__(panel, label="Learn", pos=pos)
		self.matrix = []
		self.panel = panel
		for i in range(7):
			temp = []
			for j in range(7):
				temp.append(0)
			self.matrix.append(temp)
		self.Bind(wx.EVT_BUTTON, self.onClick)
		self.energy = 0
		self.unwinded_matrix = [[0 for x in range(49)] for y in range(49)]
		self.unwinded_vector = []
		for i in range(7):
			for j in range(7):
				self.unwinded_vector.append(self.matrix[i][j])
	
	def calcEnergy(self):
		pass

	def onClick(self, event):
		for i in range(7):
			for j in range(7):
				self.matrix[i][j] += self.panel.matrix[i][j].getVal()
		for i in range(7):
			for j in range(7):
				self.unwinded_vector[i*7+j] = self.matrix[i][j]
		for i in range(49):
			for j in range(49):
				if i != j:
					self.unwinded_matrix[i][j] += (self.unwinded_vector[i]*self.unwinded_vector[j])
	def update(self):
		for i in range(49):
				self.matrix[int(i/7)][i%7] = self.unwinded_vector[i]
		for i in range(49):
			for j in range(49):
				if i != j:
					self.unwinded_matrix[i][j] += (self.unwinded_vector[i]*self.unwinded_vector[j])


class MyApp(wx.App):
	def OnInit(self):
		self.frame = MyFrame(parent=None, title='HopField Network')
		self.frame.Show()
		return True

if __name__ == '__main__':
	app = MyApp()
	app.MainLoop()