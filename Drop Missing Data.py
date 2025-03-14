#https://leetcode.com/problems/drop-missing-data/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd

def dropMissingData(students):
    df = pd.DataFrame(students, columns=['student_id', 'name', 'age'])
    df = df.dropna(subset=['name'])  
    return df
