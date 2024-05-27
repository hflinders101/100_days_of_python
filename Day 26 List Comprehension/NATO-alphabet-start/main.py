student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
import pandas as pd
nato_df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row.letter:row['code'] for (index, row) in nato_df.iterrows()}

# 2. Create a list of the phonetic code words from a word that the user inputs.

name_input = input('What would you like to convert to NATO alphabet?: ').upper()
# for letter in name_input:
#     print(nato_alphabet_dict[letter])
output_list = [nato_alphabet_dict[letter] for letter in name_input]
print(output_list)