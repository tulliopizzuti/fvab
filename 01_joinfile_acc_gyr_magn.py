import pandas as pd
import os
from os import listdir, path
from os.path import isdir, join
#Nome e descrittore di colonne per il file activity.csv
activityName = "Activity.csv"
activityColumns = ["ActivityID", "SubjectID", "SessionNumber", "StartTime", "EndTime", "RelativeStartTime",
                   "RelativeEndTime", "GestureScenario", "TaskID", "ContentID"]
#Nome e descrittore di colonne per il file accelerometer.csv
accelerometerName = "Accelerometer.csv"
accelerometerColumns = ["SysTime", "EventTime", "ActivityID", "X", "Y", "Z", "PhoneOrientation"]
#Nome e descrittore di colonne per il file gyroscope.csv
gyroscopeName = "Gyroscope.csv"
gyroscopeColumns = ["SysTime", "EventTime", "ActivityID", "X", "Y", "Z", "PhoneOrientation"]
#Nome e descrittore di colonne per il file magnetometer.csv
magnetometerName = "Magnetometer.csv"
magnetometerColumns = ["SysTime", "EventTime", "ActivityID", "X", "Y", "Z", "PhoneOrientation"]
#Path principale del dataset, contenente le cartelle con le sessioni dei soggetti
mainPath = "/home/tullio/Projects/fvab_dataset/public_dataset"
#File generati dopo l'esecuzione
csvJoinedAccelerometer = join(mainPath, "JoinedAccelerometer.csv")
csvJoinedGyroscope = join(mainPath, "JoinedGyroscope.csv")
csvJoinedMagnetometer = join(mainPath, "JoinedMagnetometer.csv")
logFilePath=join(mainPath, "file.log")
#Controllo che cancella i file nel caso siano già esistenti
if path.exists(csvJoinedAccelerometer): os.remove(csvJoinedAccelerometer)
if path.exists(csvJoinedGyroscope): os.remove(csvJoinedGyroscope)
if path.exists(csvJoinedMagnetometer): os.remove(csvJoinedMagnetometer)
if path.exists(logFilePath): os.remove(logFilePath)
#Apro il file di log
logFile = open(logFilePath,'a')
# Colonne da estrarre sui file joinati
columnExtract = ["ActivityID","SubjectID", "SysTime", "GestureScenario", "X", "Y", "Z", "PhoneOrientation"]
#Estrazione della lista delle cartelle dei soggetti
subjectDirectories = [f for f in listdir(mainPath) if isdir(join(mainPath, f))]
subjectDirectories.sort()
#Modifica nome cartelle per mantenere l'ordinamento corretto
for dir in subjectDirectories:
    subjectDirectory = join(mainPath, dir)
    sessionDirectories = [f for f in listdir(subjectDirectory) if isdir(join(subjectDirectory, f))]
    for sessionDirectory in sessionDirectories:
        splitted = sessionDirectory.split('_')
        splitted[2] = splitted[2].rjust(2, '0')
        newName = ('_'.join(splitted))
        os.rename(join(subjectDirectory, sessionDirectory), join(subjectDirectory, newName))
#Inizio scorrimento cartelle
for dir in subjectDirectories:
    #Path cartella soggetto
    subjectDirectory = join(mainPath, dir)
    #Lista sessioni del soggetto
    sessionDirectories = [f for f in listdir(subjectDirectory) if isdir(join(subjectDirectory, f))]
    sessionDirectories.sort()
    #Scorrimento sessioni
    for sessionDirectory in sessionDirectories:
        #Path cartella sessione
        path = join(subjectDirectory, sessionDirectory)
        accelerometerFile = join(path, accelerometerName)
        gyroscopeFile = join(path, gyroscopeName)
        magnetometerFile = join(path, magnetometerName)
        #Stringa di log
        log = dir + ": " + sessionDirectory + "\nAccelerometro: " + accelerometerFile + "\nGiroscopio: " + gyroscopeFile + "\nMagnetometro: " + magnetometerFile + "\n"
        #Apertura file activity e assegnazione nomi colonne
        activityCsv = pd.read_csv(join(path, activityName), header=None)
        activityCsv.columns = activityColumns
        #Apertura file accelerometro e assegnazione nomi colonne
        try:
            accelerometerCsv = pd.read_csv(accelerometerFile, header=None)
            accelerometerCsv.columns = accelerometerColumns
            #Join sui file accelerometro e activity
            joined = accelerometerCsv.merge(activityCsv, on="ActivityID")
            df = joined[columnExtract]
            #Append join sul file accelerometro
            df.to_csv(csvJoinedAccelerometer, mode='a', header=False, index=False)
        except:
            log += "Accelerometro skyppato\n"
        # Apertura file giroscopio e assegnazione nomi colonne
        try:
            gyroscopeCsv = pd.read_csv(gyroscopeFile, header=None)
            gyroscopeCsv.columns = gyroscopeColumns
            #Join sui file giroscopio e activity
            joined = gyroscopeCsv.merge(activityCsv, on="ActivityID")
            #Estrazione colonne
            df = joined[columnExtract]
            #Append join sul file giroscopio
            df.to_csv(csvJoinedGyroscope, mode='a', header=False, index=False)
        except:
            log += "Giroscopio skyppato\n"
        # Apertura file magnetometro e assegnazione nomi colonne
        try:
            magnetometerCsv = pd.read_csv(magnetometerFile, header=None)
            magnetometerCsv.columns = magnetometerColumns
            #Join sui file magnetometro e activity
            joined = magnetometerCsv.merge(activityCsv, on="ActivityID")
            #Estrazione colonne
            df = joined[columnExtract]
            #Append join sul file magnetometro
            df.to_csv(csvJoinedMagnetometer, mode='a', header=False, index=False)
        except:
            log += "Magnetometro skyppato\n"
        #Completamento
        print(log)
        logFile.write(log)
    logFile.flush()
logFile.close()