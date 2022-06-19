# Description of the Scripts

The scripts are used in this order:

- baseline_normalization.py (optional)
- dividing_data.py
- subject_column.py
- concat.py
- clearing_data.py
- classification_data.py

### baseline_normalization.py
This script is making baseline normalization on the emg data using the baseline emg features. Basically from a feature
is substracted the mean of the same feature from the baseline emg data.

### dividing_data.py
This script is dividing the  into 3  datasets: 
-Train
-Validation
-Test

### subject_column.py
This script is adding one more column to every csv file that indicates from which subject(participant) is the data

### concat.py
This script is concatenating the csv files from every participant into one big csv file

### clearning_data.py
This script removes all the rows with NaN values in the video column, which basically means all the data when nothing is going on(no video is been watched)

### classification_data
This script adds another column, a class column that depends on the value of the valiance.
