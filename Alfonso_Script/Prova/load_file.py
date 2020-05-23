import numpy as np
import RBF
import csv
from sklearn.metrics import accuracy_score
reader = csv.reader(open("D:\\public_dataset\\100669\\100669_session_01\\Accelerometer.csv", "r"), delimiter=",")
x = list(reader)
data = np.array(x).astype("float")

train_y = data[0:4, 0]
train_x = data[0:4, 1:]

test_y = data[4:8, 0]
test_x = data[4:8, 1:]

RBF_CLASSIFIER = RBF.RBF(train_x, train_y, test_x, test_y, num_of_classes=2,k=2, std_from_clusters=False)

RBF_CLASSIFIER.fit()
