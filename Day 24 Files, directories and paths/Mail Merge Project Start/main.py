#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('../Mail Merge Project Start/Input/Letters/starting_letter.txt') as blank_letter_file:
    blank_letter_as_list = blank_letter_file.readlines()

with open(r'C:\Users\hflin\PycharmProjects\100_days_of_python\Day 24 Files, directories and paths\Mail Merge Project Start\Input\Names\invited_names.txt') as name_file:
    invited_names_list = name_file.readlines()
    counter = 0
    for names in invited_names_list:
        formatted_name = names.strip()
        invited_names_list[counter] = formatted_name
        counter += 1


for name in invited_names_list:
    invitation_line = blank_letter_as_list[0].replace('[name],',f'{name},')
    with open(f'../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt','w') as unformatted_letter:
        unformatted_letter.write(invitation_line)
        for line in blank_letter_as_list:
            if line == blank_letter_as_list[0]:
                continue
            unformatted_letter.write(line)