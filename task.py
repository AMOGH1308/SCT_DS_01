import pandas as pd
import matplotlib.pyplot as plt


file_path = r'c:\Users\Admin\Downloads\API_SP.POP.TOTL_DS2_en_excel_v2_3401611.xls'  
df = pd.read_excel(file_path, skiprows=3)  
df.columns = df.columns.str.strip()
print(df.columns)  
country_name = "India"
country_data = df[df['Country Name'] == country_name].iloc[:, 4:]  
country_data = country_data.transpose()
country_data.columns = ['Population']
country_data.index.name = 'Year'
country_data.index = country_data.index.astype(int)
plt.figure(figsize=(10, 6))
plt.plot(country_data.index, country_data['Population'], marker='o', color='skyblue', linestyle='-')
plt.title(f'Population Growth Over Time in {country_name}')
plt.xlabel('Year')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
