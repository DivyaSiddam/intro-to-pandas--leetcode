#https://leetcode.com/problems/reshape-data-melt/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def meltTable(report):
    df = pd.DataFrame(report, columns=['product', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'])
    reshaped_df = df.melt(id_vars=['product'], var_name='quarter', value_name='sales')
    return reshaped_df
