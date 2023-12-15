import matplotlib.pyplot as plt
import pandas as pd

# Inladen neerslagdata
df_neerslag = pd.read_csv('Neerslag_Hoogmade.csv', skipinitialspace=True, header=0, sep=';')

# Maak een datum kolom
df_neerslag['DateTime'] = pd.to_datetime(df_neerslag['datum'])  # format is voor notatie van de import

# Vervang NaN door 0
df_neerslag['neerslagintensiteit (mm/uur)'].fillna(0, inplace=True)

# RH waardes in een lijst zetten
neerslag = df_neerslag['neerslagintensiteit (mm/uur)'].tolist()

# Plot de DateTime tegenover de RH
plt.figure(figsize=(20, 10))
plt.plot(df_neerslag["DateTime"], df_neerslag["neerslagintensiteit (mm/uur)"], label="Neerslag (mm)")
plt.title("Neerslag over tijd")
plt.xlabel("Datum")
plt.ylabel("Neerslag [mm]")
plt.grid(True)
plt.legend()
plt.show()