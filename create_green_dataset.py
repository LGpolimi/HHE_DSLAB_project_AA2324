import pandas as pd
import numpy as np

## Import datasets
tree_density = pd.read_csv('Datasources/tree_density.csv') #Import dataset about tree density
tree_density_binary = pd.read_csv('Datasources/tree_density_binary.csv') #Import dataset about tree density binary
grass_cover = pd.read_csv('Datasources/grass_stats.csv') #Import dataset about grass cover
small_woods = pd.read_csv('Datasources/small_woods.csv') #Import dataset about small woods
land_cover = pd.read_csv('Datasources/histograms_landcover.csv') #Import dataset about land cover


# Add grass cover
print(grass_cover.head(5))

final=grass_cover[["COMUNE","Shape_Area","_sum"]]
final.rename(columns={'_sum':'Grass_cover'})
print(final.tail(10))

for i in range(1,10):
    final.loc[[132+i],'COMUNE'] = 'Municipio'+str(i)
    final.loc[[132 + i], 'Shape_Area'] = grass_cover.loc[[132 + i],'AREA']

# Add small woods
print(small_woods.head(5))

final['Small_woods_cover']=small_woods["_sum"].copy()
print(final.tail(10))

# Add tree density
print(tree_density_binary.head(5))
print(tree_density.head(5))

final['Trees_cover']=tree_density_binary["_sum"].copy()
final['Trees_count']=tree_density["_sum"].copy()
final['Trees_mean_density']=tree_density["_mean"].copy()

print(final.tail(10))

# Add land cover
print(land_cover.head(5))

new_col=['Non_class_surf','Imper_surf','Perm_surf','Non_cons_surf','Hardwood','Coniferous','Shrubs','Periodic_herb','Permanent_herb','Permanent_water','Wetlands']
final[new_col]=land_cover.iloc[:,-11:].copy()

print(final.tail(10))





