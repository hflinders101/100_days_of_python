print("The Love Calculator is calculating your score...")
name1 = "Kanye West" # What is your name?
name2 = "Kim Kardashian" # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
val_1 = 0
val_2 = 0
combined_names = (name1+name2).lower()
for letter in range(len(combined_names)):
  if combined_names[letter] == "t" or combined_names[letter] == "r" or combined_names[letter] == "u" or combined_names[letter] == "e":
      val_1 += 1
  if combined_names[letter] == "l" or combined_names[letter] == "o" or combined_names[letter] == "v" or combined_names[letter] == "e":
      val_2 += 1
total_score = int(f"{val_1}{val_2}")
if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40 < total_score < 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
