from Processor import *

def print_matrix(matrix):
	for i in range(len(matrix)):
		string = ''
		for j in range(len(matrix)):
			string += str(1 if matrix[i][j] == 1 else 0) + ' '
		print(string)


nn = Network()
a = [
[ 1, 1, 1, 1, 1, 1, 1],
[-1,-1,-1, 1,-1,-1,-1],
[-1,-1,-1, 1,-1,-1,-1],
[-1,-1,-1, 1,-1,-1,-1],
[-1,-1,-1, 1,-1,-1,-1],
[-1,-1,-1, 1,-1,-1,-1],
[-1,-1,-1, 1,-1,-1,-1]]

b = [
[ 1,-1,-1,-1,-1,-1, 1],
[-1, 1,-1,-1,-1, 1,-1],
[-1,-1, 1,-1, 1,-1,-1],
[-1,-1,-1, 1,-1,-1,-1],
[-1,-1, 1,-1, 1,-1,-1],
[-1, 1,-1,-1,-1, 1,-1],
[ 1,-1,-1,-1,-1,-1, 1]]

c = [
[ 1, 1, 1,-1, 1, 1, 1],
[-1,-1,-1, 1,-1,-1,-1],
[-1,-1,-1, 1, 1,-1,-1],
[-1,-1,-1, 1,-1,-1,-1],
[-1,-1,-1, 1,-1,-1,-1],
[-1,-1, 1, 1,-1,-1,-1],
[-1,-1,-1, 1,-1,-1,-1]]

d = [
[ 1,-1,-1,-1,-1,-1, 1],
[-1,-1,-1,-1,-1,-1,-1],
[-1,-1, 1,-1, 1,-1,-1],
[-1,-1,-1, 1, 1,-1,-1],
[-1,-1, 1,-1, 1,-1,-1],
[-1, 1,-1,-1,-1, 1,-1],
[-1,-1,-1,-1,-1,-1, 1]]

e = [
[ 1,-1,-1,-1,-1,-1, 1],
[ 1,-1,-1,-1,-1,-1, 1],
[ 1,-1,-1,-1,-1,-1, 1],
[ 1, 1, 1, 1, 1, 1, 1],
[ 1,-1,-1,-1,-1,-1, 1],
[ 1,-1,-1,-1,-1,-1, 1],
[ 1,-1,-1,-1,-1,-1, 1]]

f = [
[ 1,-1,-1,-1,-1,-1, 1],
[-1,-1,-1,-1,-1,-1,-1],
[ 1,-1,-1,-1,-1,-1, 1],
[ 1, 1, 1,-1, 1, 1, 1],
[ 1,-1,-1,-1,-1,-1, 1],
[ 1, 1,-1,-1,-1,-1,-1],
[-1,-1,-1, 1,-1,-1, 1]]

nn.read_matrix(a)
nn.set_weights()
nn.read_matrix(b)
nn.set_weights()
nn.read_matrix(e)
nn.set_weights()
nn.read_matrix(c)
nn.set_input()
nn.run_async(1000)
print_matrix(nn.get_matrix())