from random import randint

class Network():
	def __init__(self):
		self.inputs = [0 for i in range(49)]
		self.outputs = [0 for i in range(49)]
		self.threshold = [0 for i in range(49)]
		self.weights = [[0 for i in range(49)] for j in range(49)]
		self.start = True

	def read_matrix(self, matrix):
		for i in range(7):
			for j in range(7):
				self.inputs[i*7+j] = matrix[i][j]

	def get_matrix(self):
		matrix = [[0 for i in range(7)] for j in range(7)]
		for i in range(7):
			for j in range(7):
				matrix[i][j] = self.outputs[i*7+j]
		return matrix

	def set_weights(self):
		for i in range(49):
			for j in range(49):
				if i != j:
					self.weights[i][j] += (self.inputs[i]*self.inputs[j])

	def set_input(self):
		for i in range(49):
			self.outputs[i] = self.inputs[i]

	def async_iteration(self, i):
		sum = 0
		for j in range(49):
			sum += self.weights[i][j]*self.outputs[j]
		if sum != self.threshold[i]:
			if sum > self.threshold[i]:
				out = 1
			if sum < self.threshold[i]:
				out = -1
			if out != self.outputs[i]:
				self.outputs[i] = out

	def run_async(self, iterations):
		if self.start:
			self.set_input()
			self.start = False
		for i in range(iterations):
			r = randint(0, 48)
			self.async_iteration(r)

	def sync_iteration(self):
		outputs = [0 for i in range(49)]
		for i in range(49):
			sum = 0
			for j in range(49):
				sum += self.weights[i][j]*self.outputs[j]
			if sum != self.threshold[i]:
				if sum > self.threshold[i]:
					out = 1
				if sum < self.threshold[i]:
					out = -1
				outputs[i] = out
		for i in range(49):
			self.outputs[i] = outputs[i]

	def run_sync(self):	
		if self.start:
			self.set_input()
			self.start = False
		self.sync_iteration()

	def reset(self):
		self.__init__()

	def energy(self, vector):
		sum = 0
		for i in range(49):
			for j in range(49):
				sum += self.weights[i][j]*vector[i]*vector[j]
		return 0.5*sum

	def calcEnergy(self):
		return (self.energy(self.inputs), self.energy(self.outputs))