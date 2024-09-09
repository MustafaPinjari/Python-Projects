import os 

text = input ("Input text To be search in multiple files : ")
path = input("Path : ")

def getfiles(path):
    f=0
    os.chdir(path)
    files = os.listdir()
    for file_name in files:
        abs_path = os.path.abspath(file_name)
        if os.path.isdir(abs_path):
            getfiles(abs_path)

        if os.path.isfile(abs_path):
             f = 1
             print(text + " found in ")
             final_path = os.path.abspath(file_name)
             print(final_path)
             return True
        
    if f == 1:
        print(text + " Not Found ! ")
        return False
    
getfiles(path)