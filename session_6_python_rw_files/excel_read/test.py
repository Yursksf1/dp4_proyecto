from __future__ import print_function

import pandas as pd
pd.__version__

california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
print(california_housing_dataframe.describe())

