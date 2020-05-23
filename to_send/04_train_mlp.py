from os.path import join
import pandas as pd
from sklearn.neural_network import MLPClassifier
import joblib

import numpy as np

fileName = 'JoinSensorsTrain.csv'
mainPath = '/home/tullio/Projects/fvab_dataset/joined_dataset100'
clfSaveName='clf.sav'
trainFilePath = join(mainPath, fileName)
clfSavePath = join(mainPath, clfSaveName)
chunksize = 10 ** 4
i=0

mlp = MLPClassifier(random_state=0, verbose=True)
for chunk in pd.read_csv(trainFilePath, chunksize=chunksize, index_col=False, iterator=True):
    y = chunk[["GestureScenario"]]
    x = chunk[["XAcc", "YAcc", "ZAcc", "XGyro", "YGyro", "ZGyro", "XMagn", "YMagn", "ZMagn"]]
    mlp.partial_fit(x.to_numpy(),y.values.ravel())
    i+=1
    print("Chunk: "+str(i))
joblib.dump(mlp, clfSavePath)