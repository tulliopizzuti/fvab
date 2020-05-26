import pandas as pd
from os.path import join
from sklearn.utils import shuffle

mainPath = '/home/tullio/Projects/fvab_dataset/joined_dataset100'
fileName = 'JoinSensors.csv'
trainFileName = 'JoinSensorsTrain.csv'
testFileName = 'JoinSensorsTest.csv'

filePath = join(mainPath, fileName)
trainFilePath = join(mainPath, trainFileName)
testFilePath = join(mainPath, testFileName)

chunksize = 10 ** 2
nChunk=0
printHead = True
for chunk in pd.read_csv(filePath, chunksize=chunksize, index_col=False):
    nChunk+=1
print(nChunk)