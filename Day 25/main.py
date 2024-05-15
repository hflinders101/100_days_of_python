import csv
# with open('weather_data.csv') as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     # next(data, None) #Skipps headers I think
#     for row in data:
#         if row != 'temp'
#             temperatures.append(int(row[1]))

import pandas
data = pandas.read_csv('weather_data.csv')
# data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()
# print(temp_list)

average_temp = data['temp'].mean()

# print(data.condition)# Another way of doing data['condition']

# print(data[data.day == 'Monday']) #Great way to find a specific row
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# celcius_temp = monday.temp
# f_temp = celcius_temp*9/5 + 32
# print(f_temp)

# data_dict = {
#     'students': ['Amy', 'JAmes', 'Angela'],
#     'Scores': [ 76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data')
# print(data)