#https://leetcode.com/problems/reshape-data-concatenate/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def concatenateTables(df1, df2):
    return pd.concat([df1, df2], axis=0)  
