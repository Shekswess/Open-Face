import os
import pandas as pd

def classification(csv_file):

    dict = {1:'negative', 2:'negative', 3:'negative', 4: 'neutral', 5:'neutral', 6:'neutral',
            7:'positive', 8:'positive', 9:'positive'}

    path = '/home/bojan/praksa/concat_data/classification'
    os.chdir(path)
    #print(os.getcwd())
    for folder in os.listdir():
        os.chdir(folder)
        for folder2 in os.listdir():
            if folder2 == csv_file:
                    #print(folder3)
                    df = pd.read_csv(folder2)
                    df['class'] = df['valence'].map(dict)
                    df.to_csv('/home/bojan/praksa/concat_data/classification' + '/' + folder + '/' + folder2 , index=False)
        os.chdir('..')
                    

if __name__ == '__main__':
    csv_files = ['videos_emg_features_05_01_test.csv', 'videos_hrv_features_test.csv','videos_emg_features_05_01_train.csv', 'videos_hrv_features_train.csv','videos_emg_features_05_01_validation.csv', 'videos_hrv_features_validation.csv']
    for csv_file in csv_files:
        classification(csv_file)
    print('Task is done !')