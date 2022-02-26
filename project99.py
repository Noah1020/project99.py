import os
import shutil
import time

def main ():
    days = 30
    path = "/test folder"
    seconde = time.time() - days*24*60*60
    if os.path.exists(path):
        for folder, subfolder, files in os.walk(path):
            if seconde > os.stat(path).st_ctime:
                shutil.rmtree(path)
            else:
                for subfolder in folder:
                    folderpath = os.path.join(folder,subfolder) 
                    if seconde > os.stat(folderpath).st_ctime:
                        shutil.rmtree(folderpath)
                for files in folder:
                    filepath = os.path.join(folder,files)
                    if seconde > os.stat(filepath).st_ctime:
                        os.remove(filepath)
    else:
        print("path does not exists ")



main()            