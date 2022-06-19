import os
import pandas as pd

def new_data(df_main, df_baseline):
    cols = df_baseline.columns.tolist()
    for col in cols:
        df_main[col] = df_main[col] - df_baseline[col].mean()
    return df_main

def working_folders(path):

    os.chdir(path)

    for folder in os.listdir():
        os.chdir(folder)
        for file in os.listdir():
            if file == 'videos_emg_features_05_01.csv':
                df_main = pd.read_csv(file)
            elif file == 'baseline_emg_features_05_01.csv':
                df_baseline = pd.read_csv(file)
        new_data(df_main, df_baseline)
        df_main.to_csv('videos_emg_features_05_01.csv')
        os.chdir('..')

if __name__ == '__main__':
    path = '/home/bojan/praksa/Extracted_features'
    working_folders(path)