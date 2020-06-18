import os
from os.path import join
from os import path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np

mainPath = "/home/tullio/Projects/fvab_dataset/2"
fileMeanSensors = "MeanSensors2.csv"
filePathMeanSensors = join(mainPath, fileMeanSensors)
scaler = StandardScaler()
sensors = pd.read_csv(filePathMeanSensors)
y = sensors["GestureScenario"]
X = sensors[["XAcc", "YAcc", "ZAcc", "XGyro", "YGyro", "ZGyro", "XMagn", "YMagn", "ZMagn"]]
X = scaler.fit_transform(X)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

parameter_space = {
    'alpha': [0.0001, 0.05],
    'activation': ["logistic", "relu", "tanh"],
    'learning_rate': ['constant', 'adaptive', 'invscaling'],
    'learning_rate_init': [0.001, 0.0001, 0.01],
    'tol': [1e-4, 1e-3, 1e-5]
}
mlp = MLPClassifier(
    random_state=0, max_iter=300)
clf = GridSearchCV(mlp, parameter_space, n_jobs=-1, cv=3, verbose=5)
clf.fit(X, y)
print('Best parameters found:\n', clf.best_params_)

means = clf.cv_results_['mean_test_score']
stds = clf.cv_results_['std_test_score']
for mean, std, params in zip(means, stds, clf.cv_results_['params']):
    print("%0.3f (+/-%0.03f) for %r" % (mean, std * 2, params))
