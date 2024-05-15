with open('file1.txt', mode='r') as f1:
    f1_list = f1.readlines()

with open('file2.txt', mode='r') as f2:
    f2_list = f2.readlines()

#new_list = [new_item for item in list if test] replace each key word
result = [int(n) for n in f1_list if (n in f2_list)]
# print(type(f1_list))
# print(f2_list)

print(result)
