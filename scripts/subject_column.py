import os
import pandas as pd


def adding_subject_column(csv_file):
    os.chdir('/home/bojan/praksa/split_data')
    for folder in os.listdir():
        os.chdir(folder)
        print(os.getcwd())
        for folder2 in os.listdir():
            os.chdir(folder2)
            print(os.getcwd())
            number = folder2[-2:]
            print(number)
            for folder3 in os.listdir():
                if folder3 == csv_file:
                    df = pd.read_csv(folder3)
                    print(folder3)
                    if 'Subject' in df.columns:
                        pass
                    else:
                        df.insert(0,'Subject', 'Subject ' + number)
                        df.to_csv('/home/bojan/praksa/split_data' + '/' + folder + '/' + folder2 + '/' + folder3, index=False)
                else:
                    pass
            os.chdir('..')
        os.chdir('..')

if __name__ == '__main__':
    csv_files = ['baseline_emg_features_05_01.csv', 'baseline_hrv_features.csv', 'calibration_emg_features_05_01.csv', 'videos_emg_features_05_01.csv', 'videos_hrv_features.csv']
    for csv_file in csv_files:
        adding_subject_column(csv_file)
    print('Task is done !')