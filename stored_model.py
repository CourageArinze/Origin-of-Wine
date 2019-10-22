from origin import testset, testsettarget
import pandas
from sklearn import model_selection
from sklearn import datasets, metrics
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

# load the model from disk
filename = 'finalized_model.sav'
loaded_model = joblib.load(filename)

#predict using the learnt classifier
predictions = loaded_model.predict(testset)
#loaded_model.score(testset, testsettarget)

print("############### Predictions #################")
print(predictions)
print("#############################################")

print("Accuracy = ",metrics.accuracy_score(testsettarget, predictions, normalize=True))

print(metrics.classification_report(testsettarget, predictions))

print(metrics.confusion_matrix(testsettarget, predictions))
#result = loaded_model.score(X_test, Y_test)

