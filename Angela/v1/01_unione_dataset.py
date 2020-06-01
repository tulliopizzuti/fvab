import os
from os.path import isdir, join
from os import listdir, path
import pandas as pd


def filterRowActivityScenarioOrientation(row):
    return (row["ActivityIDAcc"] == row["ActivityIDAcc"] == row["ActivityIDAcc"] and
            row["GestureScenarioAcc"] == row["GestureScenarioGyro"] == row["GestureScenarioMagn"] and
            row["PhoneOrientationAcc"] == row["PhoneOrientationGyro"] == row["PhoneOrientationMagn"])


# N° di cartelle da analizzare
firstNFolder = 100
total=firstNFolder*24
# Nome e descrittore di colonne per il file activity.csv
activityName = "Activity.csv"
activityColumns = ["ActivityID", "SubjectID", "SessionNumber", "StartTime", "EndTime", "RelativeStartTime",
                   "RelativeEndTime", "GestureScenario", "TaskID", "ContentID"]
sensorsColumns = ["SysTime", "EventTime", "ActivityID", "X", "Y", "Z", "PhoneOrientation"]
columnExtract = ["ActivityID", "SubjectID", "SysTime", "GestureScenario", "X", "Y", "Z", "PhoneOrientation"]
columnExtractAcc = ["ActivityIDAcc", "SubjectIDAcc", "SysTimeAcc", "GestureScenarioAcc", "XAcc", "YAcc", "ZAcc",
                    "PhoneOrientationAcc"]
columnExtractGyro = ["ActivityIDGyro", "SubjectIDGyro", "SysTimeGyro", "GestureScenarioGyro", "XGyro", "YGyro", "ZGyro",
                     "PhoneOrientationGyro"]
columnExtractMagn = ["ActivityIDMagn", "SubjectIDMagn", "SysTimeMagn", "GestureScenarioMagn", "XMagn", "YMagn", "ZMagn",
                     "PhoneOrientationMagn"]
# Nome file accelerometer.csv
accelerometerName = "Accelerometer.csv"
# Nome file gyroscope.csv
gyroscopeName = "Gyroscope.csv"
# Nome magnetometer.csv
magnetometerName = "Magnetometer.csv"

joinedFile = "JoinSensors.csv"

# Path principale del dataset, contenente le cartelle con le sessioni dei soggetti
mainPath = "C:\\Users\\angel\\OneDrive\\Desktop\\progettoBiometria\\hmog_dataset\\public_dataset"

joinedFilePath = join(mainPath, joinedFile)
if path.exists(joinedFilePath): os.remove(joinedFilePath)
# Estrazione della lista delle cartelle dei soggetti
subjectDirectories = [f for f in listdir(mainPath) if isdir(join(mainPath, f))]
subjectDirectories.sort()
printHead = True
# Modifica nome cartelle per mantenere l'ordinamento corretto
for dir in subjectDirectories:
    subjectDirectory = join(mainPath, dir)
    sessionDirectories = [f for f in listdir(subjectDirectory) if isdir(join(subjectDirectory, f))]
    for sessionDirectory in sessionDirectories:
        splitted = sessionDirectory.split('_')
        splitted[2] = splitted[2].rjust(2, '0')
        newName = ('_'.join(splitted))
        os.rename(join(subjectDirectory, sessionDirectory), join(subjectDirectory, newName))
# Inizio scorrimento cartelle
for dir in subjectDirectories:
    if (firstNFolder <= 0):
        break
    firstNFolder -= 1
    # Path cartella soggetto
    subjectDirectory = join(mainPath, dir)
    # Lista sessioni del soggetto
    sessionDirectories = [f for f in listdir(subjectDirectory) if isdir(join(subjectDirectory, f))]
    sessionDirectories.sort()
    # Scorrimento sessioni
    for sessionDirectory in sessionDirectories:
        # Path cartella sessione
        path = join(subjectDirectory, sessionDirectory)
        accelerometerFile = join(path, accelerometerName)
        gyroscopeFile = join(path, gyroscopeName)
        magnetometerFile = join(path, magnetometerName)
        activityCsv = pd.read_csv(join(path, activityName), header=None, names=activityColumns)
        accelerometerCsv = pd.read_csv(accelerometerFile, header=None, names=sensorsColumns)
        gyroscopeCsv = pd.read_csv(gyroscopeFile, header=None, names=sensorsColumns)
        magnetometerCsv = pd.read_csv(magnetometerFile, header=None, names=sensorsColumns)
        joined = accelerometerCsv.merge(activityCsv, on="ActivityID")
        dfAcc = joined[columnExtract]
        dfAcc.columns = columnExtractAcc
        joined = gyroscopeCsv.merge(activityCsv, on="ActivityID")
        dfGyro = joined[columnExtract]
        dfGyro.columns = columnExtractGyro
        joined = magnetometerCsv.merge(activityCsv, on="ActivityID")
        dfMagn = joined[columnExtract]
        dfMagn.columns = columnExtractMagn
        maxLen = min(dfAcc.shape[0], dfGyro.shape[0], dfMagn.shape[0])
        result = pd.concat([dfAcc.head(maxLen), dfGyro.head(maxLen), dfMagn.head(maxLen)], axis=1, sort=False)

        result = result[result.apply(filterRowActivityScenarioOrientation, axis=1)]
        result = result[[
            "GestureScenarioAcc",
            "XAcc", "YAcc", "ZAcc",
            "XGyro", "YGyro", "ZGyro",
            "XMagn", "YMagn", "ZMagn"]]
        result.columns = [
            "GestureScenario",
            "XAcc", "YAcc", "ZAcc",
            "XGyro", "YGyro", "ZGyro",
            "XMagn", "YMagn", "ZMagn"]
        result.to_csv(joinedFilePath, mode='a', header=printHead, index=False)
        printHead = False
        total-=1
        print(total)
