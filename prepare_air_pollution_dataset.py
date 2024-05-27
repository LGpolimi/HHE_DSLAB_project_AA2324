import pandas as pd
import numpy as np

df_stations = pd.read_csv('Air_quality_data/Stazioni_qualit__dell_aria_20240430.csv')
df_air_quality1 = pd.read_csv('Air_quality_data/Dati_sensori_aria_2010-2017_20240430.csv', low_memory=False)
df_air_quality2 = pd.read_csv('Air_quality_data/Dati_sensori_aria_dal_2018_20240430.csv', low_memory=False)

# Add the two dataframes together by row
df_air_quality = pd.concat([df_air_quality1, df_air_quality2], axis=0)

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

## Drop rows with municipalities not in the list of milan_municipalities
df_milano_stations = df_stations[df_stations['Comune'].isin(milan_municipalities)]
print(df_milano_stations['Comune'].unique())

## Remove column 'idOperatore' from the air quality dataframe
df_air_quality = df_air_quality.drop('idOperatore', axis=1)
df_air_quality.head()

## Rename the column 'idSensore' to 'IdSensore' in the air quality dataframe
df_air_quality = df_air_quality.rename(columns={'idSensore': 'IdSensore'})
df_air_quality.head()

## Add 'UnitaMisura' column to the air quality dataframe based on the 'IdSensore' column
df_air_quality = df_air_quality.merge(df_milano_stations[['IdSensore', 'UnitaMisura']], on='IdSensore')
df_air_quality.head()

## Append the column 'NomeTipoSensore' to the air quality dataframe based on the 'IdSensore' column
df_air_quality = df_air_quality.merge(df_milano_stations[['IdSensore', 'NomeTipoSensore']], on='IdSensore')
df_air_quality.head()

## Remove rows where 'NomeTipoSensore' has the value 'Cadmio', 'Benzo(a)pirene', 'Nikel', 'Piombo', 'Arsenico', 'Ammoniaca', 'BlackCarbon', 'Particelle sospese PM2.5', 'Benzene'
df_air_quality = df_air_quality[~df_air_quality['NomeTipoSensore'].isin(['Cadmio', 'Benzo(a)pirene', 'Nikel', 'Piombo', 'Arsenico', 'Ammoniaca', 'BlackCarbon', 'Particelle sospese PM2.5', 'Benzene'])]
df_air_quality.head()

## Convert the column 'Date' to datetime
df_air_quality['Data'] = pd.to_datetime(df_air_quality['Data'], dayfirst=True)
df_air_quality.head()

## Add columns 'Year', 'Month', 'Day', 'Hour' to the air quality dataframe based on the 'Data' column
df_air_quality['Year'] = df_air_quality['Data'].dt.year
df_air_quality['Month'] = df_air_quality['Data'].dt.month
df_air_quality['Day'] = df_air_quality['Data'].dt.day
df_air_quality['Hour'] = df_air_quality['Data'].dt.hour
df_air_quality.head()

## Append the column 'Comune' to the air quality dataframe based on the 'IdSensore' column
df_air_quality = df_air_quality.merge(df_milano_stations[['IdSensore', 'Comune']], on='IdSensore')
df_air_quality.head()

## Put NaN in  rows with values less than 0 in the column 'Valore' in the air quality dataframe
df_air_quality.loc[df_air_quality['Valore'] < 0, 'Valore'] = np.nan

## Save the air quality dataframe to a csv file
df_air_quality.to_csv('df_air_quality_dateTime.csv', index=False)