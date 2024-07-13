#
# try:
#     file = open('a_file.txt')
#     dict = {'1':'2'}
#     print(dict['1'])
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write('something')
# except KeyError as error_message:
#     print(f'the key {error_message} deos not exist')
# else: #When nothing breaks this happens
#     content = file.read()
#     print(content)
# finally: #happens no matter what
#     # file.close()
#     # print('File was closed')
#     raise TypeError('Made up error')
#

height = float(input('Height: '))
weight = int(input('WEight: '))

bmi = weight / height**2
print(bmi)
if height > 3:
    raise ValueError('Human heihgt shoudl nto be greater than 3m')
