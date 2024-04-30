import pandas as pd
df = pd.read_csv('Stazioni_qualit__dell_aria_20240430.csv')
print(df.columns)
## print df of columns 'provincia' and 'Location'
print(df[['Provincia', 'Comune', 'Location']])
## print unique values of 'Comune' column
print(df['Comune'].unique())
