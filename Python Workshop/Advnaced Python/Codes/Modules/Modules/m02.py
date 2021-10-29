'''
practice with modules and packages 
'''
import numpy as np 
import matplotlib.pyplot as plt

def main():

	pos_samples = np.random.randn(2,100) + 2
	neg_samples = np.random.randn(2,100) + 0



	fig, ax = plt.subplots()
	ax.plot(pos_samples[0,:], pos_samples[1,:], \
			'ks', label='positive samples')
	ax.plot(neg_samples[0,:], neg_samples[1,:], \
			'r*', label='negative samples')
	legend = ax.legend(loc='upper left', \
			shadow=True, fontsize='x-large')

	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('demonstration of plt')
	plt.show()
	return

main()

