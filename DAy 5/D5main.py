#Student heights activity
# Input a Python list of student heights
# student_heights = [151, 145, 179] #input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# total_height = 0
# length = 0
# for height in student_heights:
#     total_height += height
#     length += height/height
# average = int(round(total_height / length,0))
# print(f'total height = {total_height}')
# print(f'number of students = {int(length)}')
# print(f'average height = {average}')
# #----------------------------------

# #Highest score activity
# # Input a list of student scores
# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]#input().split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#
# # Write your code below this row 👇
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f'The highest score in the class is: {highest_score}')
#-----------------------------------------------------
# #Adding even numbers from input
# target = int(52) # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️
#
# # Write your code here 👇
# total = 0
# for n in range(0,target+1,2):
#     total += n
#     #alt way of doing it below
#     # if n % 2 == 0:
#     #     total += n
# print(total)
#---------------------------
#Fizzbuzz game
for n in range(1,101):
    if n % 5 == 0 and n % 3 ==0:
        print("FizzBuzz")
    elif n % 3 ==0:
            print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(f'{n}')