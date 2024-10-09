import pandas as pd
print("Prepade data:")

# Src to file
input_file = 'DATA/Info_BDApnea_QuironMalaga.xlsx'
output_file = 'DATA/Copilot_OSA_DB_UPM.xlsx'

# Read Excel file
df = pd.read_excel(input_file)

# Wczytaj tylko wybrane kolumny z pliku Excel
df = pd.read_excel(input_file, usecols=['Patient', 'Gender', 'Edad', 'Talla', 'Peso', 'IAH', 'PerCervical'])

# Change columns name
df = df.rename(columns={
    'Edad': 'Age',
    'Talla': 'Height',
    'Peso': 'Weight',
    'PerCervical': 'Cervical'
})

# Convert column 'Weight' ->  float
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')

# Delete rows with NA or value '-1'
df = df.replace(-1, pd.NA)  # Zastąp -1 wartością NaN
df = df.dropna()  # Usuń wiersze zawierające NaN

# Save new version DataFrame to Excel file
df.to_excel(output_file, index=False)