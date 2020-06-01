from os import listdir, path
from os.path import isdir,join

mainPath = "C:\\Users\\angel\\OneDrive\\Desktop\\progettoBiometria\\hmog_dataset\\public_dataset"
listaCartelleUsatePath=join(mainPath, "cartelle.log")

#Apro il file di log
listaCartelleUsate = open(listaCartelleUsatePath,'a')

subjectDirectories = [f for f in listdir(mainPath) if isdir(join(mainPath, f))]

for dir in subjectDirectories:
    #Path cartella soggetto
    subjectDirectory = join(mainPath, dir)
    log= dir + "\n"
    listaCartelleUsate.write(log)
listaCartelleUsate.close()
