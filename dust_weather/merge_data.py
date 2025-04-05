import pandas as pd

dust = pd.read_excel('./data/dust_final.xlsx')
weather = pd.read_excel('./data/weather_final.xlsx')

dust.shape     # (744, 11)
weather.shape  # (743, 6)

dust.drop(index=743, inplace=True)

df = pd.merge(dust, weather, on='date')

df.to_excel('./data/dust_weather.xlsx', index=False)
