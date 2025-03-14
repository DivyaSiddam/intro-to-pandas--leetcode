#https://leetcode.com/problems/display-the-first-three-rows/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd
def selectFirstRows(employees):
    df = pd.DataFrame(employees, columns=['employee_id', 'name', 'department', 'salary'])
    return df.head(3)


