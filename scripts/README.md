# Description of the Scripts

The scripts are used in this order:

- dividing_data.py
- subject_column.py
- concat.py
- clearing_data.py
- classification_data.py

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
