#https://leetcode.com/problems/create-a-dataframe-from-list/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd
def createDataframe(student_data):
  df = pd.DataFrame(student_data,columns=['student_id','age'])
  return df
