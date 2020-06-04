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
fileMeanSensors = "MeanSensors.csv"
filePathMeanSensors = join(mainPath, fileMeanSensors)
scaler = StandardScaler()
sensors = pd.read_csv(filePathMeanSensors)
y = sensors["GestureScenario"]
X = sensors[["XAcc", "YAcc", "ZAcc", "XGyro", "YGyro", "ZGyro", "XMagn", "YMagn", "ZMagn"]]
X = scaler.fit_transform(X)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

parameter_space = {
    'alpha': [0.0001, 0.05],
    'activation': ["logistic", "relu", "Tanh"],
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
'''
y_true, y_pred = y_test, clf.predict(X_test)

from sklearn.metrics import classification_report

print('Results on the test set:')
print(classification_report(y_true, y_pred))
'''


'''
Best parameters found:
 {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 1e-05}
0.906 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 0.0001}
0.875 (+/-0.012) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 0.001}
0.906 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 1e-05}
0.819 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 0.0001}
0.697 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 0.001}
0.819 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 1e-05}
0.921 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 0.0001}
0.914 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 0.001}
0.921 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 1e-05}
0.906 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 0.0001}
0.875 (+/-0.012) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 0.001}
0.906 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 1e-05}
0.819 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 0.0001}
0.697 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 0.001}
0.819 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 1e-05}
0.921 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 0.0001}
0.914 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 0.001}
0.921 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 1e-05}
0.906 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 0.0001}
0.875 (+/-0.012) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 0.001}
0.906 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 1e-05}
0.819 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 0.0001}
0.697 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 0.001}
0.819 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 1e-05}
0.921 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 0.0001}
0.914 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 0.001}
0.921 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 1e-05}
0.839 (+/-0.001) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 0.0001}
0.817 (+/-0.002) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 0.001}
0.846 (+/-0.010) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 1e-05}
0.798 (+/-0.002) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 0.0001}
0.696 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 0.001}
0.798 (+/-0.002) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 1e-05}
0.857 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 0.0001}
0.854 (+/-0.002) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 0.001}
0.856 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 1e-05}
0.839 (+/-0.001) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 0.0001}
0.817 (+/-0.002) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 0.001}
0.846 (+/-0.010) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 1e-05}
0.798 (+/-0.002) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 0.0001}
0.696 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 0.001}
0.798 (+/-0.002) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 1e-05}
0.857 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 0.0001}
0.854 (+/-0.002) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 0.001}
0.856 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 1e-05}
0.839 (+/-0.001) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 0.0001}
0.817 (+/-0.002) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 0.001}
0.846 (+/-0.010) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 1e-05}
0.798 (+/-0.002) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 0.0001}
0.696 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 0.001}
0.798 (+/-0.002) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 1e-05}
0.857 (+/-0.004) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 0.0001}
0.854 (+/-0.002) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 0.001}
0.856 (+/-0.003) for {'activation': 'logistic', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 1e-05}
0.911 (+/-0.004) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 0.0001}
0.896 (+/-0.006) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 0.001}
0.911 (+/-0.004) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 1e-05}
0.876 (+/-0.003) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 0.0001}
0.831 (+/-0.002) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 0.001}
0.876 (+/-0.003) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 1e-05}
0.906 (+/-0.007) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 0.0001}
0.895 (+/-0.013) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 0.001}
0.906 (+/-0.007) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 1e-05}
0.911 (+/-0.004) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 0.0001}
0.896 (+/-0.006) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 0.001}
0.911 (+/-0.004) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 1e-05}
0.876 (+/-0.003) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 0.0001}
0.831 (+/-0.002) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 0.001}
0.876 (+/-0.003) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 1e-05}
0.906 (+/-0.007) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 0.0001}
0.895 (+/-0.013) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 0.001}
0.906 (+/-0.007) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 1e-05}
0.911 (+/-0.004) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 0.0001}
0.896 (+/-0.006) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 0.001}
0.911 (+/-0.004) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 1e-05}
0.876 (+/-0.003) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 0.0001}
0.831 (+/-0.002) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 0.001}
0.876 (+/-0.003) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 1e-05}
0.906 (+/-0.007) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 0.0001}
0.895 (+/-0.013) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 0.001}
0.906 (+/-0.007) for {'activation': 'relu', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 1e-05}
0.897 (+/-0.005) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 0.0001}
0.883 (+/-0.001) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 0.001}
0.898 (+/-0.003) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 1e-05}
0.871 (+/-0.002) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 0.0001}
0.825 (+/-0.000) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 0.001}
0.871 (+/-0.002) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 1e-05}
0.882 (+/-0.003) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 0.0001}
0.885 (+/-0.001) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 0.001}
0.882 (+/-0.002) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 1e-05}
0.897 (+/-0.005) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 0.0001}
0.883 (+/-0.001) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 0.001}
0.898 (+/-0.003) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 1e-05}
0.871 (+/-0.002) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 0.0001}
0.825 (+/-0.000) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 0.001}
0.871 (+/-0.002) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 1e-05}
0.882 (+/-0.003) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 0.0001}
0.885 (+/-0.001) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 0.001}
0.882 (+/-0.002) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 1e-05}
0.897 (+/-0.005) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 0.0001}
0.883 (+/-0.001) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 0.001}
0.898 (+/-0.003) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 1e-05}
0.871 (+/-0.002) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 0.0001}
0.825 (+/-0.000) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 0.001}
0.871 (+/-0.002) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 1e-05}
0.882 (+/-0.003) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 0.0001}
0.885 (+/-0.001) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 0.001}
0.882 (+/-0.002) for {'activation': 'relu', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.0001, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.001, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.0001, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'constant', 'learning_rate_init': 0.01, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.001, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.0001, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'adaptive', 'learning_rate_init': 0.01, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.001, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.0001, 'tol': 1e-05}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 0.0001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 0.001}
nan (+/-nan) for {'activation': 'Tanh', 'alpha': 0.05, 'learning_rate': 'invscaling', 'learning_rate_init': 0.01, 'tol': 1e-05}

Process finished with exit code 0


'''