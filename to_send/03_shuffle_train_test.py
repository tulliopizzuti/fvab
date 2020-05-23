import pandas as pd
from os.path import  join
mainPath='/home/tullio/Projects/fvab_dataset/joined_dataset100'
fileName='JoinSensors.csv'
trainFileName='JoinSensorsTrain.csv'
testFileName='JoinSensorsTest.csv'
from sklearn.utils import shuffle

filePath=join(mainPath,fileName)
trainFilePath=join(mainPath,trainFileName)
testFilePath=join(mainPath,testFileName)

chunksize = 10 ** 5
printHead=True
chunkTrain=829
for chunk in pd.read_csv(filePath, chunksize=chunksize):
    if chunkTrain > 0 :

    else


