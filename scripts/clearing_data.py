import os
import pandas as pd

def deleting_NaN(csv_file):
    os.chdir('/home/bojan/praksa/concat_data')
    for folder in os.listdir():
        os.chdir(folder)
        #print(os.getcwd())
        for folder2 in os.listdir():
            os.chdir(folder2)
            #print(os.getcwd())
            for folder3 in os.listdir():
                if folder3 == csv_file:
                    #print(folder3)
                    df = pd.read_csv(folder3)
                    df = df.dropna(axis = 0, subset=['video'])
                    df.to_csv('/home/bojan/praksa/concat_data' + '/' + folder + '/' + folder2 + '/' + folder3, index=False)
            os.chdir('..')
        os.chdir('..')

if __name__ == '__main__':
    csv_files = ['videos_emg_features_05_01_test.csv', 'videos_hrv_features_test.csv','videos_emg_features_05_01_train.csv', 'videos_hrv_features_train.csv','videos_emg_features_05_01_validation.csv', 'videos_hrv_features_validation.csv']
    for csv_file in csv_files:
        deleting_NaN(csv_file)
    print('Task is done !')