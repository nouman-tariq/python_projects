import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

weather_data = pd.read_csv('weatherAUS.csv')

test_data = weather_data[
    (weather_data['Location'] == 'Sydney') & 
    (weather_data['Date'] > '2015-01-01')]
test_data = test_data.reset_index()

cols = [1, 2, 5]
df = test_data[test_data.columns[cols]]


df.plot(x= 'Date', y= 'Rainfall', kind= 'scatter')
plt.show()