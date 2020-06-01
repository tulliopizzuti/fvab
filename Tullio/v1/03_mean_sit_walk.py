import os
from os.path import join
from os import path
import pandas as pd
mainPath = "/home/tullio/Scrivania/Projects/fvab_dataset/2"

joinedFile = "JoinSensors.csv"
filePathJoin=join(mainPath,joinedFile)

fileSit = "JoinSensorsSit.csv"
filePathSit=join(mainPath,fileSit)


fileWalk = "JoinSensorsWalk.csv"
filePathWalk=join(mainPath,fileWalk)


fileMeanSit = "MeanSensorsSit.csv"
filePathMeanSit=join(mainPath,fileMeanSit)


fileMeanWalk = "MeanSensorsWalk.csv"
filePathMeanWalk=join(mainPath,fileMeanWalk)

if path.exists(filePathMeanSit): os.remove(filePathMeanSit)
if path.exists(filePathMeanWalk): os.remove(filePathMeanWalk)

chunksize = 10 ** 3
printHeadSit=True
printHeadWalk=True

i=0
for chunk in pd.read_csv(filePathSit, chunksize=chunksize):
    i+=1
    df=(chunk.mean().to_frame().transpose())
    df.to_csv(filePathMeanSit, mode='a', header=printHeadSit, index=False)
    printHeadSit=False
    print("Sit chunk: "+str(i))


i=0
for chunk in pd.read_csv(filePathWalk, chunksize=chunksize):
    i+=1
    df=(chunk.mean().to_frame().transpose())
    df.to_csv(filePathMeanWalk, mode='a', header=printHeadWalk, index=False)
    printHeadWalk=False
    print("Walk chunk: "+str(i))





