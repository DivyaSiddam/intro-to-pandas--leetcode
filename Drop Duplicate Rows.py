#https://leetcode.com/problems/drop-duplicate-rows/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd

def dropDuplicateEmails(customers):
    df = pd.DataFrame(customers, columns=['customer_id', 'name', 'email'])
    df = df.drop_duplicates(subset=['email']) 
    return df
