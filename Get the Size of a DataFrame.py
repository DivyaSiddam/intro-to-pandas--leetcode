#https://leetcode.com/problems/get-the-size-of-a-dataframe/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd

def getDataframeSize(players):
    df = pd.DataFrame(players)
    return [df.shape[0], df.shape[1]]
