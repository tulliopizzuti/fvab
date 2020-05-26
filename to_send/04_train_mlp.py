from os.path import join
import pandas as pd
from sklearn.neural_network import MLPClassifier
import joblib

import numpy as np

fileName = 'JoinSensorsTrain.csv'
mainPath = '/home/tullio/Projects/fvab_dataset/joined_dataset100'
trainFilePath = join(mainPath, fileName)


nEpoque=7
for e in range(0,nEpoque):
    k=e+1
    clfSaveName = 'clf_'+str(k)+'.sav'
    clfSavePath = join(mainPath, clfSaveName)
    chunksize = 10 ** k
    i = 0
    mlp = MLPClassifier(random_state=0, verbose=True)
    for chunk in pd.read_csv(trainFilePath, chunksize=chunksize, index_col=False, iterator=True):
        y = chunk[["GestureScenario"]]
        x = chunk[["XAcc", "YAcc", "ZAcc", "XGyro", "YGyro", "ZGyro", "XMagn", "YMagn", "ZMagn"]]
        mlp.partial_fit(x.to_numpy(),y.values.ravel(),classes=[1,2])
        i+=1
        print("E: "+str(k)+" - Chunk: "+str(i))
    joblib.dump(mlp, clfSavePath)