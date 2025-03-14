#https://leetcode.com/problems/method-chaining/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def findHeavyAnimals(animals):
    filtered_animals = animals[animals['weight'] > 100]
    sorted_animals = filtered_animals.sort_values(by='weight', ascending=False)
    names = sorted_animals[['name']]
    return names

#in just one line of code using method chaining 
#def findHeavyAnimals(animals):
    #return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]
