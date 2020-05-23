import pandas as pd
from os.path import join

mainPath = '/home/tullio/Projects/fvab_dataset/joined_dataset100'
fileName = 'JoinSensors.csv'
trainFileName = 'JoinSensorsTrain.csv'
testFileName = 'JoinSensorsTest.csv'
from sklearn.utils import shuffle

filePath = join(mainPath, fileName)
trainFilePath = join(mainPath, trainFileName)
testFilePath = join(mainPath, testFileName)

chunksize = 10 ** 5
printHead = True
chunkTrain = 829
i=0
for chunk in pd.read_csv(filePath, chunksize=chunksize, index_col=False):
    printFile = testFilePath if chunkTrain <=0 else trainFilePath
    chunk = shuffle(chunk, random_state=0).reset_index(drop=True)
    chunk.to_csv(printFile, mode='a', header=printHead, index=False)
    i+=1
    chunkTrain-=1
    printHead = True if chunkTrain == 0 else False
    print(i,chunkTrain,printFile)

