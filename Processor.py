import wx
import numpy as np
import random

class Matrix():
	def __init__(self):
		self.matrix = np.array([[0 for i in range(7)] for j in range(7)])
		self.trigger = True
		self.vector = np.array([self.matrix.flatten()])
		print(self.matrix.shape)
		print(self.vector.shape)


	def input(self, panel):
		print(self.trigger)
		if self.trigger:
			for i in range(7):
				for j in range(7):
					self.matrix[i][j] = panel.matrix[i][j].getVal()
			self.trigger = False
		else:
			for i in range(7):
				for j in range(7):
					self.matrix[i][j] = panel.secondMatrix[i][j].getVal()

	def sign(self, value):
		if value >= 0:
			return 1
		else:
			return -1

	def output(self, panel):
		for i in range(7):
			for j in range(7):
				panel.secondMatrix[i][j].setVal(self.matrix[i][j])

	def update(self):
		for i in range(49):
			self.matrix[int(i/7)][i%7] = self.vector[0][i]

	def runAsync(self, panel, number):
		for i in range(number):
			r = random.randint(0,48)
			temp = 0
			for j in range(49):
				temp += panel.learn.unwinded_matrix[r][j]*self.vector[0][j]
			self.vector[0][r] = self.sign(temp)
			self.update()
		self.output(panel)

	def reset(self):
		for i in range(7):
			for j in range(7):
				self.matrix[i] = 0
				self.vector[0][i*7+j] = 0
		self.trigger = True

if __name__ == '__main__':
	a = Matrix()