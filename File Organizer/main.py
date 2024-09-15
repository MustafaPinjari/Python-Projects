import os
import shutil
os.chdir("Path to organize folder with different categories")

files = os.listdir()

extensions = {
    "images" : [".jpg", ".jpeg", ".png", ".gif"],
    "video" : [".mp4", ".mkv"],
    "music" : [".mp3", ".wav"],
    "zip" : [".zip", ".rar",".tgz",".tar"],
    "documents" : [".pdf",".docx",".csv",".xlsx",".pptx",".doc",".ppt",".xls"],
    "setup" : [".msi",".exe"],
    "program" : [".py",".c",".cpp",".java",".js",".php"],
    "design" : [".xd",".psd"]
}

def sorting(file):
    keys = list(extensions.keys())
    for key in keys:
        for ext in extensions[key]:
            if file.endswith(ext):
                return key
            
for file in files:
    dist = sorting(file)
    if dist:
        try:
            shutil.move(file, "../download-sorting/"+dist)
        except:
            print(file + "is already in " + dist)
    else:
        try:
            shutil.move(file, "../download-sorting/other")
        except:
            print(file + "is already in other")