import os, random
import shutil


if __name__ == '__main__':

    path = '/home/bojan/praksa/Extracted_features'
    number_folder = len(os.listdir(path))

    names_folder = list()

    # Get all the names of the folders
    for i in range(number_folder):
        names_folder.append(os.listdir(path)[i])

    os.mkdir('/home/bojan/praksa/split_data')
    os.mkdir('/home/bojan/praksa/split_data/train')
    os.mkdir('/home/bojan/praksa/split_data/test')
    os.mkdir('/home/bojan/praksa/split_data/validation')

    for i in range(number_folder):
        number = names_folder[i][-2:]
        if number == '02' or number == '08' or number == '13' or number == '17' or number == '28':
            shutil.copytree(path + '/' + names_folder[i], '/home/bojan/praksa/split_data/test/' + names_folder[i])
        elif number == '03' or number == '06' or number == '12' or number == '20' or number == '25':\
            shutil.copytree(path + '/' + names_folder[i], '/home/bojan/praksa/split_data/validation/' + names_folder[i])
        else:
            shutil.copytree(path + '/' + names_folder[i], '/home/bojan/praksa/split_data/train/' + names_folder[i])