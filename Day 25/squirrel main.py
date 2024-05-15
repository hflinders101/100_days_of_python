import pandas as pd

squirrel_df = pd.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240505.csv')
fur_color_series = squirrel_df['Primary Fur Color']
fur_counts = fur_color_series.value_counts()
counts_df = pd.DataFrame(fur_counts)
gray_squirrels_count = len(squirrel_df[fur_color_series == 'Gray'])
red_squirrels_count = len(squirrel_df[fur_color_series == 'Cinnamon'])
black_squirrels_count = len(squirrel_df[fur_color_series == 'Black'])

data_dict = {
    'Fur color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}
df = pd.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')

counts_df.to_csv('my_squirrel_data')