import pandas as pd
df = pd.read_csv("C:/Users/blair/Desktop/data/ROUTES.csv", encoding='gbk')
save = pd.DataFrame(df.iloc[40000:50000], columns=['Departure', 'Destination'])
save.to_csv('C:/Users/blair/Desktop/data/TestTime/Rout5.csv', index=False)
