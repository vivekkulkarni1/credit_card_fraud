import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

X = pd.read_csv('train.csv')


#

y = X['loan_default']
y1 = np.array(y)
plt.figure()
plt.hist(y1)
plt.show()
