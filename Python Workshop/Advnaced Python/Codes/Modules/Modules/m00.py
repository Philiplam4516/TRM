'''
practice with modules and packages 
'''
import numpy as np 
import torch

def main():
	data_numpy = np.ones((1,3))
	print(type(data_numpy))

	data_pytorch = torch.ones(1,3)
	print(type(data_pytorch))

main()





