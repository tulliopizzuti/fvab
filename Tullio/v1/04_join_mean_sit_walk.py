import os
from os.path import join
from os import path
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import StandardScaler

mainPath = "/home/tullio/Scrivania/Projects/fvab_dataset/public_dataset100/03_MeanSitWalk/MeanSitWalk_1"
fileMeanSensors = "MeanSensors.csv"
filePathMeanSensors=join(mainPath,fileMeanSensors)
fileMeanSit = "MeanSensorsSit_1.csv"
filePathMeanSit=join(mainPath,fileMeanSit)
fileMeanWalk = "MeanSensorsWalk_1.csv"
filePathMeanWalk=join(mainPath,fileMeanWalk)
if path.exists(filePathMeanSensors): os.remove(filePathMeanSensors)
meanSitCsv=pd.read_csv(filePathMeanSit)
meanWalkCsv=pd.read_csv(filePathMeanWalk)

frames = [meanSitCsv, meanWalkCsv]
meanSensors=pd.concat(frames, ignore_index=True)
meanSensors=shuffle(meanSensors, random_state=0)
meanSensors.to_csv(filePathMeanSensors, header=True, index=False)