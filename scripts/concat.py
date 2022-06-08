from operator import index
import os
import pandas as pd

def concat_csv(csv_file):
    paths = '/home/bojan/praksa/split_data'

    os.chdir(paths)
    for folder in os.listdir():
        os.chdir(folder)
        l = list()
        for folder2 in os.listdir():
            os.chdir(folder2)
            for folder3 in os.listdir():
                if folder3 == csv_file:
                    df1 = pd.read_csv(folder3)
                    l.append(df1)
            os.chdir('..')
        df = pd.DataFrame()
        df = pd.concat(l)
        df.to_csv('/home/bojan/praksa/concat_data/' + csv_file[:-4] + '_'+ folder + '.csv', index=False)
        os.chdir('..')


if __name__ == '__main__':
    csv_files = ['baseline_emg_features_05_01.csv', 'baseline_hrv_features.csv', 'calibration_emg_features_05_01.csv', 'videos_emg_features_05_01.csv', 'videos_hrv_features.csv']
    for csv_file in csv_files:
        concat_csv(csv_file)
    print('Task is done !')