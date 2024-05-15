numbers = [1,2,3]
new_list = [n + 1 for n in numbers]
#new_list = [new_item for item in list] replace each key word

name = 'holten'
new_list = [letter for letter in name]

new_list = [n * 2 for n in range(1,5)]

#new_list = [new_item for item in list if test] replace each key word

names = ['Alex', 'Beth', 'Caronine', 'Elanore', 'Dave']
short_names = [name.upper() for name in names if len(name) < 5]
# new_dict = {new_key:new_value for (key,value) in dict.item() if test}
import random
students_scores = {student:random.randint(1,100) for student in names}
passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}
print(passed_students)


student_dict = {
    'students': ['Alex', 'Beth', 'Caronine', 'Elanore', 'Dave'],
    'scores': [45,67,85,34,57]
}

for (key,value) in student_dict.items():
    print(key)
    # print(value)

import pandas as pd
student_df = pd.DataFrame(student_dict)
# print(student_df)

#loop through each row in a df
for (index, row) in student_df.iterrows():
    # print(row.students)
    # print(row.scores)
    print(index)
    if row.students == 'Alex':
        print(row.scores)
