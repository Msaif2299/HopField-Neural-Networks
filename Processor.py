import wx
import numpy as np
import random

class Matrix():
	def __init__(self):
		self.matrix = [[0 for i in range(7)] for j in range(7)]
		self.trigger = True
		self.vector = [0 for i in range(49)]

	def input(self, panel):
		if self.trigger:
			for i in range(7):
				for j in range(7):
					self.matrix[i][j] = panel.matrix[i][j].getVal()
			self.trigger = False
		else:
			for i in range(7):
				for j in range(7):
					self.matrix[i][j] = panel.secondMatrix[i][j].getVal()
		for i in range(7):
			for j in range(7):
				self.vector[i*7+j] = self.matrix[i][j]

	def sign(self, value):
		if value >= 0:
			return 1
		else:
			return 0

	def output(self, panel):
		for i in range(7):
			for j in range(7):
				panel.secondMatrix[i][j].setVal(self.matrix[i][j])

	def update(self):
		for i in range(49):
			self.matrix[int(i/7)][i%7] = self.vector[i]

	def runAsync(self, panel, number):
		for i in range(number):
			r = random.randint(0,48)
			temp = 0
			for j in range(49):
				if r != j:
					temp += panel.learn.unwinded_matrix[r][j]*self.vector[j]
			self.vector[r] = self.sign(temp)
		self.update()
		self.output(panel)

	def runSync(self, panel):
		vector = [0 for i in range(49)]
		for i in range(49):
			for j in range(49):
				if i != j:
					vector[i] += panel.learn.unwinded_matrix[i][j]*self.vector[j]
			vector[i] = self.sign(vector[i])
		self.vector = vector
		self.update()
		self.output(panel)

	def reset(self):
		for i in range(7):
			for j in range(7):
				self.matrix[i][j] = 0
				self.vector[i*7+j] = 0
		self.trigger = True

if __name__ == '__main__':
	a = Matrix()