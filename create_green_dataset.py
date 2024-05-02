import pandas as pd
import numpy as np

## Import datasets
tree_density = pd.read_csv('Datasources/tree_density.csv')                      # Import dataset about tree density
tree_density_binary = pd.read_csv('Datasources/tree_density_binary.csv')        # Import dataset about tree density binary
grass_cover = pd.read_csv('Datasources/grass_stats.csv')                        # Import dataset about grass cover
small_woods = pd.read_csv('Datasources/small_woods.csv')                        # Import dataset about small woods
land_cover = pd.read_csv('Datasources/histograms_landcover.csv')                # Import dataset about land cover

# Add grass cover
print(grass_cover.head(5))

final=grass_cover[["COMUNE","Shape_Area","_sum"]]
final.rename(columns={'_sum':'Grass_cover'}, inplace=True)
print(final.tail(10))

for i in range(1,10):
    final.loc[[132+i],'COMUNE'] = 'Municipio'+str(i)
    final.loc[[132 + i], 'Shape_Area'] = grass_cover.loc[[132 + i],'AREA']

print(final.tail(10))

# Check municipalities names
milan_municipalities = [
    'Abbiategrasso', 'Albairate', 'Arconate', 'Arese', 'Arluno', 'Assago',
    'Baranzate', 'Bareggio', 'Basiano', 'Basiglio', 'Bellinzago Lombardo', 'Bernate Ticino', 'Besate', 'Binasco', 'Boffalora Sopra Ticino', 'Bollate', 'Bresso', 'Bubbiano', 'Buccinasco', 'Buscate', 'Bussero', 'Busto Garolfo',
    'Calvignasco', 'Cambiago', 'Canegrate', 'Carpiano', 'Carugate', 'Casarile', 'Casorezzo', 'Cassano d\'Adda', 'Cassina de\' Pecchi', 'Cassinetta di Lugagnano', 'Castano Primo', 'Cernusco sul Naviglio', 'Cerro Maggiore', 'Cerro al Lambro', 'Cesano Boscone', 'Cesate', 'Cinisello Balsamo', 'Cisliano', 'Cologno Monzese', 'Colturano', 'Corbetta', 'Cormano', 'Cornaredo', 'Corsico', 'Cuggiono', 'Cusago', 'Cusano Milanino',
    'Dairago', 'Dresano',
    'Gaggiano', 'Garbagnate Milanese', 'Gessate', 'Gorgonzola', 'Grezzago', 'Gudo Visconti',
    'Inveruno', 'Inzago',
    'Lacchiarella', 'Lainate', 'Legnano', 'Liscate', 'Locate di Triulzi',
    'Magenta', 'Magnago', 'Marcallo con Casone', 'Masate', 'Mediglia', 'Melegnano', 'Melzo', 'Mesero', 'Milano', 'Morimondo', 'Motta Visconti',
    'Nerviano', 'Nosate', 'Novate Milanese', 'Noviglio',
    'Opera', 'Ossona', 'Ozzero',
    'Paderno Dugnano', 'Pantigliate', 'Parabiago', 'Paullo', 'Pero', 'Peschiera Borromeo', 'Pessano con Bornago', 'Pieve Emanuele', 'Pioltello', 'Pogliano Milanese', 'Pozzo D\'Adda', 'Pozzuolo Martesana', 'Pregnana Milanese',
    'Rescaldina', 'Rho', 'Robecchetto con Induno', 'Robecco sul Naviglio', 'Rodano', 'Rosate', 'Rozzano',
    'San Colombano al Lambro', 'San Donato Milanese', 'San Giorgio su Legnano', 'San Giuliano Milanese', 'San Vittore Olona', 'San Zenone al Lambro', 'Santo Stefano Ticino', 'Sedriano', 'Segrate', 'Senago', 'Sesto San Giovanni', 'Settala', 'Settimo Milanese', 'Solaro',
    'Trezzano Rosa', 'Trezzano sul Naviglio', 'Trezzo sull\'Adda', 'Tribiano', 'Truccazzano', 'Turbigo',
    'Vanzaghello', 'Vanzago', 'Vaprio d\'Adda', 'Vermezzo con Zelo', 'Vernate', 'Vignate', 'Villa Cortese', 'Vimodrone', 'Vittuone', 'Vizzolo Predabissi',
    'Zibido San Giacomo'
]

check_true=0
check_false=0
for i in range(len(milan_municipalities)):
    if milan_municipalities[i] == final.loc[i, 'COMUNE']:
        check_true = check_true+1;
    else:
        print(milan_municipalities[i])
        print(final.loc[i, 'COMUNE'])
        check_false = check_false + 1;

if check_false == 0:
    print("All municipalities are correct")

# Change values
final.replace('Boffalora sopra Ticino','Boffalora Sopra Ticino', inplace=True)
dict_munic = {'Municipio1': 'Centro',
'Municipio2': 'Stazione Centrale, Gorla, Turro, Greco, Crescenzago',
'Municipio3': 'Città Studi, Lambrate, Venezia',
'Municipio4': 'Vittoria, Forlanini',
'Municipio5': 'Vigentino, Chiaravalle, Gratosoglio',
'Municipio6': 'Barona, Lorenteggio',
'Municipio7': 'Baggio, De Angeli, San Siro',
'Municipio8': 'Fiera, Gallaratese, Quarto Oggiaro',
'Municipio9': 'Stazione Garibaldi, Niguarda'}
final = final.replace(dict_munic)
print(final.tail(10))

# Add small woods
print(small_woods.head(5))

final['Small_woods_cover']=small_woods["_sum"].copy()
print(final.tail(10))

# Add tree density
print(tree_density_binary.head(5))
print(tree_density.head(5))

final['Trees_cover']=tree_density_binary["_sum"].copy()
final['Trees_mean_density']=tree_density["_mean"].copy() # not to normalize

print(final.tail(10))

# Add land cover
print(land_cover.head(5))

new_col=['Non_class_surf','Imper_surf','Perm_surf','Non_cons_surf','Hardwood','Coniferous','Shrubs','Periodic_herb','Permanent_herb','Permanent_water','Wetlands']
final[new_col]=land_cover.iloc[:,-11:].copy()

print(final.head(10))

# Normalized dataset over the area
final_norm=final.copy()
# visualize type of columns
print(final_norm.dtypes)

# Change int columns to float
columns=[]
for col in final_norm.columns:
    columns.append(col)

for col in columns:
    if final_norm[col].dtype == 'int64':
        final_norm[col]=final_norm[col].astype('float64')
print(final_norm.dtypes)

# Transform shape area to make correct divisions
final_norm.iloc[:,1]=final_norm.iloc[:,1]/100.0

# Normalize columns
for i in range(2,17):
    if i != 5:
        final_norm.iloc[:,i]=final_norm.iloc[:,i]/final_norm['Shape_Area']
        print(i)
    else:
        final_norm.iloc[:, i] = final_norm.iloc[:, i]/100.0

print(final_norm.max())
print(final_norm.min())

# Ripristinate the original shape area
final_norm.iloc[:,1]=final_norm.iloc[:,1]*100.0


# Save the dataset
final_norm.to_csv('C:/Users/user/Desktop/HHE_DSLAB_project_AA2324/final_greenareas.csv')


#Compute maximum of land cover
maxvalues=final_norm.iloc[:,-11:].max(axis=1)

indices=[]
for i in range(0,len(maxvalues)):
    ind=np.where(final_norm.iloc[i,-11:] == maxvalues[i])
    indices.append(ind[0][0])

final_norm['Max_landcover']=indices


for i in range(0,len(new_col)):
    final_norm['Max_landcover'].replace(i, new_col[i], inplace=True)


final_norm.to_csv('C:/Users/user/Desktop/HHE_DSLAB_project_AA2324/final_greenareas_withmax.csv')