#https://leetcode.com/problems/modify-columns/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd

def modifySalaryColumn(employees):
    df = pd.DataFrame(employees, columns=['name', 'salary'])
    df['salary'] = df['salary'] * 2  
    return df  
