# https://leetcode.com/problems/fill-missing-data/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def fillMissingValues(products):  
    df = pd.DataFrame(products, columns=['name', 'quantity', 'price'])
    df['quantity'] = df['quantity'].fillna(0)  
    return df
