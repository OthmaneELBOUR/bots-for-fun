import os

dir_path = "C:/Users/othma/Desktop/"
os.mkdir(os.path.join(dir_path, "Bot For Fun"))

for entry in os.listdir(dir_path):
    file = os.path.join(dir_path, entry)
    if os.path.isfile(file):
        extension = file.split('.')[-1]
        if extension == "py":
            os.rename(file, os.path.join("C:/Users/othma/Desktop/","Bot For Fun/", entry))