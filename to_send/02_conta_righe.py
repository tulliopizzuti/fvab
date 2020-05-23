import pandas as pd
from os.path import  join
mainPath='/home/tullio/Projects/fvab_dataset'
fileName='JoinSensors.csv'
filePath=join(mainPath,fileName)

chunksize = 10 ** 5
total=0
i=0
for chunk in pd.read_csv(filePath, chunksize=chunksize):
    i+=1
    total+=chunk.shape[0]
    print(i,total)

'''
Dimensione blocco 100000
Dimensione ultimo blocco 20188
Risultato 
1185 blocchi 
118420188 righe

(Righe)
train set 70% = 82894131
test  set 30% = 35526057

(Blocchi)
train set 70% = 829
test  set 30% = 356


829 82900000


'''

