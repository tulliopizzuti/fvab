import os
from os.path import join
from os import path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

mainPath = "/home/tullio/Projects/fvab_dataset/2"
fileMeanSensors = "MeanSensors.csv"
filePathMeanSensors=join(mainPath,fileMeanSensors)
scaler = StandardScaler()
sensors=pd.read_csv(filePathMeanSensors)
y=sensors["GestureScenario"]
X=sensors[["XAcc", "YAcc", "ZAcc", "XGyro", "YGyro", "ZGyro", "XMagn", "YMagn", "ZMagn"]]
#X=scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=0)


mlp = MLPClassifier(
    random_state=0, verbose=True).fit(X_train,y_train)
print(mlp.score(X_test,y_test))
