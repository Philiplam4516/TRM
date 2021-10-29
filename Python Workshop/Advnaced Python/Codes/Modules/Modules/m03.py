'''
From https://medium.com/analytics-vidhya/simple-linear-regression-with-example-using-numpy-e7b984f0d15e
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

	# read csv file
	data = pd.read_csv('HappinessAlcoholConsumption.csv', ',',
		 usecols=['HappinessScore', 'Beer_PerCapita','Spirit_PerCapita', 'Wine_PerCapita'])

	# convert data to a numpy array 
	matrix = np.array(data.values,'float')
	print('matrix.shape = ', matrix.shape)

	# combine Beer_PerCapita, Spirit_PerCapita, Wine_PerCapita as alchol 
	matrix_after = np.array([matrix[:,0], matrix[:,1]+matrix[:,2]+matrix[:,3] ]).transpose()
	print('matrix_after.shape = ', matrix_after.shape)

	num_samples = matrix_after.shape[0]

	x = matrix_after[:,1].reshape(num_samples,1) # alchol
	y = matrix_after[:,0].reshape(num_samples,1) # HappinessScore

	x = x/(np.max(x))  # data normalisation 


	# linear regression
	X=np.concatenate((x, np.ones_like(x)), axis=1)		
	A=np.matmul(X.transpose(), X)
	b= np.matmul(y.transpose(), X).transpose()

	model = np.matmul(np.linalg.inv(A),b)
	print('model.shape ',model.shape)

	plt.plot(x,y,'bo')
	plt.plot(x,model[0]*x+model[1],'r')
	
	plt.ylabel('Happiness Score')
	plt.xlabel('Alcohol consumption')
	plt.legend(['Happiness Score', 'linear model'])
	plt.title('Alcohol_Vs_Happiness')
	plt.grid()
	plt.show()	

	return

main()

