import pandas as pd
import numpy as np
import os
df = pd.read_csv("homework4.txt", sep = ";", header = 0) #name of my document is homework4 as txt.
need_columns = ["Company", "Payment"]
print (df.groupby(need_columns)["Quantity"].sum()) #I need total number of credit or cash payment according to company.