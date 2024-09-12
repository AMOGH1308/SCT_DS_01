import pandas as pd
import matplotlib.pyplot as plt


file_path = r'c:\Users\Admin\Downloads\API_SP.POP.TOTL_DS2_en_excel_v2_3401611.xls'  # Replace with your actual file path
df = pd.read_excel(file_path, skiprows=3)  


df.columns = df.columns.str.strip()


country_name = 'India'
df_country = df[df['Country Name'] == country_name]


df_country = df_country.iloc[:, 4:].transpose()  # Select all years' data and transpose
df_country.columns = ['Population']
df_country.index.name = 'Year'


df_country.index = df_country.index.astype(int)


plt.figure(figsize=(10, 6))
plt.bar(df_country.index, df_country['Population'], color='skyblue')
plt.title(f'Population Growth Over Time in {country_name}')
plt.xlabel('Year')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', linewidth=0.7)
plt.tight_layout()  
plt.show()

