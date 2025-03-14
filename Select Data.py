#https://leetcode.com/problems/select-data/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd

def selectData(students):
    df = pd.DataFrame(students, columns=['student_id', 'name', 'age'])
    return df[df['student_id'] == 101][['name', 'age']]
