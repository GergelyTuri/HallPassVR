#clean historyComb.txt
#historyPath.txt
#path.txt
#Pattern2Path.txt
#HistoryComb
#HistoryPath
import os
import shutil

def deleteallfile(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        #print(file_path)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                #print("deal 1")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                #print("deal 2")
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


historyComb  = open("historyCombCount.txt", "r+")
historyPath  = open("historyPath.txt","r+")
path         = open("path.txt", "r+")
Pattern2Path = open("Pattern2Path.txt", "r+")

historyComb .truncate(0)
historyPath .truncate(0)
path        .truncate(0)
Pattern2Path.truncate(0)

historyComb.close()
historyPath.close()
path.close()
Pattern2Path.close()


folder1 = "image/HistoryComb"
folder2 = "image/HistoryPath"

deleteallfile(folder1)
deleteallfile(folder2)