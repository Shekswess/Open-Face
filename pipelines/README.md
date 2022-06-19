# Description of the Pipelines

The scripts are used in this order:

- pipeline_1.ipynb
- pipeline_2.ipynb
- pipeline_3.ipynb
- pipeline_4.ipynb
- pipeline_5.ipynb
- pipeline_6.ipynb
- pipeline_7.ipynb

### pipeline_1.ipynb
In this notebook the aproach is typical classification with 3 classes (negative, neutral, positive valence) and looking for the best hyperparameters for the models

### pipeline_2.ipynb
In this notebook the aproach is regression of the valence values than mapping those values to a class and looking for the best hyperparameters for the models

### pipeline_3.ipynb
In this notebook the aproach is the best models from the last two pipelines but the data is scaled differently

### pipeline_4.ipynb
In this notebook the aproach is the best models from the last pipelines with different scaling for the data + undersampling the neutral class

### pipeline_5.ipynb
In this notebook the aproach is all the previous combinations of different scallings on the data + OneVsRest models

### pipeline_6.ipynb
In this notebook the aproach is all the previous best models but with baseline normalization of the data

### pipeline_7.ipynb
In this notebook the aproach is all the previous best models but with baseline normalization of the data + undersampling
