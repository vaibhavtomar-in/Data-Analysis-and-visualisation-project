import pandas as pd
import matplotlib.pyplot as plot

df = pd.read_csv("D:\code\DAV_sem_5\project\data.csv")
df = df.set_axis(["CITY", "REGION",  "COUNTRY", "AIR_QUALITY", "WATER_POLLUTION"],axis= 'columns')
l1 = list(df.COUNTRY)
l2 = [x[slice(2,-1,1)] for x in l1]
df.COUNTRY = df.COUNTRY.replace(l1,l2)
df = df.drop(['REGION'], axis=1)
grouped = df.groupby(df.COUNTRY)
df_new = grouped.get_group("India")
df_new = df_new.sort_values(by=['AIR_QUALITY'])
df_new.plot.line(x="CITY", title="Air pollution and water quality")
df_new2 = df_new.sort_values(by=['WATER_POLLUTION'])
print(df_new2)
df_new2.plot.line(x= df_new2.Index,title="Air pollution and water quality")
plot.show(block=True)

df3 = df.drop(['CITY'], axis=1)
df3 =  df3.groupby(df3.COUNTRY).mean()
df3 = df3.sort_values(by=['AIR_QUALITY'])
# print(df3)
df3.plot.line(title="Air pollution and water quality")
plot.show(block = True)
df4 = pd.read_csv("D:\code\DAV_sem_5\project\Global_Education.csv", encoding='latin-1')
# print(df4)


