import numpy as np
import pandas as pd
from os.path import join
from sklearn.utils import shuffle
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

mainFilePath = '/home/tullio/Projects/fvab_dataset/public_dataset'
fileDataset = "JoinSensors.csv"
pathDataset = join(mainFilePath, fileDataset)
columns = ["GestureScenario","XAcc", "YAcc", "ZAcc",
                                  "XGyro", "YGyro", "ZGyro",
                                  "XMagn", "YMagn", "ZMagn"]

csvDataset = pd.read_csv(pathDataset, index_col=False)

csvDataset = shuffle(csvDataset, random_state=0).reset_index(drop=True)

n = csvDataset.shape[0]
nTrain = int(n * 0.7)
nTest = int(n - nTrain)

accTrain = csvDataset.head(nTrain)
accTest = csvDataset.tail(nTest)

train_y = accTrain["GestureScenario"].to_numpy()
train_x = accTrain[
    ["XAcc", "YAcc", "ZAcc", "XGyro", "YGyro", "ZGyro", "XMagn", "YMagn", "ZMagn"]].to_numpy()
test_y = accTest["GestureScenario"].to_numpy()
test_x = accTest[
    ["XAcc", "YAcc", "ZAcc", "XGyro", "YGyro", "ZGyro", "XMagn", "YMagn", "ZMagn"]].to_numpy()

clf = MLPClassifier(
    random_state=0, max_iter=300, verbose=True).fit(train_x, train_y)
print(clf.score(test_x, test_y))
