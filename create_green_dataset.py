import pandas as pd
import numpy as np

## Import datasets
tree_density = pd.read_csv('Datasources/histograms_landcover.csv') #Import dataset about tree density
#grass_cover = pd.read_csv() #Import dataset about grass cover
#small_woods = pd.read_csv() #Import dataset about small woods
#land_cover = pd.read_csv() #Import dataset about land cover


print(tree_density.head(5))


final=tree_density["COMUNE"].to_frame()

# drop rows by index
final.drop(range(133,142), inplace = True)
municipi=[]
for i in range(1,10):
    municipi = np.append([municipi],['Municipio'+str(i)])
final = pd.concat([final,pd.DataFrame(columns=['COMUNE'],data=municipi)], ignore_index=True)



