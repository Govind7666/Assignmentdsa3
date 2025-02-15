# -*- coding: utf-8 -*-
"""assignment3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Jbp0EFoa6IgCRlW5iyNHU7bg3TCTgFTS
"""

import numpy as np
import pandas as pd

data=pd.read_excel("/content/iris.xls")

# read the dataset to the python environment
data

# display the columns
print(data.columns)

# calculate the mean of each column of the dataset
print('Mean of SL:',data['SL'].mean())
print('Mean of SW:',data['SW'].mean())
print('Mean of PL:',data['PL'].mean())
print('Mean of PW:',data['PW'].mean())

# check for the null values present in the dataset
null_counts=data.isnull().sum
print(null_counts)

