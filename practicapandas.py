import pandas as pd

edadescasa1 = [23, 24, 25, 25, 28]
edadescasa2 = [1, 4, 24, 26, 70]

dataframe1 = pd.DataFrame(edadescasa1)
dataframe2 = pd.DataFrame(edadescasa2)

print(dataframe1.describe())
print('')
print(dataframe2.describe())

