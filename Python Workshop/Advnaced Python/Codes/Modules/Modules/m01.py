'''
practice with modules and packages 
'''
import numpy as np 
import matplotlib.pyplot as plt

def main():
	array_len = 200
	x = np.linspace(0, 2.0, num=array_len)
	y1 = x*x 
	y2 = x

	fig, ax = plt.subplots()
	ax.plot(x, y1, 'k--', label='quadratic')
	ax.plot(x, y2, 'b--', label='linear')
	legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')

	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('demonstration of plt')
	plt.show()
	return

main()

