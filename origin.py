#Software Engineering Project
#Origin of Wine

print("================================================================================SOFTWARE ENGINERING PROJECT=========================================================================")
print("                                                                                                                                                                                    ")
print("||                                                                                    ORIGIN OF WINE                                                                              ||")
print("                                                                                                                                                                                    ")
print("||                                                                                    ARINZE COURAGE CHINEMELUM                                                                   ||")
print("||                                                                                    SHUBHAM TIWARI                                                                              ||")
print("||                                                                                    UTKARSH SINGH                                                                               ||")
print("||                                                                                    RISHAB MALHOTRA                                                                             ||")
print("====================================================================================================================================================================================")

import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

dataset = pd.read_csv('Wine.csv')    #pd.read_excel('Wineo.xlsx')
dataset = dataset.values
#print(name)

#Independent and Dependent
independent = dataset[:,1:14]
dependent = dataset[:,0:1]

df_ind=pd.DataFrame(independent,columns=['Malic Acid','Alcohol','Ash','Alcalanity of Ash','Magnesium','Total phenols','Flavanoid','Nonflavanoid Phenol','Proanthocynins','Color Intensity','Hue','OD280/OD315 of diluted wines','Proline'])
df_d=pd.DataFrame(dependent,columns=['Class Label'])

#Training Set
trainingset = independent[range(0,176,2),:]
trainingsettarget = dependent[range(0,176,2)]
trainingsettarget = np.ravel(trainingsettarget)

#Test Set
testset = independent[range(1,177,2),:]
testsettarget = dependent[range(1,177,2)]
testsettarget = np.ravel(testsettarget)

clf = LogisticRegression(multi_class='ovr') #creating instance of a classifier #default criterion is gini
clf.fit(trainingset, trainingsettarget)

# Store model in Disk
filename = 'finalized_model.sav'
joblib.dump(clf, filename)




                

