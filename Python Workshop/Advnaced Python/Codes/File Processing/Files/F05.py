'''
save and load data to/from a matlab file
'''

from scipy.io import savemat, loadmat
import numpy as np

def main():
	array = np.arange(10)
	mydict = {"array": array}
	savemat("matlab.mat", mydict)

	data = loadmat("matlab.mat")

	print('original data: ',array)
	print('obtained data: ', data['array'])

main()

