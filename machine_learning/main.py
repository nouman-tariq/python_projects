import pandas as pd

weather_data = pd.read_csv('weatherAUS.csv')
test_data = weather_data[
    (weather_data['Location'] == 'Sydney') & 
    (weather_data['Date'] > '2015-01-01')]



print(test_data)