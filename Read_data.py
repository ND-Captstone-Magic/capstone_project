import pandas as pd

data = pd.read_csv('Charging_PA.csv',sep=',')

print(data.head(10))
print(data.info())
print(data['Port Type'].value_counts())
# Verteilung der öffentlich zugänglichen Ladepunkte auf die Bundesländer

#print(data.where(data['Postleitzahl'] >= 78460, inplace = True))