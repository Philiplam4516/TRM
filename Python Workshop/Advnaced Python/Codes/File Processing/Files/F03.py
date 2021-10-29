'''
save and load numpy data to/from a npy file
'''

from scipy.io import savemat, loadmat
import numpy as np

def main():
	num = 5
	array = np.random.randn(1, num) # generate gaussian noises 

	#write data to a text file
	with open('data.txt', 'w') as f:
		for idx in range(num):
			f.write(str(array[0,idx])+ '\n')

	#read data from a text file
	data = []
	with open('data.txt', 'r') as f:
		while True:
			line = f.readline() # return a string 
			if not line:   # check if it is an empty string
				break
			data.append(float(line))

	print('original data: ',array)
	print('obtained data: ', data)

main()



