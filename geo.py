import pandas as pd
import geocoder

data = pd.read_csv("Parking_Violations_Issued_-_Fiscal_Year_2018.csv", nrows=5000)
data['latitude'] = 0.0
data['longitude'] = 0.0

for index, row in data.iterrows():
    s = ''
    if row['House Number'] is not None and str(row['House Number']) != 'nan':
        s += str(row['House Number']) + ', '
    if row['Street Name'] is not None and str(row['Street Name']) != 'nan':
        s += str(row['Street Name']) + ', '
    if row['Intersecting Street'] is not None and str(row['Intersecting Street']) != 'nan':
        s += str(row['Intersecting Street']) + ', '
    l = geocoder.google(s, key='YOUR_API_KEY')
    data.at[0, 'latitude'] = l.latlng[0]
    data.at[0, 'longitude'] = l.latlng[1]

data.to_excel('output.xlsx', sheet_name='sheet1')



