import pandas as pd 
import numpy as np 

def df1(dframe,featurelist):
    
    for feature in featurelist:
        if feature not in list(dframe):
            raise ValueError('feature not in featurelist')

    return dframe.drop(columns=[feature for feature in list(dframe) if feature in featurelist],axis=1)

harray = np.ones((5,4))
g = ['a','b','c','d']

h = pd.DataFrame(harray,columns=g,dtype='float64')

print(df1(h,['a','b','p']))