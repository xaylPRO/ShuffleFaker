from os import *
from random import randint


filenames_list = []

for (dirpath, dirnames, filenames) in walk("music"):
    filenames_list.extend(filenames)

for file in filenames_list:
        print(file)
        i = randint(0, len(filenames_list))
        print(i)
        new_filename = str(i) + "." + file
        print(new_filename)
        rename("music/"+file, "music/" + new_filename)

