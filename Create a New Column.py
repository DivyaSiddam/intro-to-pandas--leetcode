#https://leetcode.com/problems/create-a-new-column/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd

def createBonusColumn(employees):
    df = pd.DataFrame(employees, columns=['name', 'salary'])
    df['bonus'] = df['salary'] * 2  # Creating the bonus column
    return df
