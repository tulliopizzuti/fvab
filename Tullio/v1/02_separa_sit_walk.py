import os
from os.path import join
from os import path
import pandas as pd

joinedFile = "JoinSensors.csv"
mainPath = "/home/tullio/Projects/fvab_dataset/2"
fileSit = "JoinSensorsSit.csv"
fileWalk = "JoinSensorsWalk.csv"
filePathJoin=join(mainPath,joinedFile)
filePathSit=join(mainPath,fileSit)
filePathWalk=join(mainPath,fileWalk)

if path.exists(filePathSit): os.remove(filePathSit)
if path.exists(filePathWalk): os.remove(filePathWalk)

chunksize = 10 ** 5
printHeadSit=True
printHeadWalk=True
i=0
for chunk in pd.read_csv(filePathJoin, chunksize=chunksize):
    i+=1
    sitData=chunk[chunk.GestureScenario==1]
    walkData=chunk[chunk.GestureScenario==2]
    if sitData.shape[0] > 0 :
        sitData.to_csv(filePathSit, mode='a', header=printHeadSit, index=False)
        printHeadSit=False
    if walkData.shape[0] > 0 :
        walkData.to_csv(filePathWalk, mode='a', header=printHeadWalk, index=False)
        printHeadWalk=False
    print("Chunk: "+str(i) +" - Sit: "+ str(sitData.shape[0])+" - Walk: "+str(walkData.shape[0]))
