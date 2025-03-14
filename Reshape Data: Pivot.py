# https://leetcode.com/problems/reshape-data-pivot/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def pivotTable(weather):
    df = weather.pivot(index='month', columns='city', values='temperature')
    return df
