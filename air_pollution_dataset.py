import pandas as pd
df_stations = pd.read_csv('Air_quality_data/Stazioni_qualit__dell_aria_20240430.csv')
df_air_quality1 = pd.read_csv('Air_quality_data/Dati_sensori_aria_2010-2017_20240430.csv', low_memory=False)
df_air_quality2 = pd.read_csv('Air_quality_data/Dati_sensori_aria_dal_2018_20240430.csv', low_memory=False)
# Add the two dataframes together by row
df_air_quality = pd.concat([df_air_quality1, df_air_quality2], axis=0)
## Print the first few rows of the dataframe
print(df_air_quality.head())

print(df_stations.columns)
## print df of columns 'provincia' and 'Location'
print(df_stations[['Provincia', 'Comune', 'Location']])
## print unique values of 'Comune' column
print(df_stations['Comune'].unique())

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

## Print the number of municipalities in Milan
print(len(milan_municipalities))

## Make a list of municipalities in Milan that are not in the dataset
not_in_dataset = [municipality for municipality in milan_municipalities if municipality not in df_stations['Comune'].unique()]
print(not_in_dataset)

## Drop rows with municipalities not in the list of milan_municipalities
df_milano_stations = df_stations[df_stations['Comune'].isin(milan_municipalities)]
print(df_milano_stations['Comune'].unique())
## Print the number of municipalities in province of Milan that have air quality data
print(len(df_milano_stations['Comune'].unique()))

## Count the number of rows for each unique value in 'NomeTipoSensore' column
print(df_milano_stations['NomeTipoSensore'].value_counts())

## Get the list IdSensore for each unique value in 'NomeTipoSensore' column
print(df_milano_stations.groupby('NomeTipoSensore')['IdSensore'].unique())

## Print the number of rows in the air quality dataframe for each unique value in 'IdSensore' column
print(df_air_quality['idSensore'].value_counts())


## Print the number of rows in the air quality dataframe for each unique value in 'idSensore' column grouped by the year
print(df_air_quality.groupby(df_air_quality['Data'].str[6:10])['idSensore'].value_counts())

##Print the number of rows in the air quality dataframe for each year
print(df_air_quality['Data'].str[6:10].value_counts())






