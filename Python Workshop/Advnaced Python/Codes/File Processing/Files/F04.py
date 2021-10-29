'''
save and load numpy data to/from a npy file
'''

from scipy.io import savemat, loadmat
import numpy as np

def main():
	array = np.random.randn(1, 5) # generate gaussian noises  

	np.save("data.npy", array)

	data = np.load("data.npy")

	print('original data: ',array)
	print('obtained data: ', data)

main()

