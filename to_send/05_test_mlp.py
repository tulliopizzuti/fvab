from os.path import join
import pandas as pd
from sklearn.neural_network import MLPClassifier
import joblib
import numpy as np

fileName = 'JoinSensorsTest.csv'
mainPath = '/home/tullio/Projects/fvab_dataset/joined_dataset100'
clfLoadName='clf.sav'
testFilePath = join(mainPath, fileName)
clfLoadPath = join(mainPath, clfLoadName)
chunksize = 10 ** 5
i=0
tot=0
clf=joblib.load(clfLoadPath)
for chunk in pd.read_csv(testFilePath, chunksize=chunksize, index_col=False):
    y = chunk[["GestureScenario"]]
    x = chunk[["XAcc", "YAcc", "ZAcc", "XGyro", "YGyro", "ZGyro", "XMagn", "YMagn", "ZMagn"]]
    i+=1
    tot+=clf.score(x, y)
    print(str(i),clf.score(x, y))
print(str(i),str(tot),str(tot/i))