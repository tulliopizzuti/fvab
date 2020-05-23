import pandas as pd
from os.path import  join
mainPath='/home/tullio/Projects/fvab_dataset/joined_dataset100'
fileNameTest='JoinSensorsTest.csv'
fileNameTrain='JoinSensorsTrain.csv'
filePathTest=join(mainPath,fileNameTest)
filePathTrain=join(mainPath,fileNameTrain)
chunksize = 10 ** 5
totalSit=0
totalWalk=0
for chunk in pd.read_csv(filePathTrain, chunksize=chunksize):
    totalSit+=chunk[chunk.GestureScenario==1].shape[0]
    totalWalk+=chunk[chunk.GestureScenario==2].shape[0]

print("Train - Sit: "+str(totalSit)+" - Walk: "+str(totalWalk))
totalSit=0
totalWalk=0
for chunk in pd.read_csv(filePathTest, chunksize=chunksize):
    totalSit+=chunk[chunk.GestureScenario==1].shape[0]
    totalWalk+=chunk[chunk.GestureScenario==2].shape[0]

print("Test - Sit: "+str(totalSit)+" - Walk: "+str(totalWalk))

'''
Train - Sit: 39974301 - Walk: 42925699
Test  - Sit: 17380534 - Walk: 18139654
             57354835         61065353
             48%                52%
'''