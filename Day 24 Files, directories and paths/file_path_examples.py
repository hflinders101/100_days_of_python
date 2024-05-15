relative_file_path_to_main = '../../../OneDrive/Desktop/text_file.txt'
# C:\Users\hflin\PycharmProjects\100_days_of_python\Day 24 Files, directories and paths

normal_file_path = "C:/Users\hflin/OneDrive/Desktop/text_file.txt"
with open(relative_file_path_to_main, mode='r') as file: #Making this a variable so it doesn't use a lot of space
    # file.write('\n butts')
    contents = file.read()
    print(contents)
